from llm import llm
from prompts.fix_prompt import fix_prompt

def fix_sql(state):
    chain = fix_prompt | llm
    fixed_sql = chain.invoke(state)
    return {"sql": fixed_sql.strip()}