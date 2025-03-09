#!/usr/bin/env python3
"""
Main entry point for the Job Seeker AI Assistant.

This script initializes the CrewAI multi-agent system and provides
a simple command-line interface for interacting with the agents.
"""

import os
import yaml
import logging
from dotenv import load_dotenv
from crewai import Crew, Process
from crewai.tools import SerperDevAPI, WebScraper

from job_seeker_ai.agents.resume_agent import ResumeAgent
from job_seeker_ai.agents.skill_gap_agent import SkillGapAgent
from job_seeker_ai.agents.job_search_agent import JobSearchAgent
from job_seeker_ai.agents.interview_prep_agent import InterviewPrepAgent
from job_seeker_ai.agents.negotiation_agent import NegotiationAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def load_config(config_path):
    """
    Load agent configurations from a YAML file.
    
    Args:
        config_path (str): Path to the configuration file.
        
    Returns:
        dict: The loaded configuration.
    """
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        return {}

def initialize_tools():
    """
    Initialize the tools for the agents.
    
    Returns:
        tuple: Initialized SerperDevAPI and WebScraper tools.
    """
    serper_api_key = os.getenv("SERPER_API_KEY")
    if not serper_api_key:
        logger.warning("SERPER_API_KEY not found in environment variables.")
        
    serper_dev_api = SerperDevAPI(api_key=serper_api_key)
    web_scraper = WebScraper()
    
    return serper_dev_api, web_scraper

def initialize_agents(config, tools):
    """
    Initialize the agents with their configurations and tools.
    
    Args:
        config (dict): Agent configurations.
        tools (list): List of tools to be used by the agents.
        
    Returns:
        list: List of initialized agents.
    """
    resume_agent = ResumeAgent(
        config["resume_agent"]["role"],
        config["resume_agent"]["goal"],
        tools
    )
    
    skill_gap_agent = SkillGapAgent(
        config["skill_gap_agent"]["role"],
        config["skill_gap_agent"]["goal"],
        tools
    )
    
    job_search_agent = JobSearchAgent(
        config["job_search_agent"]["role"],
        config["job_search_agent"]["goal"],
        tools
    )
    
    interview_prep_agent = InterviewPrepAgent(
        config["interview_prep_agent"]["role"],
        config["interview_prep_agent"]["goal"],
        tools
    )
    
    negotiation_agent = NegotiationAgent(
        config["negotiation_agent"]["role"],
        config["negotiation_agent"]["goal"],
        tools
    )
    
    return [
        resume_agent,
        skill_gap_agent,
        job_search_agent,
        interview_prep_agent,
        negotiation_agent
    ]

def create_crew(agents):
    """
    Create a crew with the initialized agents.
    
    Args:
        agents (list): List of initialized agents.
        
    Returns:
        Crew: Initialized CrewAI crew.
    """
    return Crew(
        agents=agents,
        process=Process.sequential,  # Agents will work sequentially
        verbose=True
    )

def main():
    """
    Main function to run the Job Seeker AI Assistant.
    """
    # Initialize tools
    serper_dev_api, web_scraper = initialize_tools()
    tools = [serper_dev_api, web_scraper]
    
    # Load agent configurations
    config = load_config("src/job_seeker_ai/config/agents.yaml")
    if not config:
        logger.error("Failed to load agent configurations.")
        return
    
    # Initialize agents
    agents = initialize_agents(config, tools)
    
    # Create the crew
    crew = create_crew(agents)
    
    # Simple CLI interface
    print("\n=== Job Seeker AI Assistant ===\n")
    print("Welcome to the Job Seeker AI Assistant!")
    print("This assistant will help you with various aspects of your job search.\n")
    
    job_description = input("Please provide a job description: ")
    resume = input("Please provide your resume (or path to resume file): ")
    
    # If resume is a file path, read the file
    if os.path.isfile(resume):
        try:
            with open(resume, 'r') as file:
                resume = file.read()
        except Exception as e:
            logger.error(f"Error reading resume file: {e}")
            print("Error reading resume file. Please try again.")
            return
    
    # Run the crew with the provided inputs
    result = crew.kickoff(
        inputs={
            "job_description": job_description,
            "resume": resume
        }
    )
    
    print("\n=== Results ===\n")
    print(result)

if __name__ == "__main__":
    main() 