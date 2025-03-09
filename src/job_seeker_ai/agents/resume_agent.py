"""
Resume Agent - Specializes in optimizing resumes for specific job descriptions.
"""

from crewai import Agent
from typing import List


class ResumeAgent(Agent):
    """
    Resume Optimization Specialist agent that enhances user resumes to align with
    specific job descriptions, highlighting relevant skills and experience.
    """
    
    def __init__(self, role: str, goal: str, tools: List):
        """
        Initialize the Resume Agent.
        
        Args:
            role (str): The role of the agent.
            goal (str): The goal of the agent.
            tools (List): The tools available to the agent.
        """
        super().__init__(
            role=role,
            goal=goal,
            backstory="I am an expert in resume optimization with years of experience in talent acquisition and HR. I specialize in tailoring resumes to match job descriptions, highlighting relevant skills and experiences to maximize the chances of getting interviews.",
            tools=tools,
            verbose=True
        )
    
    def optimize_resume(self, resume: str, job_description: str) -> str:
        """
        Optimize a resume based on a job description.
        
        Args:
            resume (str): The user's resume.
            job_description (str): The job description.
            
        Returns:
            str: The optimized resume.
        """
        task = f"""
        Your task is to optimize the user's resume to match the provided job description.
        
        1. Analyze the job description to identify key skills, qualifications, and experiences required.
        2. Review the user's resume and identify strengths, weaknesses, and gaps compared to the job requirements.
        3. Restructure and rewrite the resume to highlight relevant skills and experiences that match the job description.
        4. Remove or downplay irrelevant information.
        5. Use industry-specific keywords and phrases from the job description.
        6. Ensure the resume follows best practices for formatting and presentation.
        7. Provide a summary of changes made and why they improve the resume's effectiveness.
        
        Job Description:
        {job_description}
        
        Resume:
        {resume}
        """
        
        return self.execute_task(task) 