import json
import os
import time

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from langchain_groq import ChatGroq

from langchain_openai import AzureChatOpenAI
from wbmulticrew.page_code import generate_section_code
from wbmulticrew.parse_json import make_page_files


from wbmulticrew.tools.dalle_tool import Dalle_Image
import shutil
import os


# groq_llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")

azure_gpt4o = AzureChatOpenAI(
    azure_endpoint="https://answerai-bilal.openai.azure.com/",
    api_key="523a50ed7a7444468d1ae5a384f032bf",
    azure_deployment="gpt4o-azure",
    api_version="2024-02-15-preview",
)

dalle_tool = Dalle_Image()

namee = "test1_222bilal"

user_conversation = """ [
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


def website_reqs(inputs):

    # agentops.init(os.environ["AGENTOPS_API_KEY"])
    # agentops.init()

    @CrewBase
    class user_requirementsCrew:
        """user_requirements crew"""

        agents_config = "config/agents.yaml"
        tasks_config = "config/tasks.yaml"

        # @track_agent(name="user_requirements_agent")
        @agent
        def user_requirements_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["user_requirements_agent"],
                verbose=True,
                llm=azure_gpt4o,
                max_iter=4,
                allow_delegation=False,
            )

        # @track_agent(name="design_brief_agent")
        @agent
        def design_brief_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["design_brief_agent"],
                verbose=True,
                llm=azure_gpt4o,
                max_iter=4,
                allow_delegation=False,
            )

        # @track_agent(name="website_structure_agent")
        @agent
        def website_structure_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["website_structure_agent"],
                verbose=True,
                llm=azure_gpt4o,
                max_iter=4,
                allow_delegation=False,
            )

        ########### Tasks ###########

        @task
        def generate_user_requirements(self) -> Task:
            return Task(
                config=self.tasks_config["generate_user_requirements"],
                verbose=True,
                agent=self.user_requirements_agent(),
                output_file=f"{namee}/user_requirements.md",
                async_execution=False,
            )

        @task
        def generate_website_design_brief(self) -> Task:
            return Task(
                config=self.tasks_config["generate_website_design_brief"],
                verbose=True,
                agent=self.design_brief_agent(),
                async_execution=False,
                output_file=f"{namee}/website_design_brief.md",
                context={self.generate_user_requirements()},
            )

        @task
        def generate_website_structure(self) -> Task:
            return Task(
                config=self.tasks_config["generate_website_structure"],
                verbose=True,
                agent=self.website_structure_agent(),
                async_execution=False,
                output_file=f"{namee}/website_structure.json",
                context={
                    self.generate_website_design_brief(),
                    self.generate_user_requirements(),
                },
            )

        @crew
        def crew(self) -> Crew:
            """Creates the user_requirements crew"""
            return Crew(
                agents=self.agents,
                tasks=[
                    self.generate_user_requirements(),
                    self.generate_website_design_brief(),
                    self.generate_website_structure(),
                ],
                process=Process.sequential,
                verbose=2,
                # memory=True,
                max_rpm=20,
                # embedder={
                #     "provider": "azure_openai",
                #     "config": {
                #         "model": "text-embedding-ada-002",
                #         "deployment_name": "ada-crewai",
                #     },
                # },
            )

    user_requirementsCrew().crew().kickoff(inputs=inputs)


def section_design(inputs, page_name, section_name):

    # agents_config = "config/agents2.yaml"
    # tasks_config = "config/tasks2.yaml"

    section_design_brief_agent = Agent(
        role="section_design_brief_agent",
        # config=agents_config["section_design_brief_agent"],
        goal=" Generate detailed design brief for the {section_name} section of the website",
        backstory="You're an AI agent with a deep understanding of design principles. You use the website structure, and the user requirements to create a well detailed design brief for the {section_name} section of the website. The design brief should include the content and image requirements for the section, as well as details of the design elements, including color schemes, typography, iconography, and user interface components, and th elayout of the section and any micro interactions or hover effects etc. \n the section design brief should include the requirements for images, with description of what image is needed, and the content requirements for the section, so that the image generation agent can use the image description to prompt an AI text to image model like Dall-E 3 to generate the images for the section, and the copywriters can use the content requirements to write the content for the section.",
        verbose=True,
        llm=azure_gpt4o,
        max_iter=4,
        allow_delegation=False,
    )

    section_content_curator_agent = Agent(
        role="Content Requirements AI Agent",
        # config=agents_config["section_content_curator_agent"],
        goal="Generate detailed content requirements for the {section_name} section of the website",
        backstory="You're an AI agent with a knack for understanding and structuring information. You use the section design brief to create the full text content for the {section_name} section of the website based on the user requirements and section design brief. ",
        verbose=True,
        llm=azure_gpt4o,
        max_iter=4,
        allow_delegation=False,
    )

    image_generation_agent = Agent(
        role="Image Generation AI Agent",
        goal="Understand the image requirements for the {section_name} section, using the section design brief and user requirements and then use the image generation tool to generate images with dall e 3 using detailed descriptive text prompts. then save the image path that is returned from the tool in your final output. \n If the section doesnt need any image, just return 'No images needed for this section'. and donot try to use the Dalle_image tool.",
        backstory="You're an AI agent with a keen eye for visual details. You use the section design brief and user requirments to create images for the section.",
        verbose=True,
        llm=azure_gpt4o,
        max_iter=4,
        allow_delegation=False,
    )

    ########### Tasks ###########

    generate_section_design_brief_task = Task(
        # config=tasks_config["generate_section_design_brief"],
        description="""Create a design brief for a the {section_name} section of the website, including the section layout, color schemes, typography, iconography, user interface components, and any additional design elements requested by the user. Your design brief should be based upon the user requirements document, and the website design brief and should be enhanced by your own knowledge and your expertise in website design, given your 10 years of experience at worlds best web deisgn agency.
        The Section Design Brief that you are supposed to generate will act as the base for the developers, content writers and image artists to create the section of the website. The design brief should contain all the necessary information, design elements, background details, interactions, and animations for that section.
        the section design brief should include the requirements for images, with description of what image is needed, and the content requirements for the section, so that the image generation agent can use the image description to prompt an AI text to image model like Dall-E 3 to generate the images for the section, and the copywriters can use the content requirements to write the content for the section.

        User Requirements:
        {user_requirements}

        Website Design Brief:
        {website_design_brief}""",
        expected_output="""A markdown file containing the design brief, with detailed information on the design elements, interactions, and animations, for the {section_name} section of the website, along with the image and content requirement so that the content writers can write the content for the section, and the image agent can generate the images""",
        verbose=True,
        agent=section_design_brief_agent,
        output_file=f"{namee}/{page_name}/{section_name}/design_brief.md",
        async_execution=False,
    )

    generate_section_content_task = Task(
        # # config=tasks_config["generate_section_content"],
        description="""Generate high-quality text content for the {section_name} section of the website, including page copy, button labels, headlines, sub headlines, blog posts, product descriptions, and any other text that would be needed for the section, as per the section design brief, tailored to the website's purpose and target audience. 
    
        user Requirements:
        {user_requirements}""",
        expected_output="""A markdown file containing the text content for the {section_name} section of the website. The content should be engaging, informative, and aligned with the website's goals and target audience.""",
        verbose=True,
        agent=section_content_curator_agent,
        output_file=f"{namee}/{page_name}/{section_name}/text_content.md",
        async_execution=False,
        context={generate_section_design_brief_task},
    )

    generate_section_images_task = Task(
        # # config=tasks_config["generate_section_images"],
        description="""Generate high-quality images based on text prompts for the {section_name} section of the website, using the DALL-E 3 model. The images should be visually appealing, relevant to the content, and consistent with the branding guidelines.
        You must use the Dalle_Image tool to generate the image paths by providing the text prompts for the images, one by one, as per the design brief.
        the tool takes in a text prompt and uses it to generate the image using an AI text to image model like dalle 3, and then provides the image path for the generated image.
        Remember to only use the tool once for one image, and then give the image paths in your final output.
        If the section doesnt need any image, just return "No images needed for this section". and donot try to use the Dalle_image tool.""",
        expected_output=""" A json file containing the image paths and text prompts returned from using the Dalle_Image tool for the {section_name} section of the website. If no images are needed for the section, return "No images needed for this section".""",
        verbose=True,
        agent=image_generation_agent,
        output_file=f"{namee}/{page_name}/{section_name}/image_urls.md",
        async_execution=False,
        tools=[dalle_tool],
        context={generate_section_design_brief_task},
    )

    sd_crew = Crew(
        page_name=page_name,
        section_name=section_name,
        agents=[
            section_design_brief_agent,
            section_content_curator_agent,
            image_generation_agent,
        ],
        tasks=[
            generate_section_design_brief_task,
            generate_section_content_task,
            generate_section_images_task,
        ],
        process=Process.sequential,
        verbose=2,
        max_rpm=20,
    )

    # Section_design_Crew(page_name=page_name, section_name=section_name).crew().kickoff(
    #     inputs=inputs
    # )
    sd_crew.kickoff(inputs=inputs)


