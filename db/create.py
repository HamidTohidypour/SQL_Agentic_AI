import sqlite3

# Create/connect DB file
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# -------------------------
# Drop tables if exist
# -------------------------
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")

# -------------------------
# Create tables
# -------------------------
cursor.execute("""
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER,
    department_id INTEGER,
    FOREIGN KEY(department_id) REFERENCES departments(id)
)
""")

# -------------------------
# Insert sample data
# -------------------------
departments = [
    (1, "Engineering"),
    (2, "HR"),
    (3, "Sales")
]

employees = [
    (1, "Alice", 120000, 1),
    (2, "Bob", 90000, 1),
    (3, "Charlie", 70000, 2),
    (4, "David", 65000, 3),
    (5, "Eve", 110000, 1)
]

cursor.executemany("INSERT INTO departments VALUES (?, ?)", departments)
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees)

conn.commit()
conn.close()

print("Database created successfully: example.db")