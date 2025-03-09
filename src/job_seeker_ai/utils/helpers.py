"""
Helper utility functions for the Job Seeker AI Assistant.
"""

import os
import logging
from typing import Dict, Any, Optional


def setup_logging(log_level: str = "INFO") -> logging.Logger:
    """
    Set up logging for the application.
    
    Args:
        log_level (str): The log level to use. Defaults to "INFO".
        
    Returns:
        logging.Logger: Configured logger.
    """
    level = getattr(logging, log_level.upper())
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("job_seeker_ai")


def read_file_content(file_path: str) -> Optional[str]:
    """
    Read the content of a file.
    
    Args:
        file_path (str): Path to the file.
        
    Returns:
        Optional[str]: The content of the file, or None if the file cannot be read.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        logger = logging.getLogger("job_seeker_ai")
        logger.error(f"Error reading file {file_path}: {e}")
        return None


def validate_input(input_data: Dict[str, Any], required_fields: list) -> bool:
    """
    Validate that all required fields are present in the input data.
    
    Args:
        input_data (Dict[str, Any]): The input data to validate.
        required_fields (list): List of required field names.
        
    Returns:
        bool: True if all required fields are present, False otherwise.
    """
    logger = logging.getLogger("job_seeker_ai")
    
    for field in required_fields:
        if field not in input_data or not input_data[field]:
            logger.error(f"Missing required field: {field}")
            return False
    
    return True


def save_result(result: str, output_path: str) -> bool:
    """
    Save a result to a file.
    
    Args:
        result (str): The result to save.
        output_path (str): Path to save the result to.
        
    Returns:
        bool: True if the result was saved successfully, False otherwise.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as file:
            file.write(result)
        return True
    except Exception as e:
        logger = logging.getLogger("job_seeker_ai")
        logger.error(f"Error saving result to {output_path}: {e}")
        return False 