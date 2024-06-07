import inspect
import json
import os
from pathlib import Path
import time
import logging
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from langchain_openai import AzureChatOpenAI
from wbmulticrew.page_code import generate_section_code
from wbmulticrew.parse_json import make_page_files

from wbmulticrew.tools.dalle_tool import Dalle_Image
from wbmulticrew.tools.file_tools import file_write_tool
import yaml


# import agentops

# agentops.init("website_builder")
# Initialize logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Configuration
base_dir = os.path.dirname(os.path.abspath(__file__))
CONFIG = {
    "azure_endpoint": "https://answerai-bilal.openai.azure.com/",
    "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
    "azure_deployment": "gpt4o-azure",
    "api_version": "2024-02-15-preview",
    "embeddings_azure_deployment": "text-ada-bilal",
    "project_name": "test_3page",
    "agents_config": os.path.join(base_dir, "config/agents.yaml"),
    "tasks_config": os.path.join(base_dir, "config/tasks.yaml"),
    "agents2_config": os.path.join(base_dir, "config/agents2.yaml"),
    "tasks2_config": os.path.join(base_dir, "config/tasks2.yaml"),
}

azure_gpt4o = AzureChatOpenAI(
    azure_endpoint=CONFIG["azure_endpoint"],
    api_key=CONFIG["api_key"],
    azure_deployment=CONFIG["azure_deployment"],
    api_version=CONFIG["api_version"],
)

dalle_tool = Dalle_Image()

file_writer_tool = file_write_tool()

USER_CONVERSATION = """ [
{ "role": "user", "content": "hello" },
  {
    "role": "assistant",
    "content": "Hello! I'm excited to discuss your website project with you. Can you please tell me the name of the website or the business you want the website for? Additionally, do you have any information about the website that you'd like to share, such as its purpose, target audience, or any specific features you'd like to include?"
  },
  {
    "role": "user",
    "content": "i am the founder of a phramacuetical company named bkf pharma, we are developing a propreitary medicine for cancer treatment. the research isnt comlete yet so details cant be shared, but i want to have a website that i can show to potential partners and investors, i dont have any branding etc set so u are free to design as you want, i am a little short on time, so try not to ask me a lot of stuff and u can give me options and ill say yes or no"
  },
  {
    "role": "assistant",
    "content": "Thank you for sharing that with me. It sounds like you're looking to create a website that will serve as a professional presence for BKF Pharma, showcasing your company's mission and vision to potential partners and investors.\n\nGiven the sensitive nature of your research, I completely understand that you can't share too many details at this point. Let's focus on creating a website that conveys your company's values and goals.\n\nFor the design, I'll suggest a few options, and you can give me a thumbs up or down. Sound good?\n\nHere's a question to get started: Would you prefer a website with a more modern, sleek design or a more traditional, professional look?"
  },
  { "role": "user", "content": "modern, sleek design," },
  {
    "role": "assistant",
    "content": "A modern, sleek design will give your website a fresh and innovative feel, which is perfect for a pharmaceutical company like BKF Pharma that's pushing the boundaries of cancer treatment.\n\nNext question: What kind of imagery would you like to feature on your website? For example, would you like to see:\n\nA) Abstract, futuristic visuals that evoke a sense of innovation and cutting-edge technology\nB) Images of people, such as scientists, researchers, or patients, to add a human touch\nC) Minimalist, clean designs that focus on typography and simple graphics\n\nLet me know your preference, and I'll take it from there!"
  },
  { "role": "user", "content": "a and some b" },
  {
    "role": "assistant",
    "content": "You'd like to combine the futuristic, high-tech feel of abstract visuals with some human elements to add a touch of warmth and empathy. This will help convey the innovative spirit of BKF Pharma while also highlighting the human impact of your work.\n\nNext question: What's the primary action you'd like visitors to take when they land on your website? For example, would you like them to:\n\nA) Learn more about BKF Pharma's mission and values\nB) Get in touch with you or your team for potential partnerships or investments\nC) Stay updated on the latest news and developments from BKF Pharma\n\nLet me know your top priority, and I'll make sure to design a website that guides visitors towards that goal!"
  },
  { "role": "user", "content": "a with a contact page for b" },
  {
    "role": "assistant",
    "content": "You'd like the website to primarily focus on showcasing BKF Pharma's mission and values, with a clear call-to-action to encourage visitors to learn more about your company's vision and goals.\n\nAdditionally, you'd like to include a dedicated contact page that makes it easy for potential partners, investors, or other interested parties to get in touch with you or your team.\n\nNext question: What kind of tone would you like to convey through your website's content and design? For example, would you like it to be:\n\nA) Professional and authoritative, conveying a sense of expertise and credibility\nB) Inspirational and motivational, highlighting the potential impact of your work\nC) Friendly and approachable, conveying a sense of collaboration and openness\n\nLet me know your preference, and I'll help create a website that resonates with your target audience!"
  },
  { "role": "user", "content": "b" },
  {
    "role": "assistant",
    "content": "You'd like the tone of your website to be inspirational and motivational, highlighting the potential impact of BKF Pharma's work on cancer treatment. This will help create an emotional connection with your visitors and inspire them to learn more about your mission.\n\nI think I have a good understanding of your vision now. Before I wrap up, is there anything else you'd like to add or any specific concerns you have about the website?\n\nIf not, I'll summarize the key points we've discussed and get started on designing a website that meets your needs.\n\n(Type \"Exit\" if you're ready to conclude our conversation)"
  },
  { "role": "user", "content": "nothing else" }
]"""


