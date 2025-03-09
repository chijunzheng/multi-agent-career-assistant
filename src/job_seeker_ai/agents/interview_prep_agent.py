"""
Interview Prep Agent - Specializes in preparing users for interviews with practice questions and feedback.
"""

from crewai import Agent
from typing import List


class InterviewPrepAgent(Agent):
    """
    Interview Preparation Coach agent that prepares users for interviews with practice
    questions and feedback tailored to specific job roles.
    """
    
    def __init__(self, role: str, goal: str, tools: List):
        """
        Initialize the Interview Prep Agent.
        
        Args:
            role (str): The role of the agent.
            goal (str): The goal of the agent.
            tools (List): The tools available to the agent.
        """
        super().__init__(
            role=role,
            goal=goal,
            backstory="I am an experienced interview coach who has helped thousands of candidates successfully prepare for job interviews across various industries. I specialize in identifying the most likely questions for specific roles and providing targeted feedback to improve interview performance.",
            tools=tools,
            verbose=True
        )
    
    def generate_interview_questions(self, job_description: str, resume: str) -> str:
        """
        Generate interview questions based on job description and resume.
        
        Args:
            job_description (str): The job description.
            resume (str): The user's resume.
            
        Returns:
            str: A list of potential interview questions with preparation guidance.
        """
        task = f"""
        Your task is to generate tailored interview questions based on the job description and the user's resume.
        
        1. Analyze the job description to identify key skills, qualifications, and experiences required.
        2. Review the user's resume to understand their background and potential areas of strength or weakness.
        3. Generate a comprehensive set of interview questions, including:
           a. Technical questions specific to the role's requirements
           b. Behavioral questions to assess fit with company culture
           c. Situational questions based on likely scenarios in the role
           d. Questions about the user's experience and how it relates to the job
           e. Questions that might address potential gaps or concerns in the resume
        4. For each question, provide:
           a. The question itself
           b. Why this question might be asked
           c. Tips for how to effectively answer it
           d. Examples of strong responses
        5. Include a section on common challenging questions for this role and how to address them.
        6. Provide general interview preparation advice tailored to this specific role and company.
        
        Job Description:
        {job_description}
        
        Resume:
        {resume}
        """
        
        return self.execute_task(task)
    
    def conduct_mock_interview(self, job_description: str, resume: str, interview_focus: str) -> str:
        """
        Conduct a mock interview based on job description, resume, and specified focus.
        
        Args:
            job_description (str): The job description.
            resume (str): The user's resume.
            interview_focus (str): The focus area for the mock interview.
            
        Returns:
            str: A simulated interview with questions and feedback.
        """
        task = f"""
        Your task is to conduct a mock interview based on the job description, resume, and specified focus area.
        
        1. Begin with a brief introduction explaining how the mock interview will work.
        2. Ask a series of 5-7 questions focused on the specified area of focus, but also covering general aspects of the role.
        3. For each question:
           a. Provide space for the user to mentally compose their answer
           b. Offer detailed feedback on what a strong answer would include
           c. Highlight key points that should be mentioned
           d. Point out potential pitfalls to avoid
        4. Include at least one challenging or unexpected question that might catch the candidate off guard.
        5. Conclude with overall feedback, including:
           a. Strengths to emphasize in the actual interview
           b. Areas for improvement
           c. Specific preparation recommendations before the real interview
        
        Job Description:
        {job_description}
        
        Resume:
        {resume}
        
        Interview Focus Area:
        {interview_focus}
        """
        
        return self.execute_task(task) 