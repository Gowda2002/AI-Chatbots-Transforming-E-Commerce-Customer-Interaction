import sqlite3

def delete_duplicate_queries():
    # Connect to the database
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    # Step 1: Identify and retrieve all the queries that appear more than once in the Solutions table
    cursor.execute("""
        SELECT question, COUNT(*)
        FROM Solutions
        GROUP BY question
        HAVING COUNT(*) > 1
    """)
    
    duplicate_queries = cursor.fetchall()

    # Step 2: For each duplicate query, remove the duplicates, keeping only one
    for query, _ in duplicate_queries:
        cursor.execute("""
            DELETE FROM Solutions
            WHERE question = ? AND rowid NOT IN (
                SELECT MIN(rowid) FROM Solutions WHERE question = ?
            )
        """, (query, query))
        conn.commit()

    # Step 3: Close the connection
    conn.close()
    
    print("Duplicate queries and answers have been deleted.")

# Call the function
delete_duplicate_queries()
