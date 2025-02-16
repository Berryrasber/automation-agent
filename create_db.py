import sqlite3

# Connect to the database (creates file if it doesn’t exist)
conn = sqlite3.connect("data/ticket-sales.db")
cursor = conn.cursor()

# Create the tickets table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    units INTEGER,
    price REAL
)
""")

# Insert sample ticket data
cursor.executemany("INSERT INTO tickets (type, units, price) VALUES (?, ?, ?)", [
    ("Gold", 10, 50.0),  # 10 Gold tickets * $50 = $500
    ("Silver", 20, 30.0),  # Not needed for this task
    ("Gold", 5, 70.0)  # 5 Gold tickets * $70 = $350
])

conn.commit()
conn.close()

print("✅ Database created successfully with sample ticket data!")