# Function to check if all required files exist
def check_files_exist(files):
    return all(os.path.exists(file) for file in files)


# Function to create directories if not exist
def create_directories(paths):
    for path in paths:
        os.makedirs(path, exist_ok=True)


# Function to run tasks asynchronously
def run_tasks_in_parallel(tasks):
    results = []
    with ThreadPoolExecutor() as executor:
        future_tasks = {executor.submit(task): task for task in tasks}
        for future in as_completed(future_tasks):
            task = future_tasks[future]
            try:
                logging.info(f"Task {task} started")
                results.append(future.result())
                logging.info(f"Task {task} finished")
            except Exception as exc:
                logging.error(f"Task {task} generated an exception: {exc}")

    logging.info("All tasks completed")
    return results


# Define Crews
def define_user_requirements_crew():

    # Load the configuration files
    with open(CONFIG["agents_config"], "r") as stream:
        agents_config = yaml.safe_load(stream)
    with open(CONFIG["tasks_config"], "r") as stream:
        tasks_config = yaml.safe_load(stream)

    # Define the agents
    user_requirements_agent = Agent(
        config=agents_config["user_requirements_agent"],
        verbose=True,
        llm=azure_gpt4o,
        max_iter=4,
        allow_delegation=False,
    )
    design_brief_agent = Agent(
        config=agents_config["design_brief_agent"],
        verbose=True,
        llm=azure_gpt4o,
        max_iter=4,
        allow_delegation=False,
    )
    website_structure_agent = Agent(
        config=agents_config["website_structure_agent"],
        verbose=True,
        llm=azure_gpt4o,
        max_iter=4,
        allow_delegation=False,
    )

    # Define the tasks
    generate_user_requirements = Task(
        config=tasks_config["generate_user_requirements"],
        verbose=True,
        agent=user_requirements_agent,
        output_file=f"{CONFIG['project_name']}/user_requirements.md",
        async_execution=False,
    )
    generate_website_design_brief = Task(
        config=tasks_config["generate_website_design_brief"],
        verbose=True,
        agent=design_brief_agent,
        async_execution=False,
        output_file=f"{CONFIG['project_name']}/website_design_brief.md",
        context={generate_user_requirements},
    )
    generate_website_structure = Task(
        config=tasks_config["generate_website_structure"],
        verbose=True,
        agent=website_structure_agent,
        async_execution=False,
        output_file=f"{CONFIG['project_name']}/website_structure.json",
        context={
            generate_website_design_brief,
            generate_user_requirements,
        },
    )

    # Define the crew
    user_requirements_crew = Crew(
        agents=[
            user_requirements_agent,
            design_brief_agent,
            website_structure_agent,
        ],
        tasks=[
            generate_user_requirements,
            generate_website_design_brief,
            generate_website_structure,
        ],
        process=Process.sequential,
        verbose=2,
        max_rpm=20,
        # memory=True,
        # embedder={
        #     "provider": "azure_openai",
        #     "config": {
        #         "model": "text-embedding-ada-002",
        #         "deployment_name": "text-ada-bilal",
        #     },
        # },
    )

    # Kickoff the crew
    return user_requirements_crew

    # return UserRequirementsCrew().crew()


