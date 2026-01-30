"""
File: scorecard.py

This module is used to display the scorecard. The Scorecard class will take
a Course and a Score object and display the entire scorecard.
"""
import json
from pathlib import Path
from typing import List, TYPE_CHECKING
from datetime import date, datetime
import score
import score_hole
import course 
import hole

class ScoreCard:
    """
    This will be the class that will be used to combine the score and course
    information. This will allow additional analysis like strokes/putts average, 
    driving accuracy, GIR % per Par 3/4/5
    """
    def __init__(self, course_played: Course):
        pass