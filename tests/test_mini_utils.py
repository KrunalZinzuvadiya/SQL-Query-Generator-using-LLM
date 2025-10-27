import pytest

from mini_utils import normalize_table_name


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("Employees", "employees"),
        (" Customers ", "customers"),
        ("orders!", "orders"),
        ("monthly sales", "monthly_sales"),
        ("  Leading and   multiple   spaces ", "leading_and_multiple_spaces"),
        ("***weird-table***", "weird-table"),
        ("", ""),
        (None, ""),
    ],
)
def test_normalize_table_name(input_text, expected):
    assert normalize_table_name(input_text) == expected


def test_normalize_preserves_words():
    # ensure words remain and punctuation trimmed
    assert normalize_table_name("#Sales2025!") == "sales2025"
