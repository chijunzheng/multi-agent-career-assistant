"""
Negotiation Agent - Specializes in providing guidance on offer evaluation and negotiation strategies.
"""

from crewai import Agent
from typing import List


class NegotiationAgent(Agent):
    """
    Negotiation and Offer Specialist agent that provides guidance on offer evaluation
    and negotiation strategies to help users secure better compensation packages.
    """
    
    def __init__(self, role: str, goal: str, tools: List):
        """
        Initialize the Negotiation Agent.
        
        Args:
            role (str): The role of the agent.
            goal (str): The goal of the agent.
            tools (List): The tools available to the agent.
        """
        super().__init__(
            role=role,
            goal=goal,
            backstory="I am a negotiation expert with extensive experience in the recruitment and HR space. I specialize in helping job seekers evaluate job offers and negotiate competitive compensation packages that reflect their true market value. I understand both the candidate and employer perspectives in the negotiation process.",
            tools=tools,
            verbose=True
        )
    
    def evaluate_job_offer(self, offer_details: str, resume: str, job_description: str) -> str:
        """
        Evaluate a job offer based on the details provided.
        
        Args:
            offer_details (str): The details of the job offer.
            resume (str): The user's resume.
            job_description (str): The job description.
            
        Returns:
            str: An evaluation of the job offer.
        """
        task = f"""
        Your task is to evaluate the job offer based on the details provided and provide guidance.
        
        1. Analyze the job offer details, including:
           a. Base salary
           b. Bonuses and incentives
           c. Benefits (healthcare, retirement, etc.)
           d. Stock options or equity
           e. Vacation time and other perks
           f. Role and responsibilities
           g. Growth opportunities
        2. Compare the offer to industry standards for similar roles by researching current market rates.
        3. Consider the user's qualifications, experience, and value they would bring to the company.
        4. Evaluate the offer's strengths and weaknesses.
        5. Provide a detailed assessment of whether the offer is fair, below market, or above market.
        6. Identify specific components that could be negotiated for improvement.
        7. Make a recommendation on whether to accept, negotiate, or decline the offer.
        
        Offer Details:
        {offer_details}
        
        Resume:
        {resume}
        
        Job Description:
        {job_description}
        """
        
        return self.execute_task(task)
    
    def prepare_negotiation_strategy(self, offer_details: str, desired_terms: str, resume: str) -> str:
        """
        Prepare a negotiation strategy based on the offer and desired terms.
        
        Args:
            offer_details (str): The details of the job offer.
            desired_terms (str): The user's desired terms.
            resume (str): The user's resume.
            
        Returns:
            str: A negotiation strategy.
        """
        task = f"""
        Your task is to prepare a comprehensive negotiation strategy based on the current offer and desired terms.
        
        1. Analyze the gap between the current offer and the user's desired terms.
        2. Research market rates for similar positions to support negotiation points.
        3. Develop a tailored negotiation strategy, including:
           a. Opening statements and tone to set a positive, collaborative approach
           b. Specific requests with justifications based on market value and the user's qualifications
           c. Prioritized list of items to negotiate (which are most important vs. nice-to-have)
           d. Fallback positions and minimum acceptable terms
           e. Potential trade-offs to suggest (e.g., if higher salary isn't possible, what alternatives could be valuable)
        4. Provide sample scripts for different negotiation scenarios, including:
           a. Initial response to the offer
           b. Negotiation conversation starters
           c. Handling potential pushback
           d. Closing the negotiation successfully
        5. Include timing recommendations and communication channel advice.
        6. Suggest specific language to articulate value and avoid common negotiation pitfalls.
        
        Current Offer Details:
        {offer_details}
        
        Desired Terms:
        {desired_terms}
        
        Resume:
        {resume}
        """
        
        return self.execute_task(task) 