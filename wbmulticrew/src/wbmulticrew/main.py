import json
import os
import time

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from langchain_groq import ChatGroq

import agentops

# from agentops import track_agent

from wbmulticrew.page_code import generate_section_code
from wbmulticrew.parse_json import make_page_files


from wbmulticrew.tools.dalle_tool import Dalle_Image


groq_llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")

dalle_tool = Dalle_Image()

namee = "test9 pharma"

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
]
"""


def website_reqs(inputs):

    # agentops.init(os.environ["AGENTOPS_API_KEY"])

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
                llm=groq_llm,
                max_iter=4,
                allow_delegation=False,
            )

        # @track_agent(name="design_brief_agent")
        @agent
        def design_brief_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["design_brief_agent"],
                verbose=True,
                llm=groq_llm,
                max_iter=4,
                allow_delegation=False,
            )

        # @track_agent(name="website_structure_agent")
        @agent
        def website_structure_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["website_structure_agent"],
                verbose=True,
                llm=groq_llm,
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
                max_rpm=20,
            )

    user_requirementsCrew().crew().kickoff(inputs=inputs)
    agentops.end_session("Success")


def section_design(inputs, page_name, section_name):

    # agentops.init(os.environ["AGENTOPS_API_KEY"])

    @CrewBase
    class Section_design_Crew:
        """Section Design Crew"""

        agents_config = "config/agents2.yaml"
        tasks_config = "config/tasks2.yaml"

        def __init__(self, page_name, section_name) -> None:
            self.page_name = page_name
            self.section_name = section_name

        # @track_agent(name="section_design_brief_agent")
        @agent
        def section_design_brief_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["section_design_brief_agent"],
                verbose=True,
                llm=groq_llm,
                max_iter=4,
                allow_delegation=False,
            )

        # @track_agent(name="section_content_curator_agent")
        @agent
        def section_content_curator_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["section_content_curator_agent"],
                verbose=True,
                llm=groq_llm,
                max_iter=4,
                allow_delegation=False,
            )

        # @track_agent(name="image_generation_agent")
        @agent
        def image_generation_agent(self) -> Agent:
            return Agent(
                config=self.agents_config["image_generation_agent"],
                verbose=True,
                llm=groq_llm,
                max_iter=4,
                allow_delegation=False,
            )

        ########### Tasks ###########

        @task
        def generate_section_design_brief(self) -> Task:
            return Task(
                config=self.tasks_config["generate_section_design_brief"],
                verbose=True,
                agent=self.section_design_brief_agent(),
                output_file=f"{namee}/{self.page_name}/{self.section_name}/design_brief.md",
                async_execution=False,
            )

        @task
        def generate_section_content(self) -> Task:
            return Task(
                config=self.tasks_config["generate_section_content"],
                verbose=True,
                agent=self.section_content_curator_agent(),
                output_file=f"{namee}/{self.page_name}/{self.section_name}/text_content.md",
                async_execution=False,
                context={self.generate_section_design_brief()},
            )

        @task
        def generate_section_images(self) -> Task:
            return Task(
                config=self.tasks_config["generate_section_images"],
                verbose=True,
                agent=self.image_generation_agent(),
                output_file=f"{namee}/{self.page_name}/{self.section_name}/image_urls.md",
                async_execution=False,
                tools=[dalle_tool],
                context={self.generate_section_design_brief()},
            )

        @crew
        def crew(self) -> Crew:
            """Creates the Section Design Crew"""
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
            )

    Section_design_Crew(page_name=page_name, section_name=section_name).crew().kickoff(
        inputs=inputs
    )
    agentops.end_session("Success")


def website_code():
    website_structure = open(f"{namee}/website_structure.json", "r").read()
    website_structure = json.loads(website_structure)

    for page in website_structure["pages"]:
        page_name = page["name"]
        for section in page["sections"]:
            section_name = section["name"]
            start_time = time.time()
            section_code_json = generate_section_code(
                section_name,
                open(f"{namee}/{page_name}/{section_name}/design_brief.md", "r").read(),
                open(f"{namee}/{page_name}/{section_name}/text_content.md", "r").read(),
                open(f"{namee}/{page_name}/{section_name}/image_urls.md", "r").read(),
            )

            with open(f"{namee}/{page_name}/{section_name}/section_code.md", "w") as f:
                f.write(section_code_json)
            end_time1 = time.time()
            print(
                f"Time taken for generating code for {section_name} section of {page_name} page of the website : {end_time1 - start_time}"
            )
        make_page_files(
            namee, page_name, [section["name"] for section in page["sections"]]
        )


def run():
    agentops.init(os.environ["AGENTOPS_API_KEY"])
    inputs = {
        "user_conversation": user_conversation,
        "example_website_structure": """{
      "sitename": "My Website",
      "pages": [
        {
          "name": "Home",
          "sections": [
            {
              "name": "Hero"
            },
            {
              "name": "About Us"
            },
            {
              "name": "Features"
            },
            {
              "name": "Testimonials"
            },
            {
              "name": "Contact Us"
            }
          ]
        },
        {
          "name": "About",
          "sections": [
            {
              "name": "Mission"
            },
            {
              "name": "Vision"
            },
            {
              "name": "Values"
            },
            {
              "name": "Team"
            },
            {
              "name": "Contact Us"
            }
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

    return website_code()
