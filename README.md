# CrewAI Research Assistant Example

This my personal diary of experiments with crewAI and agents. Please feel free to use it as you see fit. The example shows two AI agents working together to conduct research and analysis on healthcare topics.

## Features

- Multi-agent collaboration using CrewAI
- Integration with Perplexity AI's language model
- Research and analysis pipeline
- Structured output generation

## Prerequisites

- Python 3.8+
- Perplexity API key

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. All you need is an API key of the model hostel on an inference service. Pick the one you like and want to use for these experiments. Create a `.env` file in the root directory and add your Perplexity API key:
```
PERPLEXITY_API_KEY=your_api_key_here
```

## Project Structure

```
crewai-experiments/
├── examples/
│   └── research_crew.py      # Main example script
├── .env                      # Environment variables (not tracked in git)
├── .gitignore               # Git ignore file
├── LICENSE                  # License file
├── README.md               # This file
└── requirements.txt        # Project dependencies
```

## Usage

Run the example script:
```bash
python examples/research_crew.py
```

The script will:
1. Create two AI agents: a Research Specialist and a Data Analyst
2. The Research Specialist will gather information about AI in healthcare
3. The Data Analyst will analyze the findings and provide recommendations
4. Output a structured report with findings and insights

## How It Works

The example demonstrates the following concepts:

1. **Agent Creation**: Defines specialized agents with specific roles and goals
```python
researcher = Agent(
    role='Research Specialist',
    goal='Conduct thorough research on given topics',
    backstory='Experienced research specialist with attention to detail'
)
```

2. **Task Definition**: Creates tasks for agents to execute
```python
research_task = Task(
    description='Research AI developments in healthcare...',
    agent=researcher
)
```

3. **Crew Assembly**: Combines agents and tasks into a working crew
```python
crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task]
)
```

## Output

The script generates a structured report containing:
- Research findings on AI in healthcare
- Analysis of key trends and patterns
- Future implications
- Recommendations for healthcare providers

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) - Framework for orchestrating role-playing AI agents
- [Perplexity AI](https://www.perplexity.ai/) - Language model provider
