from typing import TypedDict, Optional

class State(TypedDict):
    question: str
    schema: str
    sql: str
    result: Optional[str]
    error: Optional[str]