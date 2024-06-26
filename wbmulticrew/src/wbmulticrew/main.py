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
from wbmulticrew.page_code import generate_section_code, call_gpt4o
from wbmulticrew.parse_json import make_page_files

from wbmulticrew.tools.dalle_tool import Dalle_Image
import yaml


import os
import shutil


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


def parse_markdown(markdown):
    sections = markdown.split("## ")[1:]  # Split the markdown into sections
    file_contents = []
    for section in sections:
        lines = section.split("\n")
        filename = lines[0].strip()  # The filename is the first line of the section
        print("filename is: ", filename)
        code_block = "\n".join(lines[1:])  # The rest of the section is the code block
        if "```html" in code_block:
            code_lines = code_block.split("```html")[1].split(
                "\n"
            )  # Extract the code lines
            file_content = "\n".join(
                code_lines[1:]
            ).strip()  # Join the code lines into a single string
            file_contents.append((filename, file_content))
    return file_contents


def generate_code_files(markdown, project_name):
    file_contents = parse_markdown(markdown)
    for filename, content in file_contents:
        filepath = f"{project_name}/final_code_files/{filename}"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as file:
            file.write(content)
    shutil.move("src/wbmulticrew/images", f"{project_name}/final_code_files")


def generate_full_website(
    project_name, website_structure, user_requirements, website_design_brief
):

    logging.info("Generating Full Website1")

    # Generate section codes for the website
    all_section_codes = []
    all_image_paths = []
    for page in website_structure["pages"]:
        page_name = page["name"]
        for section in page["sections"]:
            section_name = section["name"]
            section_code_file = (
                f"{project_name}/{page_name}/{section_name}/section_code.md"
            )
            image_path_file = f"{project_name}/{page_name}/{section_name}/image_urls.md"
            with open(section_code_file, "r") as file:
                section_code = file.read()
            all_section_codes.append(section_code)
            with open(image_path_file, "r") as file:
                image_paths = file.read()
            all_image_paths.append(image_paths)

    # print(all_image_paths)

    # system_prompt = f"""
    # You are website GPT. You have extensive experience in designing and developing HTML CSS & JS based website
    # You are known for making amazing websites that are visually appealing and user-friendly.
    # your attention to detail is second to none. You have mastered the art of creating websites that are both beautiful and functional.
    # Currently your task is to build a fully functional, responsive, visually apealing, interactive(with animations and hover affects), and user friendly website for {project_name}.

    # Since you are the senior most website developer in the team, the junior developers and designers have been working on this website section by section, and now it's your turn to put everything together and make sure the website is ready to be deployed.

    # Your job includes, understanding the user's requirements, and build the website according to the user's approved website structure. The junior developers have already written code for all the sections on all the pages of the website, your job is to write the full code for the website, by giving HTML codes for each page seperatly, and by using inline CSS and JS. Your job isnt just to put the code together, but to make it actually work well together, from consistant styling, to properly structured html sections, navbar and footer, proper layouts, and responsive design.

    # the section codes, are for your reference only as they have been done by junior developers so they are not the best quality, so use your knowledge and their hard work to create the full website in the best way possible.

    # Make sure to have consistant styling, aesthetic design, proper and consitant nav bar and footer on all pages, and a fully functional and responsive website. You are one of the best website developers in the world's top most website development agency, so make sure to show your skills in this project.

    # Your Job depends on this website passing the clients approval, so make sure to make it as good as possible.

    # Remember to use proper constraints for the images, as all images are originally 1024 by 1024 pixels, and u need to use them according to the requirements of the design of the website.

    # Also Remember, the websites are supposed to use, tailwind css mainly,  and fontawesome for icons. so you should write the code accordingly to benefit from these, and also use the following links and scripts to add these libraries to the webspage,

    # <script src="https://cdn.tailwindcss.com"></script>
    # <script src="https://kit.fontawesome.com/037776171a.js" crossorigin="anonymous"></script>

    # Expected Output: A markdown format with just the HTML code, nothing else.

    # Example Output:
    # Do Not add any Placeholders, comments, backticks (```) or any other text in your response

    # Only Respond with a Properly Formatted MARKDOWN with the HTML code for each HTML file(each page) of the website.

    # Write

    # ## All Files Completed

    # at the end of the markdown file, after all the HTML code for each page.

    # the markdown should include each codeblock seperatly with language specified as HTML, and heading as name of the file, and a final heading of code completed.

    # such as

    # ## index.html
    # ```html
    # <html code here>
    # ```

    # ## about_us.html
    # ```html
    # <html code here>
    # ```

    # ## contact_us.html
    # ```html
    # <html code here>
    # ```

    # ## All Files Completed

    # NOTHING ELSE.
    # """

    system_prompt = f"""
    You are website GPT. You have extensive experience in designing and developing HTML CSS & JS based website
    You are known for making amazing websites that are visually appealing and user-friendly.
    your attention to detail is second to none. You have mastered the art of creating websites that are both beautiful and functional.
    Currently your task is to build a fully functional, responsive, visually apealing, interactive(with animations and hover affects), and user friendly website for {project_name}.
    
    
    Your job includes, understanding the user's requirements, and build the website according to the user's approved website structure. You job is to make sur ethe website is the best work of yours to date, from consistant styling, to properly structured html sections, navbar and footer, proper layouts, and responsive design.
    
    Make sure to have consistant styling, aesthetic design, proper and consistant navingation bar and footer on all pages, and a fully functional and responsive website. You are one of the best website developers in the world's top most website development agency, so make sure to show your skills in this project.
    
    Your Job depends on this website passing the clients approval, so make sure to make it as good as possible.
    
    In some cases, the client has also provided some referneces, for which u will be given the code, so try to use that code as a reference for the clients website, not to copy from it, or to make a replica, but for inspiration of the design that the client has already pointed to as something he likes.
    
    Remember to use proper constraints for the images, as all images are originally 1024 by 1024 pixels, and u need to use them according to the requirements of the design of the website.
    
    Also Remember, the websites are supposed to use, tailwind css mainly,  and fontawesome for icons. so you should write the code accordingly to benefit from these, and also use the following scripts to add these libraries to the webspage, 
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://kit.fontawesome.com/037776171a.js" crossorigin="anonymous"></script>
   
    
    Expected Output: A markdown format with just the HTML code, nothing else.
    
    Example Output:
    Do Not add any Placeholders, comments, backticks (```) or any other text in your response

    Only Respond with a Properly Formatted MARKDOWN with the HTML code for each HTML file(each page) of the website.

    Write 
    
    ## All Files Completed 
    
    at the end of the markdown file, after all the HTML code for each page.

    the markdown should include each codeblock seperatly with language specified as HTML, and heading as name of the file, and a final heading of code completed.
    

    such as

    ## index.html
    ```html
    <html code here>
    ```
    
    ## about_us.html
    ```html
    <html code here>
    ```
    
    ## contact_us.html
    ```html
    <html code here>
    ```
    
    ## All Files Completed

    NOTHING ELSE. 
    """

    user_prompt = f"""
    
    User Requirements for the website:
    
    {user_requirements} 
    
    Website Design Brief:
    {website_design_brief}  
    
    Website Structure:
    {website_structure}
    
    AI generated Images to use in this website:
    {all_image_paths} 
    
    """
    extra = f"""section codes for the website, by junior developers:
    {all_section_codes}"""
    assistant_messages = []
    final_response = ""

    while True:
        print("Calling GPT4o")
        response = call_gpt4o(system_prompt, user_prompt, assistant_messages)

        # Add the response to the final response
        final_response += response + "\n"

        # If the response ends with "## All Files Completed", break the loop
        if response.strip().endswith("## All Files Completed"):
            break

        # Otherwise, add the response to the assistant_messages and try again
        assistant_messages.append(response)

    # Save the final response to a file
    print("Saving response to file")
    with open("website_code1response.md", "w") as file:
        file.write(final_response)

    # Call the function with the markdown response
    print("Generating code files from gpt4o response")
    logging.info("Generating code files from gpt4o response")
    generate_code_files(final_response, project_name)

    return "Website Generated Successfully!"


