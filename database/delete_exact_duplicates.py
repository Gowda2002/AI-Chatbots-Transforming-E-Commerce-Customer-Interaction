import sqlite3

def delete_exact_duplicates():
    # Connect to the database
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    # Step 1: Find all duplicate (question, answer) pairs
    cursor.execute("""
        SELECT question, answer, COUNT(*)
        FROM Solutions
        GROUP BY question, answer
        HAVING COUNT(*) > 1
    """)
    
    duplicate_pairs = cursor.fetchall()

    # Step 2: For each duplicate pair, keep only one entry and delete others
    for question, answer, _ in duplicate_pairs:
        cursor.execute("""
            DELETE FROM Solutions
            WHERE question = ? AND answer = ? AND rowid NOT IN (
                SELECT MIN(rowid) FROM Solutions WHERE question = ? AND answer = ?
            )
        """, (question, answer, question, answer))
        conn.commit()

    # Step 3: Close the connection
    conn.close()
    
    print("Exact duplicate queries and answers have been deleted.")

# Call the function
delete_exact_duplicates()
