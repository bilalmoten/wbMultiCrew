import os

# import json
# import time

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from langchain_groq import ChatGroq
from langchain_openai import AzureChatOpenAI

from wbmulticrew.tools.file_tools import file_write_tool

from dotenv import load_dotenv

from wbmulticrew.main import namee

load_dotenv()

File_write_tool = file_write_tool()

groq_llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")
azure_gpt4 = AzureChatOpenAI(
    azure_endpoint="https://wbmulticrew.openai.azure.com/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    azure_deployment="gpt4-wbmulticrew",
    api_version="2024-02-15-preview",
)


@CrewBase
class Section_code_crew:
    """Section_code crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def section_code_generation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["section_code_generation_agent"],
            verbose=True,
            llm=groq_llm,
            max_iter=4,
            allow_delegation=False,
        )

    ########### Tasks ###########

    @task
    def generate_page_code(self) -> Task:
        return Task(
            config=self.tasks_config["generate_page_code"],
            verbose=True,
            agent=self.section_code_generation_agent(),
            async_execution=False,
            output_file=f"{namee}/output.txt",
            tools=[File_write_tool],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Section_code crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            # manager_llm=azure_gpt4,
            # process=Process.hierarchical,  # Specifies the hierarchical management approach
            process=Process.sequential,
            verbose=2,
            max_rpm=20,
        )
