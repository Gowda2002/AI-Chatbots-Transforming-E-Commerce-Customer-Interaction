import sqlite3

def insert_multiple_solutions(solutions):
    # Connect to the database
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    # Insert each solution into the database
    cursor.executemany("""
        INSERT INTO Solutions (question, answer)
        VALUES (?, ?)
    """, solutions)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    print(f"{len(solutions)} solutions inserted successfully.")

# Replace the following list with your data
solutions = [
    ("What is your refund policy?", "Our refund policy allows returns within 30 days of purchase."),
    ("How can I track my order?", "You can track your order using the tracking link in your email."),
    ("What payment methods do you accept?", "We accept credit cards, PayPal, and other payment methods."),
    ("How do I contact customer support?", "You can contact us via email or our helpline."),
    ("Where are you located?", "We are located in New York City."),
    ("Do you ship internationally?", "Yes, we ship to most countries worldwide."),
    ("What are your working hours?", "Our working hours are 9 AM to 5 PM, Monday to Friday."),
    ("How do I reset my password?", "To reset your password, click on 'Forgot Password' on the login page."),
    ("What is your return policy?", "You can return items within 30 days with proof of purchase."),
    ("How do I cancel my order?", "To cancel your order, please contact customer support."),
    ("Do you offer discounts?", "We offer seasonal discounts and promotions."),
    ("How can I update my account details?", "You can update your account details in the 'My Account' section."),
    ("Is my data secure?", "Yes, we adhere to strict data security standards."),
    ("Can I change my delivery address?", "You can change your delivery address before the order is shipped."),
    ("What is the warranty on your products?", "Our products come with a 1-year warranty.")
]


insert_multiple_solutions(solutions)
