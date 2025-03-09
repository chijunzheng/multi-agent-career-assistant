"""
Resume Parser Tool - A custom tool for parsing resumes.
"""

import re
from typing import Dict, Any, Optional
from langchain.tools import BaseTool


class ResumeParser(BaseTool):
    """
    A tool for parsing resumes to extract relevant information.
    """
    
    name = "resume_parser"
    description = "Parse a resume to extract relevant information such as skills, experience, education, etc."
    
    def _extract_contact_info(self, text: str) -> Dict[str, str]:
        """
        Extract contact information from the resume.
        
        Args:
            text (str): The resume text.
            
        Returns:
            Dict[str, str]: Extracted contact information.
        """
        contact_info = {}
        
        # Extract email
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_match = re.search(email_pattern, text)
        if email_match:
            contact_info['email'] = email_match.group(0)
        
        # Extract phone number (simple pattern)
        phone_pattern = r'\b(?:\+\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
        phone_match = re.search(phone_pattern, text)
        if phone_match:
            contact_info['phone'] = phone_match.group(0)
        
        # Extract LinkedIn URL
        linkedin_pattern = r'linkedin\.com/in/[A-Za-z0-9_-]+'
        linkedin_match = re.search(linkedin_pattern, text)
        if linkedin_match:
            contact_info['linkedin'] = linkedin_match.group(0)
        
        return contact_info
    
    def _extract_skills(self, text: str) -> list:
        """
        Extract skills from the resume.
        
        Args:
            text (str): The resume text.
            
        Returns:
            list: List of extracted skills.
        """
        # Look for skills section
        skills_section_pattern = r'(?i)(?:SKILLS|TECHNICAL SKILLS|CORE COMPETENCIES|COMPETENCIES|PROFICIENCIES)[^\n]*\n+(.*?)(?:\n\n|\n[A-Z][A-Z\s]+:|\Z)'
        skills_match = re.search(skills_section_pattern, text, re.DOTALL)
        
        skills = []
        if skills_match:
            skills_text = skills_match.group(1)
            # Extract skills listed with commas or bullet points
            skills = [
                skill.strip() 
                for skill in re.split(r'[,•\n]', skills_text) 
                if skill.strip() and len(skill.strip()) > 1
            ]
        
        return skills
    
    def _extract_education(self, text: str) -> list:
        """
        Extract education information from the resume.
        
        Args:
            text (str): The resume text.
            
        Returns:
            list: List of extracted education entries.
        """
        # Look for education section
        education_section_pattern = r'(?i)(?:EDUCATION|ACADEMIC BACKGROUND)[^\n]*\n+(.*?)(?:\n\n|\n[A-Z][A-Z\s]+:|\Z)'
        education_match = re.search(education_section_pattern, text, re.DOTALL)
        
        education = []
        if education_match:
            education_text = education_match.group(1)
            # Split by new lines to get education entries
            entries = [entry.strip() for entry in education_text.split('\n') if entry.strip()]
            education = entries
        
        return education
    
    def _extract_experience(self, text: str) -> list:
        """
        Extract work experience information from the resume.
        
        Args:
            text (str): The resume text.
            
        Returns:
            list: List of extracted experience entries.
        """
        # Look for experience section
        experience_section_pattern = r'(?i)(?:EXPERIENCE|WORK EXPERIENCE|PROFESSIONAL EXPERIENCE|EMPLOYMENT)[^\n]*\n+(.*?)(?:\n\n|\n[A-Z][A-Z\s]+:|\Z)'
        experience_match = re.search(experience_section_pattern, text, re.DOTALL)
        
        experience = []
        if experience_match:
            experience_text = experience_match.group(1)
            # Split by double new lines to get experience entries
            entries = [entry.strip() for entry in re.split(r'\n\s*\n', experience_text) if entry.strip()]
            experience = entries
        
        return experience
    
    def _run(self, text: str) -> Dict[str, Any]:
        """
        Parse a resume text to extract relevant information.
        
        Args:
            text (str): The resume text to parse.
            
        Returns:
            Dict[str, Any]: Extracted information from the resume.
        """
        parsed_data = {
            'contact_info': self._extract_contact_info(text),
            'skills': self._extract_skills(text),
            'education': self._extract_education(text),
            'experience': self._extract_experience(text),
            'full_text': text
        }
        
        return parsed_data
    
    async def _arun(self, text: str) -> Dict[str, Any]:
        """
        Async version of _run.
        
        Args:
            text (str): The resume text to parse.
            
        Returns:
            Dict[str, Any]: Extracted information from the resume.
        """
        return self._run(text) 