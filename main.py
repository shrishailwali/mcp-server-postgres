from fastapi import FastAPI, Request
from module.context import MCPContext
from module.nl2sql import generate_sql
from module.executor import execute_query

app = FastAPI()

@app.post("/mcp/query")
async def mcp_query(req: Request):
    body = await req.json()
    user_input = body.get("query")
    ctx = MCPContext(user_input)
    ctx.query = await generate_sql(ctx)
    execute_query(ctx)

    return {
        "sql": ctx.query,
        "results": ctx.result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)