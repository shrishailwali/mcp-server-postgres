MCP Server with PostgreSQL, uV Python, and AutoGen AI
Overview
This project is a modular backend server built with uV Python, powered by PostgreSQL for data storage and integrated with AutoGen AI for intelligent data processing and autonomous task execution. The core module, MCP (Modular Command Processor), handles structured interactions between the database and AI agents, supporting real-time operations, import validation, and AI-augmented decision logic.

Key Components
uV Python: Lightweight, isolated Python environment used for fast, reproducible deployments.

PostgreSQL: Robust relational database for structured data storage and querying.

MCP (Modular Command Processor): Core logic engine to orchestrate data imports, validation, and transformations using schema-driven rules.

AutoGen AI: Integrated to augment operations with AI capabilities such as natural language query processing, autonomous task execution, and intelligent agent support.

Features
Schema-based data validation and transformation

AI-assisted natural language interaction with the database

Streamlined setup using pyproject.toml and uv

Clean modular structure for extensibility and maintainability

Getting Started
Prerequisites
Python 3.10+

uV (installed via pip: pip install uv)

PostgreSQL running locally or remotely

Setup Instructions
bash
Copy
Edit
# Clone the repository
git clone https://github.com/your-username/MCP_Server_Postgres.git
cd MCP_Server_Postgres

# Install dependencies using uV
uv pip install -r requirements.txt  # or use pyproject.toml directly
Environment Configuration
Create a .env file with the following keys:

env
Copy
Edit
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_DB=cmms
POSTGRES_PASSWORD=yourpassword
Run the Server
bash
Copy
Edit
uvicorn main:app --reload
Project Structure
bash
Copy
Edit
MCP_Server_Postgres/
├── main.py               # FastAPI app entry point
├── db.py                 # Database connection logic
├── schemas/              # JSON schema definitions for assets, parts, etc.
├── utils/                # Helper functions for transformation and validation
├── .env                  # Environment configuration
├── pyproject.toml        # Project dependencies and metadata
└── uv.lock               # uV environment lock file
Integration with AutoGen AI
AutoGen is used to:

Parse user input (e.g., file uploads, commands)

Generate SQL queries via AI agents

Automate backend workflows with LLM-powered reasoning

AutoGen integration uses your Azure OpenAI deployment named spick-ai to generate responses and perform actions.