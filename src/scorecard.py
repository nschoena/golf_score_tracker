"""
File: scorecard.py

This module is used to display the scorecard. The Scorecard class will take
a Course and a Score object and display the entire scorecard. It will also allow
for advanced analytics on the score because there will be a direct relationship
between the score and the course where it was played.
"""
import json
from pathlib import Path
from typing import List, TYPE_CHECKING
from datetime import date, datetime
from course import *
from score import *

class ScoreCard:
    """
    This will be the class that will be used to combine the score and course
    information. This will allow additional analysis like strokes/putts average, 
    driving accuracy, GIR % per Par 3/4/5
    """
    def __init__(self, course: Course, score: Score):
        """
        :param course_played: the course where the round was played
        :type course_played: Course
        :param score: the score for the round played
        :type score: Score
        """
        self.course = course
        self.score = score

    @property
    def course(self) -> Course:
        return self._course
    
    @course.setter
    def course(self, value: Course):
        """setter for course object, validate that the parameter is a Course 
        object"""
        if not isinstance(value, Course): 
            raise TypeError(f"Parameter must be Course object, received {type(value).__name__}.")
        
        # Store the validated value in the internal variable
        self._course = value

    @property
    def score(self) -> Score:
        return self._score
    
    @score.setter
    def score(self, value: Score):
        """setter for score object, validate that the parameter is a Score 
        object"""
        if not isinstance(value, Score): 
            raise TypeError(f"Parameter must be Score object, received {type(value).__name__}.")
        
        # Store the validated value in the internal variable
        self._score = value

    #
    # Class methods
    #
    @classmethod
    def load_scorecard(cls, course: Course, score: Score):
        """Reads the course and score objects and creates a ScoreCard object"""
        # Load the course
        course = course

        # Load the score
        score = score

        # Return the ScoreCard object
        return cls(
            course=course,
            score=score
        ) 
    
    #
    # instance methods - display
    # 
    def display_scorecard(self):
        """
        Display the scorecard with course and score data.
        Needs to handle is_detailed score property
        """
        self.course.display_course_info()
        self.score.display_score_info()