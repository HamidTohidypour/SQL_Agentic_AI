from langchain_core.prompts import ChatPromptTemplate

fix_prompt = ChatPromptTemplate.from_template("""
The SQL query failed.

Schema:
{schema}

Original question:
{question}

Bad SQL:
{sql}

Error:
{error}

Fix the SQL query.
Return ONLY corrected SQL.
""")