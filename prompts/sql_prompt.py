from langchain_core.prompts import ChatPromptTemplate

sql_prompt = ChatPromptTemplate.from_template("""
You are an expert SQL generator.

Schema:
{schema}

Question:
{question}

Generate ONLY SQL query.
""")