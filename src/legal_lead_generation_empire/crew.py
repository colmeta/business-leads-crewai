import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerpApiGoogleSearchTool,
	ScrapeWebsiteTool
)






@CrewBase
class LegalLeadGenerationEmpireCrew:
    """LegalLeadGenerationEmpire crew"""

    
    @agent
    def local_business_intelligence_agent(self) -> Agent:

        
        return Agent(
            config=self.agents_config["local_business_intelligence_agent"],
            
            
            tools=[
				SerpApiGoogleSearchTool(),
				ScrapeWebsiteTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def lead_qualification_specialist(self) -> Agent:

        
        return Agent(
            config=self.agents_config["lead_qualification_specialist"],
            
            
            tools=[
				ScrapeWebsiteTool(),
				SerpApiGoogleSearchTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def service_provider_outreach_coordinator(self) -> Agent:

        
        return Agent(
            config=self.agents_config["service_provider_outreach_coordinator"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def research_local_service_market(self) -> Task:
        return Task(
            config=self.tasks_config["research_local_service_market"],
            markdown=False,
            
            
        )
    
    @task
    def source_legitimate_lead_opportunities(self) -> Task:
        return Task(
            config=self.tasks_config["source_legitimate_lead_opportunities"],
            markdown=False,
            
            
        )
    
    @task
    def build_service_provider_network(self) -> Task:
        return Task(
            config=self.tasks_config["build_service_provider_network"],
            markdown=False,
            
            
        )
    
    @task
    def daily_lead_matching_operation(self) -> Task:
        return Task(
            config=self.tasks_config["daily_lead_matching_operation"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the LegalLeadGenerationEmpire crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
