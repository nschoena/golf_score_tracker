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
    # instance methods 
    # 
    # display
    def display_scorecard(self):
        """
        Display the scorecard with course and score data.
        Needs to handle is_detailed score property
        """
        self.course.display_course_info()
        self.score.display_score_info()

    # analytics
    def calc_par_averages_brute_force(self):
        """
        calculate the scoring average per hole par type
        """

        # determine CourseHoles that are par 3s/4s/5s, cataloguing hole numbers
        # create empty array to store the hole numbers for each par
        par3_hole_numbers = []
        par4_hole_numbers = []
        par5_hole_numbers = []

        # iterate through each hole in course_holes and check the par. Assign
        # the hole number to the appropriate par*_hole_numbers array
        for ch in self.course.course_holes:
            if ch.par == 3:
                par3_hole_numbers.append(ch.hole_number)
            elif ch.par == 4:
                par4_hole_numbers.append(ch.hole_number)
            elif ch.par == 5:
                par5_hole_numbers.append(ch.hole_number)
            else:
                continue

        # print the hole numbers
        print(f"Par 3s are: {par3_hole_numbers}")
        print(f"Par 4s are: {par4_hole_numbers}")
        print(f"Par 5s are: {par5_hole_numbers}")
            
        # determine ScoreHoles that correspond to those hole numbers and 
        # calculate the average for par3s
        par3_scores = []
        for hole_num in par3_hole_numbers:
            hole_score = self.score.holes_played[hole_num-1]
            par3_scores.append(hole_score.strokes)

        avg_par3 = sum(par3_scores) / len(par3_scores) if par3_scores else 0

        print(f"Par 3 average: {avg_par3:.2f}")

        # calculate the average for par3s
        par4_scores = []
        for hole_num in par4_hole_numbers:
            hole_score = self.score.holes_played[hole_num-1]
            par4_scores.append(hole_score.strokes)

        avg_par4 = sum(par4_scores) / len(par4_scores) if par4_scores else 0

        print(f"Par 4 average: {avg_par4:.2f}")

        # calculate the average for par3s
        par5_scores = []
        for hole_num in par5_hole_numbers:
            hole_score = self.score.holes_played[hole_num-1]
            par5_scores.append(hole_score.strokes)

        avg_par5 = sum(par5_scores) / len(par5_scores) if par5_scores else 0

        print(f"Par 5 average: {avg_par5:.2f}")

    def calc_par_averages(self):
        """Calculate score averages for each par num"""
        #
        # Pythonic way
        #
        # Dictionaries are great for grouping these stats
        pars = {3: [], 4: [], 5: []}

        # Zip aligns course data with score data perfectly
        for ch, sh in zip(self.course.course_holes, self.score.holes_played):
            if ch.par in pars:
                pars[ch.par].append(sh.strokes)

        # Calculate and print averages
        for par_val, scores in pars.items():
            if scores:
                avg = sum(scores) / len(scores)
                print(f"Par {par_val} Average: {avg:.2f}")
            else:
                print(f"Par {par_val} Average: N/A")

    #TODO: Do the same averages calculations for GIRs
    #      Average score (per par value) for drives that hit the fairway 
    #      compared to drives that did not.