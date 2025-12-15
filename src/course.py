from typing import List, TYPE_CHECKING
# TYPE_CHECKING is used here for clean import in a real file structure
if TYPE_CHECKING:
    from .hole import Hole  # Assuming you split Hole into its own file

"""
File: course.py

This module defines the data structure for a golf course mirroring the 
established JSON schema as defined in course.schema.json.

Imports are for:
1. Utilization of List of a certain object for holes parameter
2. Course uses Hole object

"""

class Course:
    """
    The Course class is the basic unit for the course. It is aligned with 
    course.schema.json which is found in /data/courses. 
    """
    def __init__(self, course_id: int, course_name: str, tees: str, 
                 course_side: str, location: str, rating: float, slope: int,
                 holes: List[Hole]):
        """
        Initializes a new Course object. This function mirrors the structure 
        of the course.schema.json file
        
        :param course_id: Serves as primary key and easy way to reference the
                          golf course. Eventually, this should be looked up in 
                          the database and use next available id.
        :param course_name: Name of the golf course.
        :param tees: Name of tees, usually a color, but not always.
        :param course_side: Front 9, Back 9, or All 18. Not positive this is 
                            needed. Perhaps this can be done programmatically 
                            where I can derive Front 9 and Back 9 from All 18.
        :param location: Geographic location of the golf course.
        :param rating: Rating of the golf course. 
        :param slope: Slope of the golf course.
        :param holes: 9 or 18 sized array of Hole objects.
        
        Note: Yardage and par for the course will be calculated from holes array
        
        """
        
        # The lines below must call the setters!
        self.course_id = course_id
        self.course_name = course_name
        self.tees = tees
        self.course_side = course_side
        self.location = location
        self.rating = rating
        self.slope = slope

        # Set holes to private variable
        self._holes = holes    

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
        MIN_LENGTH = 3
        if len(stripped_value) < MIN_LENGTH:
            raise ValueError(f"Course name must be at least {MIN_LENGTH} "
                             f"characters long. Received: {value}.")
        
        # Store the validated, stripped value
        self._course_name = stripped_value

    @property
    def course_side(self) -> str:
        return self._course_side

    @course_side.setter
    def course_side(self, value: str):
        """setter for course_side, validating it is 'Front', 'Back', or 'All'"""
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
    def slope(self) -> int:
        return self._slope
    
    @slope.setter
    def slope(self, value: int):
        """Setter for slope, with USGA validation (55-155)."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Slope must be an integer, received "
                            f"{type(value).__name__}.")
        
        # Validation Logic
        MIN_SLOPE = 55
        MAX_SLOPE = 155
        if not (MIN_SLOPE <= value <= MAX_SLOPE):
            raise ValueError(f"Slope must be between {MIN_SLOPE} and "
                             f"{MAX_SLOPE}. Received: {value}.")
        
        # Store the validated value in the internal variable
        self._slope = int(value)

    @property
    def rating(self) -> float:
        return self._rating

    @rating.setter
    def rating(self, value: float):
        """Setter for rating, which should be between 60.0 and 85.0"""
        if not isinstance(value, (float, int)):
            raise TypeError(f"Rating must be a float (decimal), received "
                            f"{type(value).__name__}.")
        
        # Validation Logic
        MIN_RATING = 60.0
        MAX_RATING = 85.0
        if not (MIN_RATING <= value <= MAX_RATING):
            raise ValueError(f"Rating must be between {MIN_RATING} and "
                             f"{MAX_RATING}. Received: {value}.")
        
        # Store the validated value in the internal variable
        self._rating = float(value)

    @property
    def yardage(self) -> int:
        """Calculates the total yardage based on distance in the holes array"""
        return sum(hole.distance for hole in self.holes)
    
    @property
    def par(self) -> int:
        """Calculates the total par based on par in the holes array"""
        return sum(hole.par for hole in self.holes)