def website_code():
    website_structure = open(f"{namee}/website_structure.json", "r").read()
    website_structure = json.loads(website_structure)

    for page in website_structure["pages"]:
        page_name = page["name"]
        for section in page["sections"]:
            section_name = section["name"]
            section_code_file = f"{namee}/{page_name}/{section_name}/section_code.md"

            if os.path.exists(section_code_file):
                print(
                    f"Section code file already exists for {section_name} section of {page_name} page."
                )
                continue

            start_time = time.time()
            section_code_json = generate_section_code(
                section_name,
                open(f"{namee}/{page_name}/{section_name}/design_brief.md", "r").read(),
                open(f"{namee}/{page_name}/{section_name}/text_content.md", "r").read(),
                open(f"{namee}/{page_name}/{section_name}/image_urls.md", "r").read(),
            )

            with open(section_code_file, "w") as f:
                f.write(section_code_json)
            end_time1 = time.time()
            print(
                f"Time taken for generating code for {section_name} section of {page_name} page of the website : {end_time1 - start_time}"
            )
        make_page_files(
            namee, page_name, [section["name"] for section in page["sections"]]
        )


def main():
    overall_start_time = time.time()

    inputs = {
        "user_conversation": user_conversation,
        "example_website_structure": """{
      "sitename": "My Website",
      "pages": [
        {
          "name": "<page name>",
          "sections": [
            {
              "name": "<section name>"
              "description": "<brief section description>"
            },
            <more sections>
          ]
        },
        {
          "name": "<page name>",
          "sections": [
           {
              "name": "<section name>"
              "description": "<brief section description>"
            },
            <more sections>
          ]
        }
      ]
      //any other pages and sections as needed by the user requirements.
    }""",
    }

    start_time = time.time()

    os.makedirs(namee, exist_ok=True)
    if (
        not os.path.exists(f"{namee}/website_structure.json")
        or not os.path.exists(f"{namee}/user_requirements.md")
        or not os.path.exists(f"{namee}/website_design_brief.md")
    ):
        website_reqs(inputs)
    else:
        print(
            "Required files already exist already exist, skipping user requirements crew"
        )
    end_time1 = time.time()
    print(
        f"Time taken for generating user requirements and website structure: {end_time1 - start_time}"
    )

    website_structure = open(f"{namee}/website_structure.json", "r").read()

    user_requirements = open(f"{namee}/user_requirements.md", "r").read()
    website_design_brief = open(f"{namee}/website_design_brief.md", "r").read()

    website_structure = json.loads(website_structure)
    for page in website_structure["pages"]:
        page_name = page["name"]
        for section in page["sections"]:
            section_name = section["name"]
            start_time = time.time()

            os.makedirs(f"{namee}/{page_name}/{section_name}", exist_ok=True)
            inputs = {
                "user_requirements": user_requirements,
                "website_design_brief": website_design_brief,
                "website_structure": website_structure,
                "page_name": page_name,
                "section_name": section_name,
            }
            if (
                not os.path.exists(
                    f"{namee}/{page_name}/{section_name}/design_brief.md"
                )
                or not os.path.exists(
                    f"{namee}/{page_name}/{section_name}/text_content.md"
                )
                or not os.path.exists(
                    f"{namee}/{page_name}/{section_name}/image_urls.md"
                )
            ):
                section_design(inputs, page_name, section_name)
            else:
                print(
                    f"Required files already exist for {section_name} section of {page_name} page, skipping section design crew"
                )
            end_time1 = time.time()
            print(
                f"Time taken for creating design, content and images for {section_name} section of {page_name} page of the website : {end_time1 - start_time}"
            )

    website_code()
    shutil.move("images", f"{namee}/files")
    overall_end_time = time.time()
    print(
        f"Time taken for generating website structure, design, content and images: {overall_end_time - overall_start_time}"
    )
    return "Website Generated Successfully!"


if __name__ == "__main__":
    main()
