"""
Tests for the Resume Agent.
"""

import pytest
from unittest.mock import Mock, patch
from src.job_seeker_ai.agents.resume_agent import ResumeAgent


def test_init():
    """Test Resume Agent initialization."""
    # Arrange
    role = "Test Role"
    goal = "Test Goal"
    tools = []
    
    # Act
    agent = ResumeAgent(role, goal, tools)
    
    # Assert
    assert agent.role == role
    assert agent.goal == goal
    assert agent.tools == tools


@patch('src.job_seeker_ai.agents.resume_agent.Agent.execute_task')
def test_optimize_resume(mock_execute_task):
    """Test optimize_resume method."""
    # Arrange
    mock_execute_task.return_value = "Optimized resume content"
    
    role = "Test Role"
    goal = "Test Goal"
    tools = []
    agent = ResumeAgent(role, goal, tools)
    
    resume = "Test resume content"
    job_description = "Test job description"
    
    # Act
    result = agent.optimize_resume(resume, job_description)
    
    # Assert
    assert result == "Optimized resume content"
    mock_execute_task.assert_called_once()
    
    # Verify that the task contains both the resume and job description
    task_arg = mock_execute_task.call_args[0][0]
    assert resume in task_arg
    assert job_description in task_arg


def test_optimize_resume_with_mock_tools():
    """Test optimize_resume with mock tools."""
    # Arrange
    mock_serper = Mock()
    mock_serper.name = "serper_dev_api"
    mock_serper.return_value = "Mocked search result"
    
    mock_scraper = Mock()
    mock_scraper.name = "web_scraper"
    mock_scraper.return_value = "Mocked web content"
    
    tools = [mock_serper, mock_scraper]
    
    with patch('src.job_seeker_ai.agents.resume_agent.Agent.execute_task', return_value="Optimized resume with search data"):
        agent = ResumeAgent("Resume Specialist", "Optimize resumes", tools)
        
        # Act
        result = agent.optimize_resume("Sample resume", "Sample job description")
        
        # Assert
        assert result == "Optimized resume with search data" 