# 🤖 Multi-AI-Agents Research

### An Intelligent Multi-Agent Research System Powered by Python and LLMs

A modular AI research application that combines multiple AI agents, custom tools, prompt engineering, and execution pipelines to automate web research and information gathering.

The project demonstrates how AI agents can collaborate to search for information, retrieve relevant web content, and generate research-oriented responses through a structured workflow.

---

## 🚀 Key Features

- **Multi-Agent Architecture:** Organizes AI tasks into specialized agent workflows.
- **AI-Powered Research:** Uses large language models (LLMs) to process research queries.
- **Web Search Integration:** Retrieves relevant information using web search tools.
- **Web Scraping:** Extracts useful content from web pages for further processing.
- **Custom Tools:** Integrates reusable tools for search and information retrieval.
- **Prompt Engineering:** Uses custom prompts and templates to guide AI responses.
- **Modular Pipeline:** Separates agent logic, tools, prompts, and application execution.
- **Web Interface:** Provides an HTML-based interface through Flask templates.
- **Environment Configuration:** Manages API keys and configuration through environment variables.

---
<img width="1322" height="611" alt="Screenshot 2026-10-12 145656" src="https://github.com/user-attachments/assets/ada5c21b-60d1-4121-847e-75793e1a6668" />

<video controls src="Screen Recording 2026-10-12 161301.mp4" title="Title"></video>

## 🏗️ Project Architecture

The application follows a modular architecture in which each component has a specific responsibility.

```text
User Query
    |
    v
Web Interface (app.py)
    |
    v
Research Pipeline (pipline.py)
    |
    v
AI Agents (agents.py)
    |
    +----------------------+
    |                      |
    v                      v
Web Search Tool       Web Scraping Tool
    |                      |
    +----------+-----------+
               |
               v
      Retrieved Information
               |
               v
   LLM Processing & Prompting
               |
               v
       Research Response
```

*Note: The diagram represents the intended high-level workflow. The exact execution sequence depends on the implementation in your source files.*

---

## 📂 Project Structure

```text
Multi-Ai-Agents-Research/
│
├── templates/
│   └── index.html            # Web interface template
│
├── agents.py                 # AI agent definitions and logic
├── app.py                    # Main application entry point
├── pipline.py                 # Research execution pipeline
├── prompt_and_chain.py       # Prompt templates and chain logic
├── tools.py                  # Custom search and scraping tools
│
├── requirements.txt          # Python dependencies
├── .env.example              # Example environment configuration
├── .gitignore                # Files excluded from Git
├── README.md                 # Project documentation
└── pyproject.toml             # Project configuration (if used)
```

> The `.venv/` directory and `.env` file should remain local and must not be committed to GitHub.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM integration, tools, and chaining |
| Hugging Face | Language model integration |
| Tavily Search API | Web search and research |
| BeautifulSoup | HTML parsing and web scraping |
| Flask | Web application backend |
| HTML / CSS | Web interface |
| python-dotenv | Environment variable management |
| uv | Python package and project management |

*The technologies listed above should match the libraries and integrations actually used in your source code and dependency file.*

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/gautam-purohit2006/Multi-Ai-Agents-Research.git
cd Multi-Ai-Agents-Research
```

### 2. Install uv

If `uv` is not installed, follow the official installation instructions:

https://docs.astral.sh/uv/getting-started/installation/

Verify the installation:

```bash
uv --version
```

### 3. Create a virtual environment

```bash
uv venv
```

Activate it on Windows Git Bash:

```bash
source .venv/Scripts/activate
```

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

If the project contains `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root.

Example configuration:

```env
HF_TOKEN=your_huggingface_token
TAVILY_API_KEY=your_tavily_api_key
```

Replace the example values with your own valid API credentials. Use only the variables required by your actual code.

Get your API credentials from:

- Hugging Face: https://huggingface.co/settings/tokens
- Tavily: https://app.tavily.com/

**Security:** Never upload your real `.env` file, API keys, or access tokens to GitHub.

### 6. Run the application

If `app.py` contains a Flask application:

```bash
python app.py
```

If the application uses Flask's CLI instead:

```bash
flask --app app run --debug
```

Open the local URL displayed in your terminal, commonly:

http://127.0.0.1:5000/

Use the command that matches the entry point implemented in your project.

---

## 🔄 How It Works

1. **Query Input:** The user submits a research question through the application interface.
2. **Pipeline Execution:** The application passes the query to the research pipeline.
3. **Agent Processing:** The configured AI agent or agents process the query using the selected LLM.
4. **Information Retrieval:** Search and scraping tools gather relevant web information.
5. **Prompt and Chain Processing:** Retrieved information is processed according to the configured prompts and chain logic.
6. **Response Generation:** The application returns the resulting research response to the user.

The actual agent collaboration, tool-calling behavior, and response-generation process depend on the implementation and model configuration.

---

## 💡 Example Use Cases

- Researching AI and machine learning topics
- Gathering information from multiple web sources
- Exploring technical concepts and documentation
- Building modular LLM-powered research workflows
- Experimenting with AI agents and custom tools
- Prototyping automated information retrieval applications

---

## 🔐 Environment and Security

- Keep API credentials in `.env`.
- Add `.env` and `.venv/` to `.gitignore`.
- Use `.env.example` to document required variable names without exposing secrets.
- Avoid committing logs, caches, generated databases, and unnecessary files.
- Rotate any API key accidentally exposed in a public repository.

---

## 🚧 Future Improvements

- Add dedicated search, analysis, and summarization agents.
- Implement source citations and research references.
- Add conversation history and persistent research sessions.
- Introduce structured outputs and validation.
- Add error handling, retry logic, and logging.
- Support configurable LLM providers and models.
- Add automated tests and CI workflows.
- Deploy the application to a cloud platform.

---

## 👨‍💻 Author

**Gautam Purohit**

B.Sc. (CA & IT) Graduate | Python | Machine Learning | Generative AI | LLMs | AI Agents

- **GitHub:** https://github.com/gautam-purohit2006
- **LinkedIn:** https://www.linkedin.com/in/gautam-purohit-618383315/

---

## 📌 Project Status

**Status:** Learning and Development

This project is part of my practical learning journey in Generative AI, LLM applications, agent-based workflows, prompt engineering, and tool integration.

---

⭐ If you find this project useful, consider giving the repository a star!
