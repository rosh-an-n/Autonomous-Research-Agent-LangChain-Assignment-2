# Autonomous Research Agent

An AI-powered research agent built with LangChain that automatically researches any topic and generates a structured Markdown report.

## Features

- **Web Search**: Searches the web using DuckDuckGo for current information, statistics, and real-world examples
- **Knowledge Retrieval**: Queries Wikipedia for background information, definitions, and historical context
- **ReAct Agent**: Uses LangChain's ReAct (Reasoning + Acting) agent pattern for intelligent multi-step research
- **Structured Reports**: Generates professional Markdown reports with Introduction, Key Findings, Challenges, Future Scope, and Conclusion

## Tech Stack

- **Python 3.9+**
- **LangChain** — Agent framework
- **OpenRouter** — LLM provider (OpenAI-compatible API)
- **DuckDuckGo Search** — Web search (free, no API key)
- **Wikipedia API** — Knowledge base

## Project Structure

```
autonomous-research-agent/
├── main.py                  # CLI entry point
├── agent.py                 # ReAct agent setup
├── report_generator.py      # Markdown report formatter
├── tools/
│   ├── __init__.py
│   ├── web_search.py        # DuckDuckGo search tool
│   └── knowledge_tool.py    # Wikipedia tool
├── requirements.txt
├── .env.example
├── outputs/                 # Generated reports
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd autonomous-research-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # for macOS/Linux
venv\Scripts\activate   # for Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your OpenRouter API key:

```
OPENROUTER_API_KEY=your-openrouter-api-key-here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

You can get a free API key at [openrouter.ai](https://openrouter.ai).

## Usage

### Command-line argument

```bash
python main.py "How to Bake a Cake"
```

### Interactive mode

```bash
python main.py
```

Then enter your topic when prompted.

### Output

Reports are saved to the `outputs/` directory as Markdown files. For example:
- `outputs/impact_of_ai_in_healthcare.md`
- `outputs/climate_change_and_renewable_energy.md`

## Report Format

Each generated report includes:

- **Cover Page** — Topic, date, and metadata
- **Introduction** — Overview and context
- **Key Findings** — Main discoveries and insights
- **Challenges** — Limitations and obstacles identified
- **Future Scope** — Emerging trends and future directions
- **Conclusion** — Summary and final thoughts

## Architecture

The agent follows the **ReAct (Reasoning + Acting)** pattern:

1. **Thought** — The agent reasons about what information is needed
2. **Action** — The agent selects and calls a tool (web search or Wikipedia)
3. **Observation** — The agent processes the tool's output
4. **Repeat** — Until sufficient information is gathered
5. **Final Answer** — The agent synthesizes a comprehensive research summary

The report generator then transforms the raw output into a structured Markdown document.

## Sample Topics

- "Impact of AI in Healthcare"
- "Climate Change and Renewable Energy"
- "Future of Quantum Computing"
- "Blockchain Technology in Finance"
- "Cybersecurity Trends 2025"

