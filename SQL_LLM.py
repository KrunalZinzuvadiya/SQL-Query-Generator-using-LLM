import tkinter as tk
from tkinter import messagebox, scrolledtext

# Try to import Cohere, but don't fail if it's not installed/configured.
try:
    import cohere  # type: ignore
except Exception:
    cohere = None

# Configure your Cohere API key (set to None to use local fallback)
COHERE_API_KEY = None

# Initialize Cohere client if available and configured
cohere_client = None
if cohere is not None and COHERE_API_KEY:
    try:
        cohere_client = cohere.Client(COHERE_API_KEY)
    except Exception:
        cohere_client = None

# Import local rule-based generator as a fallback
from sql_generator import SimpleSQLGenerator


def generate_sql_query(natural_language_input):
    """Generate SQL from natural language using Cohere if available, otherwise fallback.

    This keeps the GUI usable even when no API key or model is configured.
    """
    # If we have a working cohere client, use it.
    if cohere_client is not None:
        prompt = f"""
You are an SQL expert. Convert the following natural language queries into SQL queries. Be precise and ensure proper SQL syntax. Assume a general database schema.

Examples:
1. "List all employees who earn more than 5000."
SQL: SELECT * FROM employees WHERE salary > 5000;

2. "Get the names of customers who have made purchases in the last 30 days."
SQL: SELECT name FROM customers WHERE purchase_date >= NOW() - INTERVAL '30 days';

3. "Find the total revenue for this month."
SQL: SELECT SUM(revenue) AS total_revenue FROM sales WHERE MONTH(sale_date) = MONTH(CURRENT_DATE);

Natural language query: {natural_language_input}
SQL:
"""
        response = cohere_client.generate(
            model="command-xlarge-nightly",
            prompt=prompt,
            max_tokens=100
        )
        sql_query = response.generations[0].text.strip()
        return sql_query

    # Otherwise, use local SimpleSQLGenerator fallback
    gen = SimpleSQLGenerator()
    return gen.generate(natural_language_input)

# Function to handle user query
def handle_query():
    user_input = user_query.get()
    if not user_input.strip():
        messagebox.showerror("Input Error", "Please enter a query.")
        return

    # Append user input to conversation history
    conversation.insert(tk.END, f"You: {user_input}\n\n")
    user_query.delete(0, tk.END)

    # Generate SQL query
    sql_query = generate_sql_query(user_input)
    conversation.insert(tk.END, f"Bot (Generated SQL): {sql_query}\n\n")

# Create the main tkinter application
root = tk.Tk()
root.title("Natural Language to SQL Query Generator")

# Chat conversation history
conversation = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, state=tk.NORMAL)
conversation.pack(pady=10)
conversation.insert(tk.END, "Bot: Hi! How can I assist you with SQL queries today?\n\n")

# User input field
user_query = tk.Entry(root, width=50)
user_query.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Send", command=handle_query)
submit_button.pack(pady=10)

# Run the tkinter main loop
root.mainloop()
