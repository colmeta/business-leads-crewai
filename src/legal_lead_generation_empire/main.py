import os
import json

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
    SerpApiGoogleSearchTool,
    ScrapeWebsiteTool
)


@CrewBase
class LegalLeadGenerationEmpireCrew:
    """
    Legal Lead Generation Empire Crew
    
    This crew executes the 3-phase blueprint for building a PI lawyer
    lead generation business from $0 to $10k+/month.
    """

    # ==================== AGENTS ====================
    
    @agent
    def pi_law_firm_intelligence_agent(self) -> Agent:
        """
        Phase 1 Agent: Research and identify target PI law firms
        
        This agent finds firms that are spending money on advertising
        but need better quality leads. It's your market intelligence system.
        """
        return Agent(
            config=self.agents_config["pi_law_firm_intelligence_agent"],
            tools=[
                SerpApiGoogleSearchTool(),  # For finding firms and their online presence
                ScrapeWebsiteTool()          # For analyzing firm websites
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
    def pi_lead_qualification_specialist(self) -> Agent:
        """
        Core Value Agent: Finds and qualifies PI leads
        
        This is your money-maker. It filters out bad leads and only
        passes high-quality, pre-vetted clients to law firms.
        """
        return Agent(
            config=self.agents_config["pi_lead_qualification_specialist"],
            tools=[
                ScrapeWebsiteTool(),         # For researching case details
                SerpApiGoogleSearchTool()    # For verifying information
            ],
            reasoning=True,  # Enable reasoning for complex qualification decisions
            max_reasoning_attempts=3,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.5,  # Lower temp for consistent qualification
            ),
        )
    
    @agent
    def pi_law_firm_outreach_coordinator(self) -> Agent:
        """
        Relationship Builder: Signs up law firms as partners
        
        This agent crafts personalized outreach that converts firms
        into paying clients using the risk-free trial offer.
        """
        return Agent(
            config=self.agents_config["pi_law_firm_outreach_coordinator"],
            tools=[],  # No tools needed - pure strategy and communication
            reasoning=True,
            max_reasoning_attempts=2,
            inject_date=True,
            allow_delegation=False,
            max_iter=20,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.8,  # Higher temp for creative, personalized outreach
            ),
        )
    
    @agent
    def pi_client_matching_coordinator(self) -> Agent:
        """
        Operations Manager: Matches leads to firms and tracks $$
        
        This agent runs your daily operations, tracking every lead,
        every consultation, and every dollar earned.
        """
        return Agent(
            config=self.agents_config["pi_client_matching_coordinator"],
            tools=[],  # Operates on data from other agents
            reasoning=True,
            max_reasoning_attempts=2,
            inject_date=True,
            allow_delegation=False,
            max_iter=30,  # More iterations for complex matching logic
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.3,  # Very low temp for consistent operations
            ),
        )

    # ==================== TASKS ====================
    
    @task
    def research_pi_law_firm_market(self) -> Task:
        """
        TASK 1: Market Research
        Phase 1, Week 1
        
        Output: List of 20-30 target PI law firms with full profiles
        """
        return Task(
            config=self.tasks_config["research_pi_law_firm_market"],
            markdown=True,  # Enable markdown for nicely formatted output
        )
    
    @task
    def source_qualified_pi_leads(self) -> Task:
        """
        TASK 2: Lead Generation & Qualification
        Phase 1, Week 2-4 (ongoing)
        
        Output: Daily batch of 3-10 qualified PI leads
        """
        return Task(
            config=self.tasks_config["source_qualified_pi_leads"],
            markdown=True,
        )
    
    @task
    def build_pi_law_firm_network(self) -> Task:
        """
        TASK 3: Partnership Outreach
        Phase 1, Week 1-4
        
        Output: Outreach templates, follow-up sequences, signed partners
        """
        return Task(
            config=self.tasks_config["build_pi_law_firm_network"],
            markdown=True,
        )
    
    @task
    def execute_daily_lead_matching(self) -> Task:
        """
        TASK 4: Daily Operations (The Money Maker)
        Phase 1-3, Ongoing
        
        Output: Daily report of leads matched, consultations booked, revenue earned
        """
        return Task(
            config=self.tasks_config["execute_daily_lead_matching"],
            markdown=True,
        )

    # ==================== CREW ASSEMBLY ====================
    
    @crew
    def crew(self) -> Crew:
        """
        Assembles the Legal Lead Generation Empire crew
        
        Process: Sequential (each task depends on the previous one)
        - First: Research target firms
        - Second: Generate qualified leads
        - Third: Build partner network
        - Fourth: Execute daily matching operations
        """
        return Crew(
            agents=self.agents,  # All 4 agents defined above
            tasks=self.tasks,    # All 4 tasks defined above
            process=Process.sequential,  # Run tasks in order
            verbose=True,  # Show detailed execution logs
            memory=True,   # Enable memory so agents learn over time
            planning=True,  # Enable planning for complex multi-step tasks
        )

    # ==================== UTILITY METHODS ====================
    
    def _load_response_format(self, name):
        """
        Load structured output formats for agents
        (Currently unused, but available for future JSON schema validation)
        """
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())
        
        # Note: SchemaConverter import needed if you use this
        # from crewai import SchemaConverter
        # return SchemaConverter.build(json_schema)
        return json_schema