def section_code_generator(page_name, section_name, section_code_file):
    start_time = time.time()
    section_code_json = generate_section_code(
        section_name,
        open(
            f"{CONFIG['project_name']}/{page_name}/{section_name}/design_brief.md",
            "r",
        ).read(),
        open(
            f"{CONFIG['project_name']}/{page_name}/{section_name}/text_content.md",
            "r",
        ).read(),
        open(
            f"{CONFIG['project_name']}/{page_name}/{section_name}/image_urls.md",
            "r",
        ).read(),
    )

    with open(section_code_file, "w") as f:
        f.write(section_code_json)


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

    # section_code_tasks = []
    # # Generate section codes
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

    #         section_code_tasks.append(
    #             (
    #                 lambda page_name=page_name, section_name=section_name, section_code_file=section_code_file,: section_code_generator(
    #                     page_name, section_name, section_code_file
    #                 )
    #             )
    #         )

    # run_tasks_in_parallel(section_code_tasks)
    print("Generating Full Website")
    generate_full_website(
        CONFIG["project_name"],
        website_structure,
        user_requirements,
        website_design_brief,
    )

    overall_end_time = time.time()
    print(
        f"Time taken for generating website structure, design, content and images: {overall_end_time - overall_start_time}"
    )

    return "Website Generated Successfully!"


## testing markdown parsing
# # print current directory
# print(os.getcwd())
# # load mark down file named website_code1response.md
# with open("website_code1response.md", "r") as file:
#     response = file.read()
# # use parse markdown function
# generate_code_files(response, project_name="hello")
