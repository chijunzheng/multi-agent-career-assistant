"""
Skill Gap Agent - Specializes in identifying skill gaps and recommending development resources.
"""

from crewai import Agent
from typing import List


class SkillGapAgent(Agent):
    """
    Skill Development Advisor agent that identifies skill gaps between the user's resume 
    and job requirements, and recommends resources to bridge these gaps.
    """
    
    def __init__(self, role: str, goal: str, tools: List):
        """
        Initialize the Skill Gap Agent.
        
        Args:
            role (str): The role of the agent.
            goal (str): The goal of the agent.
            tools (List): The tools available to the agent.
        """
        super().__init__(
            role=role,
            goal=goal,
            backstory="I am a professional career development advisor with expertise in identifying skill gaps and providing targeted learning resources. I help job seekers understand what skills they need to develop to succeed in their desired roles and recommend the best resources to gain those skills efficiently.",
            tools=tools,
            verbose=True
        )
    
    def analyze_skill_gaps(self, resume: str, job_description: str) -> str:
        """
        Analyze skill gaps between a resume and a job description.
        
        Args:
            resume (str): The user's resume.
            job_description (str): The job description.
            
        Returns:
            str: Analysis of skill gaps and recommended resources.
        """
        task = f"""
        Your task is to identify skill gaps between the user's resume and the job description and recommend resources to bridge these gaps.
        
        1. Analyze the job description to identify required skills, qualifications, and experiences.
        2. Review the user's resume to determine which skills they already possess.
        3. Identify gaps between the user's current skills and the job requirements.
        4. For each gap identified, provide:
           a. A clear description of the skill needed
           b. Why this skill is important for the position
           c. Specific recommendations for learning resources (online courses, books, tutorials, etc.)
           d. Estimated time required to develop the skill to a sufficient level
        5. Prioritize the skill gaps based on importance for the role.
        6. Provide a learning roadmap with a suggested timeline.
        
        Job Description:
        {job_description}
        
        Resume:
        {resume}
        """
        
        return self.execute_task(task) 