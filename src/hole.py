"""
File: hole.py

This module defines the data structure for a golf Hole to be used in Course 
object, mirroring the established JSON schema as defined in course.schema.json.
"""

class Hole:
    """
    The Hole class will represent a hole as observed on a golf course or on a
    scorecard.
    """
    def __init__(self, hole_number: int, yardage: int, par: int, 
                 handicap: int):
        """
        Initializes a Hole object representing a hole in the Course object.
        
        :param hole_number: Hole number on the course. This is unique and must 
                            be between 1-18.
        :param yardage: yardage in yards for this hole.
        :param par: The strokes required (or less than) to be considered par for 
                    the hole.
        :param handicap: The handicap rating for the hole indicating difficulty.
                         The lower the number, the harder the hole.
        """
        self.hole_number = hole_number # Calls the setter
        self.yardage = yardage # Calls the setter
        self.par = par # Calls the setter
        self.handicap = handicap # Calls the setter

    @property
    def hole_number(self) -> int:
        return self._hole_number
    
    @hole_number.setter
    def hole_number(self, value: int):
        """setter for hole_number, validating it is between 1-18"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Hole number must be an integer, received {type(value).__name__}.")
        
        # Validation Logic
        MIN_HOLE_NUMBER = 1
        MAX_HOLE_NUMBER = 18
        if not (MIN_HOLE_NUMBER <= value <= MAX_HOLE_NUMBER):
            raise ValueError(f"Hole number must be between {MIN_HOLE_NUMBER} and {MAX_HOLE_NUMBER}. Received: {value}")
        
        # Store the validated value in the internal variable
        self._hole_number = int(value)

    @property
    def yardage(self) -> int:
        return self._yardage
    
    @yardage.setter
    def yardage(self, value: int):
        """setter for yardage, validating it is between 3-6"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"yardage must be an integer, received {type(value).__name__}.")
        
        # Validation Logic
        MIN_YARDAGE = 50
        MAX_YARDAGE = 700
        if not (MIN_YARDAGE <= value <= MAX_YARDAGE):
            raise ValueError(f"yardage must be between {MIN_YARDAGE} and {MAX_YARDAGE}. Received: {value}")
        
        # Store the validated value in the internal variable
        self._yardage = int(value)
        
    @property
    def par(self) -> int:
        return self._par
    
    @par.setter
    def par(self, value: int):
        """setter for par, validating it is between 3-6"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Par must be an integer, received {type(value).__name__}.")
        
        # Validation Logic
        MIN_PAR = 3
        MAX_PAR = 6
        if not (MIN_PAR <= value <= MAX_PAR):
            raise ValueError(f"Par must be between {MIN_PAR} and {MAX_PAR}. Received: {value}")
        
        # Store the validated value in the internal variable
        self._par = int(value)

    @property
    def handicap(self) -> int:
        return self._handicap
    
    @handicap.setter
    def handicap(self, value: int):
        """setter for handicap, validating it is between 1-18"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Handicap must be an integer, received {type(value).__name__}.")
        
        # Validation Logic
        MIN_HANDICAP = 1
        MAX_HANDICAP = 18
        if not (MIN_HANDICAP <= value <= MAX_HANDICAP):
            raise ValueError(f"Handicap must be between {MIN_HANDICAP} and {MAX_HANDICAP}. Received: {value}")
        
        # Store the validated value in the internal variable
        self._handicap = int(value)