def define_section_design_crew(page_name, section_name):
    @CrewBase
    class SectionDesignCrew:
        agents_config = CONFIG["agents2_config"]
        tasks_config = CONFIG["tasks2_config"]

        def __init__(self, page_name, section_name) -> None:
            self.page_name = page_name
            self.section_name = section_name

        @agent
        def section_design_brief_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["section_design_brief_agent"],
                verbose=True,
                llm=azure_gpt4o,
                max_iter=4,
                allow_delegation=False,
            )

        @agent
        def section_content_curator_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["section_content_curator_agent"],
                verbose=True,
                llm=azure_gpt4o,
                max_iter=4,
                allow_delegation=False,
            )

        @agent
        def image_generation_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["image_generation_agent"],
                verbose=True,
                llm=azure_gpt4o,
                max_iter=4,
                allow_delegation=False,
            )

        @task
        def generate_section_design_brief(self) -> Task:
            return Task(
                config=self.tasks_config["generate_section_design_brief"],
                verbose=True,
                agent=self.section_design_brief_agent(),
                output_file=f"{CONFIG['project_name']}/{self.page_name}/{self.section_name}/design_brief.md",
                async_execution=False,
            )

        @task
        def generate_section_content(self) -> Task:
            return Task(
                config=self.tasks_config["generate_section_content"],
                verbose=True,
                agent=self.section_content_curator_agent(),
                output_file=f"{CONFIG['project_name']}/{self.page_name}/{self.section_name}/text_content.md",
                async_execution=False,
                context={self.generate_section_design_brief()},
            )

        @task
        def generate_section_images(self) -> Task:
            return Task(
                config=self.tasks_config["generate_section_images"],
                verbose=True,
                agent=self.image_generation_agent(),
                output_file=f"{CONFIG['project_name']}/{self.page_name}/{self.section_name}/image_urls.md",
                async_execution=False,
                tools=[dalle_tool],
                context={self.generate_section_design_brief()},
            )

        @crew
        def crew(self) -> Crew:
            return Crew(
                agents=[
                    self.section_design_brief_agent(),
                    self.section_content_curator_agent(),
                    self.image_generation_agent(),
                ],
                tasks=[
                    self.generate_section_design_brief(),
                    self.generate_section_content(),
                    self.generate_section_images(),
                ],
                process=Process.sequential,
                verbose=2,
                max_rpm=20,
                # memory=True,
                # embedder={
                #     "provider": "azure_openai",
                #     "config": {
                #         "model": "text-embedding-ada-002",
                #         "deployment_name": CONFIG["embeddings_azure_deployment"],
                #     },
                # },
            )

    return SectionDesignCrew(page_name=page_name, section_name=section_name).crew()


