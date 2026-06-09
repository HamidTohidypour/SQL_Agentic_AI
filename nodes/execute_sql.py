from db.database import run_sql

def execute_sql(state):
    try:
        result = run_sql(state["sql"])
        return {"result": str(result), "error": None}
    except Exception as e:
        return {"result": None, "error": str(e)}