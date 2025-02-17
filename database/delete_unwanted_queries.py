import sqlite3

def delete_unwanted_queries(keyword=None, status=None):
    # Connect to the database
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    # Build the SQL DELETE query based on given conditions
    if keyword:
        cursor.execute("""
            DELETE FROM Queries
            WHERE question LIKE ?
        """, (f"%{keyword}%",))
    
    if status:
        cursor.execute("""
            DELETE FROM Queries
            WHERE status = ?
        """, (status,))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print("Unwanted queries deleted successfully.")

# Example usage:
# To delete queries with "unwanted" in the question
delete_unwanted_queries(keyword="unwanted")

# To delete queries with "Pending" status
delete_unwanted_queries(status="Pending")
