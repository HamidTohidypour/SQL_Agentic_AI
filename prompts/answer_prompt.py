from langchain_core.prompts import ChatPromptTemplate

answer_prompt = ChatPromptTemplate.from_template("""
Question:
{question}

SQL Result:
{result}

Provide a clear natural language answer.
""")