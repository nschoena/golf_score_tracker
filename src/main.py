import sys
from course import Course
from score import Score
from pathlib import Path
from datetime import date, datetime
from scorecard import ScoreCard

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

# Village Green 
# define the path to the course json file to load and load it
course_file_to_load = COURSE_BASE_PATH / "village_green_white.json"
village_green_white_course = Course.load_from_json(course_file_to_load)

# define the path to the score json file to load and load it
score_file_to_load = SCORE_BASE_PATH / "20251004_village_green_white.json"
village_green_white_20251004_score = Score.load_from_json(score_file_to_load)

# Use ScoreCard class to display the scorecard and additional analytics
score = ScoreCard.load_scorecard(village_green_white_course, village_green_white_20251004_score)
score.display_scorecard()

# --- Script Execution Block ---
if __name__ == "__main__":
    # Ensure a clean exit with the appropriate status code.
    sys.exit(main())