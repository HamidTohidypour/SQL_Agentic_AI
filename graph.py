from langgraph.graph import StateGraph, END
from state import State

from nodes.schema import select_schema
from nodes.generate_sql import generate_sql
from nodes.execute_sql import execute_sql
from nodes.fix_sql import fix_sql
from nodes.answer import generate_answer

builder = StateGraph(State)

builder.add_node("schema", select_schema)
builder.add_node("generate_sql", generate_sql)
builder.add_node("execute_sql", execute_sql)
builder.add_node("fix_sql", fix_sql)
builder.add_node("answer", generate_answer)

builder.set_entry_point("schema")

builder.add_edge("schema", "generate_sql")
builder.add_edge("generate_sql", "execute_sql")

def route(state):
    return "fix_sql" if state["error"] else "answer"

builder.add_conditional_edges(
    "execute_sql",
    route,
    {"fix_sql": "fix_sql", "answer": "answer"}
)

builder.add_edge("fix_sql", "execute_sql")
builder.add_edge("answer", END)

graph = builder.compile()