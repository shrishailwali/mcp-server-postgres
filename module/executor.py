from db import get_connection

def execute_query(ctx):
    print("Original query:", ctx.query, '← query input')

    # Sanitize the query if wrapped in Markdown-style backticks
    query = ctx.query.strip()
    if query.startswith("```sql") and query.endswith("```"):
        query = query[6:-3].strip()
    elif query.startswith("```") and query.endswith("```"):
        query = query[3:-3].strip()

    print("Sanitized query:", query, '← after cleanup')

    conn = get_connection()
    cur = conn.cursor()
    print("Cursor and Connection:", cur, conn, '← connection debug')

    try:
        cur.execute(query)
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        ctx.result = [dict(zip(columns, row)) for row in rows]
        return ctx.result
    finally:
        conn.close()