def coding_crew():

    # agentops.init(tags="coding_crew", api_key="794cc782-0211-4096-a9fb-eafaffd3655f")

    # Manager Agent
    manager = Agent(
        role="Project Manager",
        goal="Oversee the website code generation process and that the final code represents a beautiful website, as per the user requirements. You are also given the website structure, to help with nav bar links and footer area links etc. Make sure that the website is fully functional and very nicely made, following the latest design trends and industry standards.",
        verbose=True,
        llm=azure_gpt4o,
        backstory="You are the project manager ensuring all tasks are completed efficiently and to a high standard.",
        allow_delegation=True,
    )

    # Layout Agent
    layout_agent = Agent(
        role="Layout Designer",
        goal="Generate HTML structure for website sections.",
        verbose=True,
        llm=azure_gpt4o,
        backstory="You are responsible for creating the HTML layout based on the design brief and user requirements.",
    )

    # Styling Agent
    styling_agent = Agent(
        role="Styling Designer",
        goal="Generate CSS for website sections.",
        verbose=True,
        llm=azure_gpt4o,
        backstory="You ensure the website is visually appealing and consistent by creating the necessary CSS.",
    )

    # Animation Agent
    animation_agent = Agent(
        role="Animation Designer",
        goal="Add JavaScript animations and interactivity to the website.",
        verbose=True,
        llm=azure_gpt4o,
        backstory="You enhance the user experience by adding engaging animations and interactivity with JavaScript.",
    )

    # Layout Task
    layout_task = Task(
        description="Generate HTML for each website section based on the design brief and user requirements.",
        expected_output="HTML structure for each section.",
        agent=layout_agent,
    )

    # Styling Task
    styling_task = Task(
        description="Generate CSS for each website section to ensure consistent styling.",
        expected_output="CSS for each section.",
        agent=styling_agent,
    )

    # Animation Task
    animation_task = Task(
        description="Generate JavaScript for animations and interactivity for each website section.",
        expected_output="JavaScript for each section.",
        agent=animation_agent,
    )

    # Integration Task
    integration_task = Task(
        description="""
        Integrate the HTML, CSS, and JavaScript into final web pages. As the manager, your job is to understand the user requirements and website structure and get the full code of the website generated, you are expected to use the HTML css and JS agents to write the code for the website. You are also incharge of saving the finalised website files in the correct directories. The final set of files should be saved in the Final_files directory of the project. The expectation is that each page in the website would have an html file, using inline css and js.
        
        User Requiremnts:
        
        {user_requirements}
        
        
        Website Design Brief
        
        {website_design_brief}
        
        
        Website structure:
        
        {website_structure}
        
        
        Design Brief, Text Content, and Image Paths, for each section of each page of the website:
        
        {pages_briefs}
        
        
        
        """,
        expected_output="Complete and optimized HTML files with inline CSS and JS. You are supposed to use the file writer tool to write the code to the files.",
        tools=[file_writer_tool],
        agent=manager,  # Manager oversees this task
    )

    website_code_crew = Crew(
        agents=[layout_agent, styling_agent, animation_agent],
        tasks=[integration_task, layout_task, styling_task, animation_task],
        process=Process.hierarchical,
        manager_agent=manager,
    )

    # Assuming `sections` contains the section briefs and other necessary information
    return website_code_crew


