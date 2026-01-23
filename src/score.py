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
from datetime import date, datetime
from score_hole import ScoreHole

class Score:
    """
    The Score class is the basic unit for recording a score. It is aligned with 
    score.schema.json which is found in /data/scores.
    """
    def __init__(self, score_id: int, course_id: int, course_name: str, 
                 tees: str, course_side: str, date_played: date,  
                 holes_played: List[ScoreHole]):
        """
        Docstring for __init__
        
        :param score_id: Serves as primary key and easy way to reference the
            round played. Eventually, this should be looked up in the database 
            and use next available id.        
        :param course_id: ID for the course that was played. This will be a de
            facto foreign key relationship to courses.
        :param course_name: Name of the course.
            **Note** It will be redundant to have both course_id and course_name
            stored for the same score. Knowing one should lead to the other 
            because there will be a 1-1 relationship.
        :param tees: The name for the tees played. Typically a color, but can be 
            something else.
        :param course_side: Side of the course played. Allowed values based on 
            enum in course.schema.json are: Front, Back, All.
        :param date_played: Date the round was played. Must be in YYYY-MM-DD 
            format (IS0 8601)
        :param holes_played: Description

        Calculated values from holes_played array:
            round_score: Sum of strokes.

            Detailed (these will be calculated only if every ScoreHole has 
                is_detailed property.)
            round_putts: Sum of putts
            drive_accuracy: A three value float array representing tee shot accuracy. First value is for drives missing the fairway left, second value is fairways hit, and third value is drives missing the fairway right. Formula for each is (number of drives with that value/number of total drives). Number of total drives doesn't include Par 3s.
            gir_percent (Detailed): Calculation for number of greens hit in regulation based on gir property. Formula is: (Sum of Trues/Number of Holes played). 
        """
        # The lines below must call the setters!
        self.score_id = score_id
        self.course_id = course_id
        self.course_name = course_name
        self.tees = tees
        self.course_side = course_side
        self.date_played = date_played

    #
    # properties and setters
    #
       
    @property
    def score_id(self) -> int:
        return self._score_id
    
    @score_id.setter
    def score_id(self, value: int):
        """Setter for score_id. Eventually this will be a lookup to the 
        score database and incremented one from the max value currently 
        stored."""
        # Type check
        if not isinstance(value, (int, float)):
            raise TypeError(f"ScoreID must be a integer, received: "
                            f"{type(value).__name__}.")
        
        # Validation logic            
        if value < 0:
            raise ValueError(f"ScoreID must be a positive integer, " 
                                f"received: {value}")
        
        # Store the validated value in the internal variable
        self._score_id = int(value)

    @property
    def course_id(self) -> int:
        return self._course_id
    
    @course_id.setter
    def course_id(self, value: int):
        """Setter for course_id."""
        # Type check
        if not isinstance(value, (int, float)):
            raise TypeError(f"CourseD must be a integer, received: "
                            f"{type(value).__name__}.")
        
        # Validation logic
        # Eventually the validation would be done by a check to see if the 
        # course_id exists in the database of courses. Or, more likely, this
        # will be done away with because it is redundant to have both course_id
        # and course_name.            
        if value < 0:
            raise ValueError(f"CourseID must be a positive integer, " 
                                f"received: {value}")
        
        # Store the validated value in the internal variable
        self._course_id = int(value)

    @property
    def course_name(self) -> str:
        return self._course_name
    
    @course_name.setter
    def course_name(self, value: str):
        """setter for course name. Validates it's a string and at least 3 
        characters long"""
        if not isinstance(value, (str)):
            raise TypeError(f"Course name must be a string, received"
                            f" {type(value).__name__}.")

        # Strip the white space
        stripped_value = value.strip()

        # Validation Logic. String must be at least 3 characters long
        # Eventually the validation would be done by a check to see if the 
        # course_name exists in the database of courses. 
        MIN_LENGTH = 3
        if len(stripped_value) < MIN_LENGTH:
            raise ValueError(f"Course name must be at least {MIN_LENGTH} "
                             f"characters long. Received: {value}.")
        
        # Store the validated, stripped value
        self._course_name = stripped_value

    @property
    def tees(self) -> str:
        return self._tees
    
    @tees.setter
    def tees(self, value:str):
        """setter for tees. Type validation required. Validates it's a string 
        and at least 2 characters long"""
        # Type check
        if not isinstance(value, (str)):
            raise TypeError(f"Tees must be a string, received: "
                            f"{type(value).__name__}.")
        # Strip the white space
        stripped_value = value.strip()

        # Validation Logic. String must be at least 3 characters long
        MIN_LENGTH = 2
        if len(stripped_value) < MIN_LENGTH:
            raise ValueError(f"Tees name must be at least {MIN_LENGTH} "
                             f"characters long. Received: {value}.")
        
        # Store the validated, stripped value
        self._tees = stripped_value
    
    @property
    def course_side(self) -> str:
        return self._course_side

    @course_side.setter
    def course_side(self, value: str):
        """setter for course_side, validating it is 'Front', 'Back', or 'All'"""
        # Type check
        if not isinstance(value, (str)):
            raise TypeError(f"Course side must be a string, received "
                            f"{type(value).__name__}.")
        
        # Allowed values
        ALLOWED_SIDES = ['Front', 'Back', 'All']

        # Normalize the input to Title Case for case-insensitive validation
        normalized_value = value.capitalize()

        # Validation Logic
        if normalized_value not in ALLOWED_SIDES:
            raise ValueError(f"Course side must be one of "
                             f"{', '.join(ALLOWED_SIDES)}. Received: {value}.")
        
        # Store the validated value in the internal variable
        self._course_side = str(value)

    @property
    def date_played(self) -> date:
        return self._date_played
    
    @date_played.setter
    def date_played(self, value: str | date | datetime):
        """setter for date_played. Accepts either string or date. Will do type
        check, if it's a string, convert it to a date, and return a date."""
        # Type check
        if not isinstance(value, (str, date, datetime)):
            raise TypeError(f"Date played must be a string representing a date "
                            f"in YYYY-MM-DD format. Received: "
                            f"{type(value).__name__}.")
        
        # Validation logic
        # Check if it's already a datetime (this check must occur before date
        # check because datetime is a subclass of date class.) If so, store the 
        # value in the internal variable
        if isinstance(value, datetime):
            date_converted_value = value.date()
            self._date_played = date_converted_value 

        # Check if it's already a date. If so, store the value in the internal 
        # variable
        elif isinstance(value, date):
            self._date_played = value
        
        # The value is a string and must be converted to date type
        else:
            # Strip the white space
            stripped_value = value.strip()
            
            # Convert from string to date in a try/except block
            try:
                date_converted_value = date.fromisoformat(stripped_value)
            except: 
                raise ValueError(f"Date must be valid isoformat string "
                              f"(YYYY-MM-DD and valid values for YYYY, MM, DD)."
                              f" Received {stripped_value}")
            
            # Store the validated value in the internal variable
            self._date_played = date_converted_value

    @property
    def holes_played(self) -> List[ScoreHole]:
        return self._holes_played
    
    @holes_played.setter
    def holes_played(self, value: List[ScoreHole]):
        """Setter for holes_played array. Validate that all the objects passed 
        are objects of ScoreHole class."""
        # Type check to make sure holes is actually a list
        if not isinstance(value, List):
            raise TypeError(f"holes_played parameter must be a list. Received: "
                            f"{type(value).__name__}.")
        
        # Type check to make sure all objects in list are of Hole type
        for h in value:
            if not isinstance(h, ScoreHole):
                raise TypeError(f"elements in holes_played list must be of "
                                f"ScoreHole type. "
                                f"Received {type(h).__name__}.")

        # Store the validated list in the internal variable
        self._holes_played = value