"""
File: score.py

This module defines the data structure for a score, mirroring the established
JSON schema as defined in score.schema.json.

Imports are for:
1. Utilization of List of a certain object for holes parameter
2. Score uses ScoreHole object

"""
import json
from pathlib import Path
from typing import List, TYPE_CHECKING
from datetime import date
from score_hole import ScoreHole

class Score:
    """
    The Score class is the basic unit for recording a score. It is aligned with 
    score.schema.json which is found in /data/scores.
    """
    def __init__(self, score_id: int, course_id: int, course_name: str, 
                 tees: str, course_side: str, date_played: date, 
                 round_score: int, gir_percent: float, 
                 tee_accuracy: List[float], holes_played: List[ScoreHole]):
        