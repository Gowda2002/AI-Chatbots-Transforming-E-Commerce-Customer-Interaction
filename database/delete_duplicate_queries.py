import sqlite3

def delete_duplicate_queries():
    # Connect to the database
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    # Query to find duplicate queries based on the 'question' field
    cursor.execute("""
        SELECT question, COUNT(*) 
        FROM Queries
        GROUP BY question
        HAVING COUNT(*) > 1;
    """)
    duplicates = cursor.fetchall()

    # Loop through the duplicates and delete them
    for duplicate in duplicates:
        question = duplicate[0]

        # Delete all but the first occurrence of each duplicate query
        cursor.execute("""
            DELETE FROM Queries
            WHERE id NOT IN (
                SELECT MIN(id)
                FROM Queries
                WHERE question = ?
            )
            AND question = ?;
        """, (question, question))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Duplicate queries deleted successfully.")

# Run the function
delete_duplicate_queries()
