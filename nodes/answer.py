from llm import llm
from prompts.answer_prompt import answer_prompt

def generate_answer(state):
    chain = answer_prompt | llm
    answer = chain.invoke({
        "question": state["question"],
        "result": state["result"]
    })
    return {"result": answer}