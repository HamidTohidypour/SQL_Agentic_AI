from prompts.sql_prompt import sql_prompt
from llm import llm

def generate_sql(state):
    chain = sql_prompt | llm
    sql = chain.invoke({
        "schema": state["schema"],
        "question": state["question"]
    })
    print (sql.strip())
    return {"sql": sql.strip()}