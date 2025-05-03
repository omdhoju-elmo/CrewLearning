from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from course_builder.tools.pdf_reader_tool import extract_pdf_content
from course_builder.tools.create_elearning_tool import create_elearning
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class CourseBuilder():
    """CourseBuilder crew"""

    agents: List[BaseAgent]
    tasks: List[Task]


    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def doc_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['doc_extractor'],
            tools=[extract_pdf_content], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def slide_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['slide_designer'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def elearning_aurthor(self) -> Agent:
        return Agent(
            config=self.agents_config['elearning_aurthor'], # type: ignore[index]
            tools=[create_elearning], # type: ignore[index]
            verbose=True
        )


    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    
    @task
    def extract_pdf_content(self) -> Task:
        return Task(
            config=self.tasks_config['extract_pdf_content_task'], # type: ignore[index]
            output_file='extract.md'
        )
    
    @task
    def slide_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['slide_design_task'],
            output_file='slides.json',
        )
    
    @task
    def create_elearning_task(self) -> Task:
        return Task(
            config=self.tasks_config['elearning_aurthor_task'],
            output_file='elearning.json',
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CourseBuilder crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
