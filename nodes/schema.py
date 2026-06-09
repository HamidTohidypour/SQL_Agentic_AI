from state import State
def select_schema(state: State):
    schema = """
    Tables:
    employees(id, name, salary, department_id)
    departments(id, name)
    """
    return {"schema": schema}