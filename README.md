# Job Seeker AI Assistant

A multi-agent AI system built with CrewAI to help job seekers in their job hunting journey.

## Overview

This project leverages CrewAI to build a multi-agent chatbot system designed to assist users in securing their desired jobs. The system comprises specialized agents, each focused on a specific aspect of the job-seeking process:

- **Resume Agent**: Tailors user resumes to specific job descriptions.
- **Skill Gap & Development Agent**: Identifies and recommends resources to bridge skill gaps.
- **Job Search Agent**: Finds and summarizes relevant job postings.
- **Interview Prep Agent**: Prepares users for interviews with practice questions and feedback.
- **Negotiation & Offer Agent**: Provides guidance on offer evaluation and negotiation strategies.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/job-seeker-ai.git
cd job-seeker-ai
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file in the root directory with your API keys:
```
SERPER_API_KEY=your_serper_dev_api_key
```

## Usage

Run the main application:
```bash
python src/job_seeker_ai/main.py
```

## Project Structure

```
job-seeker-ai/
├── src/
│   └── job_seeker_ai/
│       ├── agents/          # Specialized agents
│       ├── config/          # Configuration files
│       ├── tools/           # Custom tools
│       ├── utils/           # Utility functions
│       └── main.py          # Main application entry point
├── tests/                   # Test files
├── .env                     # Environment variables (not tracked by git)
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Testing

Run the tests:
```bash
pytest
```

## License

MIT 