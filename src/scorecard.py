"""
File: scorecard.py

This module is used to display the scorecard. The Scorecard class will take
a Course and a Score object and display the entire scorecard.

Imports are for:
1. Utilization of List of a certain object for holes parameter
2. Score uses ScoreHole object

"""
import json
from pathlib import Path
from typing import List, TYPE_CHECKING
from datetime import date, datetime
from score_hole import ScoreHole