import os
from module.schema import load_schema
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken
from autogen_agentchat.messages import TextMessage

# Load environment variables
model_ = os.getenv("MODEL_", "gpt-4o")
openapi_base = os.getenv("AZURE_API_BASE", "").strip()
openapi_version = os.getenv("AZURE_API_VERSION", "").strip()
openapi_deployment = os.getenv("AZURE_DEPLOYMENT_NAME", "").strip()
azureapi_key = os.getenv("AZURE_API_KEY", "").strip()

assert all([model_, openapi_base, openapi_version, openapi_deployment, azureapi_key]), "Missing environment variables!"

# Initialize model client
client = AzureOpenAIChatCompletionClient(
    azure_deployment=openapi_deployment,
    model=model_,
    api_version=openapi_version,
    azure_endpoint=openapi_base,
    api_key=azureapi_key,
)

# Initialize assistant agent
assistant_agent = AssistantAgent(
    name="sql_assistant",
    model_client=client,
    reflect_on_tool_use=True,
    system_message="You are a helpful SQL assistant.",
    model_client_stream=True,
)

# Generate SQL using the assistant
async def generate_sql(ctx):
    schema = load_schema(ctx)
    prompt = f"""
You are a SQL assistant. Based on the following schema and request, write a PostgreSQL SQL query.

Schema:
{schema}

User Request: {ctx.user_input}

SQL:
"""
    response = await assistant_agent.on_messages(
        messages=[TextMessage(content=prompt, source="user")],
        cancellation_token=CancellationToken(),
    )
    print(response,'kkk')
    # Extract the SQL query from the response
    sql_query = response.chat_message.content.strip()
    ctx.query = sql_query

    return ctx.query
