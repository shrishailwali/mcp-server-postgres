from db import get_connection

def load_schema(ctx):
    if ctx.schema:
        return ctx.schema

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    tables = cur.fetchall()

    schema_info = ""
    for (table_name,) in tables:
        cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")
        columns = cur.fetchall()
        schema_info += f"Table: {table_name}\n"
        for col in columns:
            schema_info += f" - {col[0]} ({col[1]})\n"
        schema_info += "\n"

    conn.close()
    ctx.schema = schema_info
    return ctx.schema
