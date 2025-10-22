"""Tiny demo that uses mini_utils.normalize_table_name."""
from mini_utils import normalize_table_name


def main():
    examples = ["Employees", " Customers ", "orders!", "#Sales"]
    for e in examples:
        print(f"{repr(e)} -> {normalize_table_name(e)}")


if __name__ == '__main__':
    main()
