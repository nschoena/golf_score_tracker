import sys
from course import Course as C
from score import Score as S
from pathlib import Path
from datetime import date, datetime

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

# setup pathing anchor for courses and scores
COURSE_BASE_PATH = Path(__file__).resolve().parent.parent / "data" / "courses"
SCORE_BASE_PATH = Path(__file__).resolve().parent.parent / "data" / "scores"

# Hawley test
# define the path to the course json file to load
course_file_to_load = COURSE_BASE_PATH / "hawley_white.json"
# load the json file into course object
hawley_white = C.load_from_json(course_file_to_load)
# display the course info
hawley_white.display_course_info()

# Hawley test
# define the path to the course json file to load
course_file_to_load = COURSE_BASE_PATH / "village_green_white.json"
# load the json file into course object
village_green_white = C.load_from_json(course_file_to_load)
# display the course info
village_green_white.display_course_info()

# score test
# 20251004_village_green_white test
# define the path to the course json file to load
score_file_to_load = SCORE_BASE_PATH / "20251004_village_green_white.json"

# load the json file into score object
village_green_white_20251004_score = S.load_from_json(score_file_to_load)

# use print statement to confirm the information in the score object is valid
print(village_green_white_20251004_score)

# In main.py, after loading your score:
for sh in village_green_white_20251004_score.holes_played:
    print(sh)

# --- Script Execution Block ---
if __name__ == "__main__":
    # Ensure a clean exit with the appropriate status code.
    sys.exit(main())