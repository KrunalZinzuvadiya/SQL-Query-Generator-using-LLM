"""Small utility helpers used by demo scripts.

This module contains tiny helpers intended for examples and CI-free demos.
"""

from __future__ import annotations

import re


def normalize_table_name(name: str) -> str:
    """Return a safe, lowercased table name.

    Rules (small and predictable):
    - Return empty string for falsy input.
    - Strip punctuation from the start and end of the string.
    - Collapse internal whitespace to a single underscore.
    - Lowercase the result.

    Examples:
        "Employees" -> "employees"
        " Customers " -> "customers"
        "orders!" -> "orders"
        "monthly sales" -> "monthly_sales"
    """
    if not name:
        return ""

    # Trim surrounding punctuation/whitespace
    cleaned = re.sub(r"^[^\w]+|[^\w]+$", "", name.strip())

    # Replace any run of whitespace with a single underscore
    cleaned = re.sub(r"\s+", "_", cleaned)

    return cleaned.lower()
