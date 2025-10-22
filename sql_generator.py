"""
A small, dependency-free natural language to SQL generator for demo/testing.
This file is intentionally lightweight so it can run without external LLMs or APIs.

Usage:
    python sql_generator.py

It will print example conversions and allow a simple interactive prompt.
"""
import re
import sys

class SimpleSQLGenerator:
    """Convert a small set of natural language queries into SQL using rules and templates.

    This is not an LLM. It uses pattern matching for common query types.
    """

    def __init__(self):
        # Simple patterns -> handler mapping
        self.patterns = [
            (re.compile(r"list all (?P<table>\w+)s who earn more than (?P<number>\d+)", re.I), self._handle_greater_than),
            (re.compile(r"list all (?P<table>\w+)s", re.I), self._handle_select_all),
            (re.compile(r"get the names of (?P<table>\w+)s who have made purchases in the last (?P<days>\d+) days", re.I), self._handle_recent_purchases),
            (re.compile(r"find the total (?P<field>\w+) for this month", re.I), self._handle_sum_this_month),
        ]

    def generate(self, text: str) -> str:
        text = text.strip()
        if not text:
            return ""  # caller can decide how to handle empty input

        for pattern, handler in self.patterns:
            m = pattern.search(text)
            if m:
                try:
                    return handler(m)
                except Exception as e:
                    return f"-- Error generating SQL: {e}"

        # Fallback: try to heuristically map simple verbs/nouns
        return self._fallback(text)

    def _handle_greater_than(self, m: re.Match) -> str:
        table = m.group('table')
        number = m.group('number')
        # naive mapping: salary field for employees
        if table.lower() == 'employee' or table.lower() == 'employees':
            return f"SELECT * FROM employees WHERE salary > {number};"
        return f"SELECT * FROM {table}s WHERE value > {number};"

    def _handle_select_all(self, m: re.Match) -> str:
        table = m.group('table')
        return f"SELECT * FROM {table}s;"

    def _handle_recent_purchases(self, m: re.Match) -> str:
        table = m.group('table')
        days = m.group('days')
        # assume purchases stored in purchases or sales table
        table_name = table if table.endswith('s') else f"{table}s"
        return (f"SELECT name FROM {table_name} WHERE purchase_date >= "
                f"NOW() - INTERVAL '{days} days';")

    def _handle_sum_this_month(self, m: re.Match) -> str:
        field = m.group('field')
        return (f"SELECT SUM({field}) AS total_{field} FROM sales "
                f"WHERE MONTH(sale_date) = MONTH(CURRENT_DATE);")

    def _fallback(self, text: str) -> str:
        # very naive fallback: if contains 'count' return COUNT, if contains 'names' return name select
        if re.search(r"count", text, re.I):
            # try to extract noun
            noun = self._extract_noun(text) or 'items'
            return f"SELECT COUNT(*) FROM {noun};"
        if re.search(r"name|names", text, re.I):
            noun = self._extract_noun(text) or 'table'
            return f"SELECT name FROM {noun};"
        return "-- Sorry, I couldn't confidently generate SQL for that input."

    def _extract_noun(self, text: str) -> str:
        # rough heuristic: find the last noun-like token before keywords
        tokens = re.findall(r"\w+", text.lower())
        common = {'who','that','which','for','in','on','the','a','an','of','with','made','have','has','last','this'}
        for t in reversed(tokens):
            if t not in common and not t.isdigit():
                return t if t.endswith('s') else f"{t}s"
        return None


def _demo_examples(gen: SimpleSQLGenerator):
    examples = [
        "List all employees who earn more than 5000.",
        "Get the names of customers who have made purchases in the last 30 days.",
        "Find the total revenue for this month.",
        "Count users",
        "Show all orders",
    ]
    print("Demo: natural language -> SQL")
    print("------------------------------------")
    for ex in examples:
        sql = gen.generate(ex)
        print(f"NL: {ex}\nSQL: {sql}\n")


def _interactive_prompt(gen: SimpleSQLGenerator):
    print("Enter natural language queries and press Enter. Empty line to exit.")
    try:
        while True:
            text = input('> ').strip()
            if not text:
                break
            print(gen.generate(text))
    except (EOFError, KeyboardInterrupt):
        print('\nGoodbye')


if __name__ == '__main__':
    gen = SimpleSQLGenerator()
    # If a CLI argument is provided, generate for that
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(gen.generate(input_text))
    else:
        _demo_examples(gen)
        # then offer interactive prompt
        _interactive_prompt(gen)
