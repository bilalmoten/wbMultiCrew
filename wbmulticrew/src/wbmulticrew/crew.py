import os
import json
import time

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from langchain_groq import ChatGroq
from langchain_openai import AzureChatOpenAI

# from wbmulticrew.tools.file_tools import FileTools
# from wbmulticrew.tools.image_generation_tools import Image_generation_tools
from wbmulticrew.tools.dalle_tool import Dalle_Image

from langchain_community.agent_toolkits import FileManagementToolkit

from dotenv import load_dotenv

from wbmulticrew.main import namee, user_conversation

load_dotenv()

dalle_tool = Dalle_Image()

toolkit = FileManagementToolkit(
    root_dir="workdir", selected_tools=["read_file", "list_directory"]
)

groq_llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")
# self.llm = ollama_mixtral
azure_gpt4 = AzureChatOpenAI(
    azure_endpoint="https://wbmulticrew.openai.azure.com/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    azure_deployment="gpt4-wbmulticrew",
    api_version="2024-02-15-preview",
)


@CrewBase
class user_requirementsCrew:
    """user_requirements crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def user_requirements_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["user_requirements_agent"],
            verbose=True,
            llm=groq_llm,
            max_iter=4,
            allow_delegation=False,
        )

    @agent
    def design_brief_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["design_brief_agent"],
            verbose=True,
            llm=groq_llm,
            max_iter=4,
            allow_delegation=False,
        )

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
            # user_requirements=self.generate_user_requirements().output,
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
            # output_json=True,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the user_requirements crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            # manager_llm=azure_gpt4,
            # process=Process.hierarchical,  # Specifies the hierarchical management approach
            process=Process.sequential,
            verbose=2,
            max_rpm=20,
        )


@CrewBase
class Section_design_Crew:
    """Section Design Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self, page_name, section_name) -> None:
        self.page_name = page_name
        self.section_name = section_name

    @agent
    def section_design_brief_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["section_design_brief_agent"],
            verbose=True,
            llm=groq_llm,
            max_iter=4,
            allow_delegation=False,
        )

    @agent
    def section_content_curator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["section_content_curator_agent"],
            verbose=True,
            llm=groq_llm,
            max_iter=4,
            allow_delegation=False,
        )

    @agent
    def image_generation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["image_generation_agent"],
            verbose=True,
            llm=groq_llm,
            max_iter=4,
            allow_delegation=False,
            # tools=[dalle_tool],
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
            agents=self.agents,
            tasks=self.tasks,
            # manager_llm=azure_gpt4,
            # process=Process.hierarchical,
            process=Process.sequential,
            verbose=2,
            max_rpm=20,
        )
