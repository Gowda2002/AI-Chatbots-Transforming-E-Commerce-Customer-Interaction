import sqlite3

def get_pending_queries():
    # Connect to the database
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    # Fetch pending queries
    cursor.execute("""
        SELECT id, question 
        FROM Queries 
        WHERE status = 'Pending'
    """)
    pending_queries = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Print the pending queries
    if pending_queries:
        print("Pending Queries:")
        for query in pending_queries:
            print(f"ID: {query[0]}, Question: {query[1]}")
    else:
        print("No pending queries found.")

# Call the function
get_pending_queries()
