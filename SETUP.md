# SQL Query Generator using LLM - Setup Guide

This guide will help you set up and run the SQL Query Generator project that uses Large Language Models.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/KrunalZinzuvadiya/SQL-Query-Generator-using-LLM.git
   cd SQL-Query-Generator-using-LLM
   ```

2. Set up a virtual environment (recommended):

   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Linux/macOS
   source venv/bin/activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Make sure you have your LLM API keys properly configured (if required)
2. Configure your database connection settings in the appropriate configuration file

## Running the Application

## Running the Application

To run the SQL Query Generator (Tkinter UI):

```powershell
python .\SQL_LLM.py
```

There are small demo scripts included that are dependency-free and useful for quick checks:

- `sql_generator.py` — rule-based NL->SQL demo (prints examples and offers a prompt)
- `mini_demo.py` — tiny demos for utilities and version info

To run those:

```powershell
python .\sql_generator.py
python .\mini_demo.py
```

## Local LLM fallback

The GUI in `SQL_LLM.py` will try to use Cohere if `COHERE_API_KEY` is set and the Cohere package is available.
If not configured, it falls back to a small local rule-based generator (`sql_generator.py`). This lets you try the UI and demos without an external API key.

## Project Structure

```
SQL-Query-Generator-using-LLM/
├── SQL_LLM.py         # Main application file
├── README.md          # Project overview and documentation
└── SETUP.md          # Setup instructions (this file)
```

## Troubleshooting

If you encounter any issues during setup:

1. Ensure all prerequisites are properly installed
2. Verify that your Python environment is correctly configured
3. Check that all required dependencies are installed

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request with your changes

## Support

If you need help or have questions, please open an issue on the GitHub repository.
