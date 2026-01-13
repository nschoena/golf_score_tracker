import sys
from course import Course as C
from pathlib import Path

"""
Main entry point for the Golf Score Tracker application
"""

def main():
    """
    The main execution function.

    Returns:
        int: The exit code (0 for success).
    """
# TODO: Implement a menu system

    return 0

# setup pathing anchor
COURSE_BASE_PATH = Path(__file__).resolve().parent.parent / "data" / "courses"

# define the path to the course json file to load
file_to_load = COURSE_BASE_PATH / "hawley_white.json"
hawley_white = C.load_from_json(file_to_load)
# print(f"The total yardage for Hawley Golf Course White Tees is " 
    #   f"{hawley_white.yardage}")
print(hawley_white)

# --- Script Execution Block ---
if __name__ == "__main__":
    # Ensure a clean exit with the appropriate status code.
    sys.exit(main())