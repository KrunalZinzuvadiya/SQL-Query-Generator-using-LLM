# SQL-Query-Generator-using-LLM

## Overview
This project enables users to translate natural language queries into SQL statements using Cohere's NLP model. With a simple graphical interface built in Tkinter, users can input queries in plain English, and the tool generates syntactically correct SQL code for various database operations.

## Features
- **Natural Language to SQL Translation**: Converts user queries into SQL statements.
- **GUI Interface**: Easy-to-use interface built with Tkinter.
- **Cohere Integration**: Uses Cohere's API for natural language processing.
- **Real-Time Query Generation**: Get instant SQL code based on your input.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/natural-language-to-sql.git
   cd natural-language-to-sql
   ```
Requirements  
```
Python 3.x
Cohere Python SDK
Tkinter (comes pre-installed with Python)
```
Usage  
```
Launch the application.
Enter a query in plain English (e.g., "List all employees who earn more than 5000").
The tool will generate and display the corresponding SQL query.
```

Example
Input
```
List all employees who joined after January 2022.
```
Output
```
SELECT * FROM employees WHERE join_date > '2022-01-01';
```

Acknowledgments

    Cohere for their powerful NLP capabilities.
    Python and its robust libraries for building this tool.

Author  
Krunal  
