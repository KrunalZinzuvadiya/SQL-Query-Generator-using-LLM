"""Tiny demo that shows table name normalization and version info."""
from mini_utils import normalize_table_name
from version import get_version, get_version_tuple, is_compatible_version


def demo_table_names():
    """Show table name normalization examples."""
    print("\nTable Name Normalization:")
    print("-" * 25)
    examples = ["Employees", " Customers ", "orders!", "#Sales"]
    for e in examples:
        print(f"{repr(e):20} -> {normalize_table_name(e)}")


def demo_version_info():
    """Show version compatibility examples."""
    print("\nVersion Information:")
    print("-" * 25)
    current = get_version()
    print(f"Current version: {current}")
    print(f"Version tuple: {get_version_tuple()}")
    
    test_versions = ["0.2.1", "0.2.0", "1.0.0", "0.1.9", "invalid"]
    print("\nCompatibility Check:")
    for v in test_versions:
        result = "✓" if is_compatible_version(v) else "✗"
        print(f"Compatible with {v:8} -> {result}")


def main():
    """Run all demos."""
    print("=== Mini Demo ===")
    demo_table_names()
    demo_version_info()


if __name__ == '__main__':
    main()
