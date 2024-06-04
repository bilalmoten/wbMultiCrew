import os
from crewai import Agent, Task, Crew, Process

# from crewai_tools import FileWriteTool

from langchain_openai import AzureChatOpenAI


# # Configuration
# CONFIG = {
#     "azure_endpoint": "https://answerai-bilal.openai.azure.com/",
#     "api_key": os.getenv("AZURE_OPENAI_API_KEY2"),
#     "azure_deployment": "gpt4o-azure",
#     "api_version": "2024-02-15-preview",
#     "project_name": "test15_coffee",
#     "agents_config": "config/agents.yaml",
#     "tasks_config": "config/tasks.yaml",
#     "agents2_config": "config/agents2.yaml",
#     "tasks2_config": "config/tasks2.yaml",
# }


azure_gpt4o = AzureChatOpenAI(
    azure_endpoint="https://answerai-bilal.openai.azure.com/",
    api_key="523a50ed7a7444468d1ae5a384f032bf",
    azure_deployment="gpt4o-azure",
    api_version="2024-02-15-preview",
)

# Set up environment variables
# os.environ["SERPER_API_KEY"] = "Your Serper.dev API key"
os.environ["OPENAI_API_KEY"] = "Your OpenAI API key"

# Create the SerperDevTool and FileWriteTool instances
# search_tool = SerperDevTool()
# file_write_tool = FileWriteTool()

# Create agents for Crew 1
requirement_analyst = Agent(
    role="Requirement Analyst",
    goal="Understand the user requirements for a website design",
    verbose=True,
    memory=True,
    backstory="You are an expert in gathering and analyzing client requirements.",
    # tools=[search_tool],
    allow_delegation=True,
    llm=azure_gpt4o,
)

designer = Agent(
    role="Designer",
    goal="Generate a hero section design brief based on client requirements",
    verbose=True,
    memory=True,
    backstory="You are a creative designer focused on delivering stunning design briefs.",
    # tools=[search_tool],
    allow_delegation=False,
    llm=azure_gpt4o,
)

# Create tasks for Crew 1
understand_requirements_task = Task(
    description="Understand the user's chat to gather website design requirements.",
    expected_output="A detailed list of website design requirements.",
    # tools=[search_tool],
    agent=requirement_analyst,
)

generate_design_brief_task = Task(
    description="Create a hero section design brief based on the gathered requirements.",
    expected_output="A design brief document for the hero section.",
    # tools=[search_tool],
    agent=designer,
)

# Create Crew 1
crew1 = Crew(
    agents=[requirement_analyst, designer],
    tasks=[understand_requirements_task, generate_design_brief_task],
    process=Process.sequential,
)

# Execute Crew 1 to get the design brief
result_crew1 = crew1.kickoff(
    inputs={
        "user_chat": "I need a modern, sleek hero section for a tech startup website."
    }
)
design_brief = result_crew1["generate_design_brief_task"]["output"]

print("Crew 1 Results:", result_crew1)

# Create agents for Crew 2
html_css_developer = Agent(
    role="HTML/CSS Developer",
    goal="Write the HTML and CSS code for the hero section",
    verbose=True,
    memory=True,
    backstory="You are a skilled developer specializing in front-end technologies.",
    # tools=[file_write_tool],
    allow_delegation=True,
    llm=azure_gpt4o,
)

javascript_developer = Agent(
    role="JavaScript Developer",
    goal="Add JavaScript functionality to the hero section",
    verbose=True,
    memory=True,
    backstory="You are a JavaScript expert focusing on enhancing user interactions.",
    # tools=[file_write_tool],
    allow_delegation=False,
    llm=azure_gpt4o,
)

# Create tasks for Crew 2
create_html_css_task = Task(
    description="Write the HTML and CSS code for the hero section based on the design brief.",
    expected_output="HTML and CSS files for the hero section.",
    output_file="hero_section.html",
    # tools=[file_write_tool],
    agent=html_css_developer,
)

create_javascript_task = Task(
    description="Add JavaScript functionality to the hero section based on the design brief.",
    expected_output="JavaScript file for the hero section.",
    # tools=[file_write_tool],
    output_file="hero_section.js",
    agent=javascript_developer,
)

# Create Crew 2
crew2 = Crew(
    agents=[html_css_developer, javascript_developer],
    tasks=[create_html_css_task, create_javascript_task],
    process=Process.sequential,
)

# Execute Crew 2 with the design brief from Crew 1
result_crew2 = crew2.kickoff(inputs={"design_brief": design_brief})
print("Crew 2 Results:", result_crew2)
