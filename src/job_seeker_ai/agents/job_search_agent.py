"""
Job Search Agent - Specializes in finding and summarizing relevant job postings.
"""

from crewai import Agent
from typing import List


class JobSearchAgent(Agent):
    """
    Job Search Specialist agent that finds and summarizes relevant job postings
    based on user preferences and qualifications.
    """
    
    def __init__(self, role: str, goal: str, tools: List):
        """
        Initialize the Job Search Agent.
        
        Args:
            role (str): The role of the agent.
            goal (str): The goal of the agent.
            tools (List): The tools available to the agent.
        """
        super().__init__(
            role=role,
            goal=goal,
            backstory="I am a seasoned job search specialist with extensive knowledge of job markets, industry trends, and recruitment practices. I excel at finding relevant job opportunities that match a candidate's skills, experience, and career goals across various platforms and networks.",
            tools=tools,
            verbose=True
        )
    
    def find_job_opportunities(self, resume: str, job_preferences: str) -> str:
        """
        Find job opportunities based on resume and preferences.
        
        Args:
            resume (str): The user's resume.
            job_preferences (str): The user's job preferences.
            
        Returns:
            str: A list of relevant job opportunities.
        """
        task = f"""
        Your task is to find and summarize relevant job opportunities based on the user's resume and preferences.
        
        1. Analyze the user's resume to understand their skills, qualifications, and experience.
        2. Consider the user's job preferences.
        3. Use web search to find job postings that match the user's profile and preferences.
        4. For each relevant job posting, provide:
           a. Job title and company
           b. Location (including remote options)
           c. Key responsibilities and requirements
           d. Compensation information (if available)
           e. Match score (how well the job matches the user's profile)
           f. Application link or process
        5. Recommend the top 5 jobs with a brief explanation of why they're a good fit.
        6. Suggest search terms or job titles the user might not have considered but would be qualified for.
        
        Resume:
        {resume}
        
        Job Preferences:
        {job_preferences}
        """
        
        return self.execute_task(task)
    
    def analyze_job_market(self, industry: str, location: str) -> str:
        """
        Analyze the job market for a specific industry and location.
        
        Args:
            industry (str): The industry to analyze.
            location (str): The location to analyze.
            
        Returns:
            str: Analysis of the job market.
        """
        task = f"""
        Your task is to analyze the job market for the specified industry and location.
        
        1. Research the current state of the job market in the {industry} industry in {location}.
        2. Provide information on:
           a. Current demand for professionals in this field
           b. Average salary ranges for different positions
           c. Required skills and qualifications
           d. Major employers and companies that are hiring
           e. Industry trends and outlook
           f. Competition level for jobs in this market
        3. Identify emerging opportunities and recommend strategies for job seekers in this market.
        4. Compare this market with national or global trends for context.
        
        Industry: {industry}
        Location: {location}
        """
        
        return self.execute_task(task) 