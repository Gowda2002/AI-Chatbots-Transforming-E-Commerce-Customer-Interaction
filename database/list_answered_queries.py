import sqlite3

# Connect to the database
conn = sqlite3.connect('chatbot.db')
cursor = conn.cursor()

# Query to fetch answered queries
cursor.execute("""
    SELECT id, question, response, status 
    FROM Queries 
    WHERE status = 'Answered';
""")

# Fetch all results
answered_queries = cursor.fetchall()

# Display the results
if answered_queries:
    print("Answered Queries:")
    for query in answered_queries:
        print(f"ID: {query[0]}, Question: {query[1]}, Response: {query[2]}, Status: {query[3]}")
else:
    print("No answered queries found.")

# Close the connection
conn.close()
