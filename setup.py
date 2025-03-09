#!/usr/bin/env python3
"""
Setup script for the Job Seeker AI Assistant.
"""

from setuptools import setup, find_packages
import os

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="job-seeker-ai",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A multi-agent AI system to help job seekers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/job-seeker-ai",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "job-seeker-ai=job_seeker_ai.main:main",
        ],
    },
) 