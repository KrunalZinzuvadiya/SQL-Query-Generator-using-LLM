"""Project version information and change tracking.

Changelog:
- 0.2.0: Added version components and changelog
- 0.1.0: Initial version
"""

VERSION = "0.2.0"
VERSION_TUPLE = (0, 2, 0)  # major, minor, patch


def get_version() -> str:
    """Return the current version string."""
    return VERSION


def get_version_tuple() -> tuple[int, int, int]:
    """Return version as (major, minor, patch) tuple."""
    return VERSION_TUPLE


def is_compatible_version(other_version: str) -> bool:
    """Check if other_version is compatible with current version.
    
    Compatible means same major version number (backward compatible changes only).
    """
    try:
        import re
        match = re.match(r"^(\d+)\.\d+\.\d+$", other_version)
        if not match:
            return False
        other_major = int(match.group(1))
        return other_major == VERSION_TUPLE[0]
    except (ValueError, IndexError):
        return False