# Main workflow
def run():
    overall_start_time = time.time()
    # inputs = {
    #     "user_conversation": USER_CONVERSATION,
    #     "example_website_structure": """{
    #   "sitename": "My Website",
    #   "pages": [
    #     {
    #       "name": "<page name>",
    #       "sections": [
    #         {
    #           "name": "<section name>"
    #           "description": "<brief section description>"
    #         },
    #         <more sections>
    #       ]
    #     },
    #     {
    #       "name": "<page name>",
    #       "sections": [
    #        {
    #           "name": "<section name>"
    #           "description": "<brief section description>"
    #         },
    #         <more sections>
    #       ]
    #     }
    #   ]
    #   //any other pages and sections as needed by the user requirements.
    # }""",
    # }

    # create_directories([CONFIG["project_name"]])

    # # Run User Requirements Crew
    # if not check_files_exist(
    #     [
    #         f"{CONFIG['project_name']}/website_structure.json",
    #         f"{CONFIG['project_name']}/user_requirements.md",
    #         f"{CONFIG['project_name']}/website_design_brief.md",
    #     ]
    # ):
    #     crew1 = define_user_requirements_crew()
    #     crew1.kickoff(inputs)
    # else:
    #     logging.info("Required files already exist, skipping user requirements crew")

    # Read generated files
    with open(f"{CONFIG['project_name']}/website_structure.json", "r") as file:
        website_structure = json.load(file)

    with open(f"{CONFIG['project_name']}/user_requirements.md", "r") as file:
        user_requirements = file.read()

    with open(f"{CONFIG['project_name']}/website_design_brief.md", "r") as file:
        website_design_brief = file.read()

    # # Run Section Design Crews
    # tasks = []
    # for page in website_structure["pages"]:
    #     page_name = page["name"]
    #     for section in page["sections"]:
    #         section_name = section["name"]
    #         create_directories([f"{CONFIG['project_name']}/{page_name}/{section_name}"])

    #         if not check_files_exist(
    #             [
    #                 f"{CONFIG['project_name']}/{page_name}/{section_name}/design_brief.md",
    #                 f"{CONFIG['project_name']}/{page_name}/{section_name}/text_content.md",
    #                 f"{CONFIG['project_name']}/{page_name}/{section_name}/image_urls.md",
    #             ]
    #         ):
    #             task_inputs = {
    #                 "user_requirements": user_requirements,
    #                 "website_design_brief": website_design_brief,
    #                 "website_structure": website_structure,
    #                 "page_name": page_name,
    #                 "section_name": section_name,
    #             }
    #             # tasks.append(
    #             #     lambda: define_section_design_crew(page_name, section_name).kickoff(
    #             #         task_inputs
    #             #     )
    #             # )
    #             tasks.append(
    #                 (
    #                     lambda page_name=page_name, section_name=section_name: define_section_design_crew(
    #                         page_name, section_name
    #                     ).kickoff(
    #                         task_inputs
    #                     )
    #                 )
    #             )
    #         else:
    #             logging.info(
    #                 f"Files already exist for {section_name} section of {page_name} page, skipping section design crew"
    #             )

    # run_tasks_in_parallel(tasks)

    # time_till_crews = time.time() - overall_start_time
    # logging.info(f"Time taken till now(crews completed): {time_till_crews}")

    # # Generate website code
    # for page in website_structure["pages"]:
    #     page_name = page["name"]
    #     for section in page["sections"]:
    #         section_name = section["name"]
    #         section_code_file = (
    #             f"{CONFIG['project_name']}/{page_name}/{section_name}/section_code.md"
    #         )

    #         if os.path.exists(section_code_file):
    #             logging.info(
    #                 f"Section code file already exists for {section_name} section of {page_name} page."
    #             )
    #             continue

    #         start_time = time.time()
    #         section_code_json = generate_section_code(
    #             section_name,
    #             open(
    #                 f"{CONFIG['project_name']}/{page_name}/{section_name}/design_brief.md",
    #                 "r",
    #             ).read(),
    #             open(
    #                 f"{CONFIG['project_name']}/{page_name}/{section_name}/text_content.md",
    #                 "r",
    #             ).read(),
    #             open(
    #                 f"{CONFIG['project_name']}/{page_name}/{section_name}/image_urls.md",
    #                 "r",
    #             ).read(),
    #         )

    #         with open(section_code_file, "w") as f:
    #             f.write(section_code_json)

    #         # end_time = time.time()
    #         # logging.info(
    #         #     f"Time taken for generating code for {section_name} section of {page_name} page: {end_time - start_time}"
    #         # )

    # # time_till_website_code = time.time() - overall_start_time
    # # logging.info(f"Time taken till now(crews completed): {time_till_website_code}")

    # make_page_files(
    #     CONFIG["project_name"],
    #     page_name,
    #     [section["name"] for section in page["sections"]],
    # )
    # shutil.move("images", f"{CONFIG['project_name']}/files")

    # overall_end_time = time.time()
    # logging.info(
    #     f"Time taken for generating website structure, design, content and images: {overall_end_time - overall_start_time}"
    # )

    # return "Website Generated Successfully!"

    pages_brief = []  # Initialize pages_brief

    for page in website_structure["pages"]:
        page_name = page["name"]
        page_brief = []  # Initialize page_brief for each page
        for section in page["sections"]:
            section_name = section["name"]

            files = [
                f"{CONFIG['project_name']}/{page_name}/{section_name}/design_brief.md",
                f"{CONFIG['project_name']}/{page_name}/{section_name}/text_content.md",
                f"{CONFIG['project_name']}/{page_name}/{section_name}/image_urls.md",
            ]

            if check_files_exist(files):
                # Read the contents of the files and append to page_brief
                for file in files:
                    with open(file, "r") as f:
                        page_brief.append(f.read())
            else:
                logging.info(
                    f"Files dont exist for {section_name} section of {page_name} page"
                )
        pages_brief.append(page_brief)  # Append each page_brief to pages_brief

    # Pass pages_brief to the kickoff method of the coding crew
    coding_inputs = {
        "pages_briefs": pages_brief,
        "website_structure": website_structure,
        "user_requirements": user_requirements,
        "website_design_brief": website_design_brief,
    }
    coding_crew().kickoff(coding_inputs)

    overall_end_time = time.time()
    logging.info(
        f"Time taken for generating website code using coding crew: {overall_end_time - overall_start_time}"
    )
