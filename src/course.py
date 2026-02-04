"""
File: course.py

This module defines the data structure for a golf course mirroring the 
established JSON schema as defined in course.schema.json.

Classes defined:
- CourseHole: defines what a hole is as used in the Course class
- Course: defines the components and methods of the golf course

"""
import json
from pathlib import Path
from typing import List, TYPE_CHECKING

class CourseHole:
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

class Course:
    """
    The Course class is the basic unit for the course. It is aligned with 
    course.schema.json which is found in /data/courses. 
    """
    def __init__(self, course_id: int, course_name: str, tees: str, 
                 course_side: str, location: str, rating: float, slope: int,
                 course_holes: List[CourseHole]):
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
        :param holes: 9 or 18 sized array of CourseHole objects.
        
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
        self.course_holes = course_holes    

    # Used for testing before the display function is written
    def __str__(self) -> str:
        """Print a human-readable summary of the course"""
        return (
            f"{self.course_name.title()} is a Par {self.par} course in "
            f"{self.location} and is {self.yardage} yards long."
        )

    @property
    def course_id(self) -> int:
        return self._course_id
    
    @course_id.setter
    def course_id(self, value: int):
        """Setter for course_id. Eventually this will be a lookup to the course
            database and incremented one from the max value currently 
            stored."""
        # Type check
        if not isinstance(value, (int, float)):
            raise TypeError(f"ScoreID must be a integer, received: "
                            f"{type(value).__name__}.")
        
        # Validation logic                    
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
    def course_holes(self) -> List[CourseHole]:
        return self._course_holes
    
    @course_holes.setter
    def course_holes(self, value: List[CourseHole]):
        """Setter for holes array. Validate that all the objects passed are
        actually objects of Hole class."""
        # Type check to make sure holes is actually a list
        if not isinstance(value, List):
            raise TypeError(f"holes parameter must be a list. Received: "
                            f"{type(value).__name__}.")
        
        # Type check to make sure all objects in list are of Hole type
        for ch in value:
            if not isinstance(ch, CourseHole):
                raise TypeError(f"elements in holes list must be of hole type. "
                                f"Received {type(ch).__name__}.")

        # Store the validated list in the internal variable
        self._course_holes = value

    # Calculated properties
    @property
    def yardage(self) -> int:
        """Calculates the total yardage based on yardage in the holes array"""
        return sum(course_hole.yardage for course_hole in self._course_holes)
    
    @property
    def par(self) -> int:
        """Calculates the total par based on par in the holes array"""
        return sum(hole.par for hole in self._course_holes)
    
    # Class methods
    @classmethod
    def load_from_json(cls, filepath: str | Path):
        """Reads a JSON file and returns a new Course instance"""
        # Load the course data json file and deserialize into raw_data
        with open(filepath, 'r') as file:
            raw_data = json.load(file)

        # Create empty array to store hole objects
        course_hole_objects = []

        # iterate through the hole info in the dictionary and create a hole
        # object. On each loop, append the newly created hole to the 
        # hole_objects array.
        for hole_dict in raw_data['holes']:
            # 1. Create a Hole instance 'h' by passing in data from hole_dict
            ch = CourseHole(
                hole_number=hole_dict['holeNumber'],
                yardage=hole_dict['yardage'],
                par=hole_dict['par'],
                handicap=hole_dict['handicap']                
            )            
            # 2. Append 'h' to the hole_objects list
            course_hole_objects.append(ch)

        # assign the courseId property. Eventually this will be an identity 
        # field that will read the highest courseId from the database and 
        # increment by one
        course_id = raw_data['courseId']

        # assign the courseName property
        course_name = raw_data['courseName']

        # assign the tees property
        tees = raw_data['tees']

        # assign the courseSide property
        course_side = raw_data['courseSide']

        # assign the location property
        location = raw_data['location']

        # assign the rating property
        rating = raw_data['rating']

        # assign the slope property
        slope = raw_data['slope']

        # assign the yardage property. This is calculated based on the sum of
        # the yardages in the hole_objects array.
        yardage = sum(course_hole.yardage for course_hole in course_hole_objects)        

        # assign the par property. This is calculated based on the sum of
        # the par in the hole_objects array.
        par = sum(course_hole.par for course_hole in course_hole_objects) 

        # return the course class object
        # note:  that yardage and par are currently not part of the class but 
        # will be calculated when retrieved.
        
        return cls(
            course_id=course_id,
            course_name=course_name,
            tees=tees,
            course_side=course_side,
            location=location,
            rating=rating,
            slope=slope,
            course_holes=course_hole_objects
        )
    
    def display_score_horizontal_lines(self):
        """Display the hole numbers"""
        # Set the column width to use in the display
        LABEL_WIDTH = 9
        COL_WIDTH = 4
        SUMMARY_WIDTH = 5
        TOTAL_WIDTH = (LABEL_WIDTH + 1) + (18 * (COL_WIDTH + 1)) + (3 * (SUMMARY_WIDTH + 2))
        print("-" * TOTAL_WIDTH)
    
    def display_course_header(self):
        """Displays course header info for the scorecard"""        
        self.display_score_horizontal_lines()
        print(f"{self.course_name}")
        print(f"{self.location}")
        print(f"Rating: {self.rating}")
        print(f"{'Slope:':7} {self.slope}")
        print(f"Yardage: {self.yardage}")
        print(f"Par: {self.par}")
        self.display_score_horizontal_lines()
    
    def display_course_hole_number(self):
        """Display the hole numbers"""
        # Set the column width to use in the display
        LABEL_WIDTH = 9
        COL_WIDTH = 4
        SUMMARY_WIDTH = 5
        
        # Define front_nine, back_nine because I need to break them up to 
        # display OUT/IN/TOT
        front_nine = self._course_holes[:9]
        back_nine = self._course_holes[9:18]

        # print the Holes for first 9, OUT, back 9, IN, and TOT
        print(f"{'HOLE':{LABEL_WIDTH}}", end="|")

        for course_hole in front_nine:
            print(f"{course_hole.hole_number:{COL_WIDTH}}", end="|")

        print(f"{'OUT':>{SUMMARY_WIDTH}} ", end="|")

        for course_hole in back_nine:
            print(f"{course_hole.hole_number:{COL_WIDTH}}", end="|")


        print(f"{'IN':>{SUMMARY_WIDTH}} ", end="|")
        print(f"{'TOT':>{SUMMARY_WIDTH}} ", end="|")  

    def display_course_yardage(self):
        """Display yardage"""
        # Set the column width to use in the display
        LABEL_WIDTH = 9
        COL_WIDTH = 4
        SUMMARY_WIDTH = 5
        
        # Define front_nine, back_nine because I need to break them up to 
        # display OUT/IN/TOT
        front_nine = self._course_holes[:9]
        back_nine = self._course_holes[9:18]

        # print the yardages for first 9, OUT, back 9, IN, and TOT
        print(f"{self.tees:<{LABEL_WIDTH}}", end="|")

        for course_hole in front_nine:
            print(f"{course_hole.yardage:{COL_WIDTH}}", end="|")

        print(f"{sum(course_hole.yardage for course_hole in front_nine):{SUMMARY_WIDTH}} ", end="|")

        for hole in back_nine:
            print(f"{hole.yardage:{COL_WIDTH}}", end="|")

        print(f"{sum(course_hole.yardage for course_hole in back_nine):{SUMMARY_WIDTH}} ", end="|")
        print(f"{sum(course_hole.yardage for course_hole in self._course_holes):{SUMMARY_WIDTH}} ", end="|")

    def display_course_hcp(self):
        """Display HCP"""
        # Set the column width to use in the display
        LABEL_WIDTH = 9
        COL_WIDTH = 4
        SUMMARY_WIDTH = 6
        
        # Define front_nine, back_nine because I need to break them up to 
        # display OUT/IN/TOT
        front_nine = self._course_holes[:9]
        back_nine = self._course_holes[9:18]

        # print the HCPs for first 9, OUT, back 9, IN, and TOT
        print(f"{'HCP':<{LABEL_WIDTH}}", end="|")

        for course_hole in front_nine:
            print(f"{course_hole.handicap:{COL_WIDTH}}", end="|")

        print(f"{'':{SUMMARY_WIDTH}}", end="|")

        for course_hole in back_nine:
            print(f"{course_hole.handicap:{COL_WIDTH}}", end="|")

        print(f"{'':{SUMMARY_WIDTH}}", end="|")
        print(f"{'':{SUMMARY_WIDTH}}", end="|") 

    def display_course_par(self):
        """Display par for each hole and OUT/IN/TOT"""        
        # Set the column width to use in the display
        LABEL_WIDTH = 9
        COL_WIDTH = 4
        SUMMARY_WIDTH = 5
        
        # Define front_nine, back_nine because I need to break them up 
        front_nine = self._course_holes[:9]
        back_nine = self._course_holes[9:18]

        # print the Par for first 9, OUT, back 9, IN, and TOT
        print(f"{'PAR':<{LABEL_WIDTH}}", end="|")

        for course_hole in front_nine:
            print(f"{course_hole.par:{COL_WIDTH}}", end="|")

        print(f"{sum(course_hole.par for course_hole in front_nine):>{SUMMARY_WIDTH}} ", end="|")

        for course_hole in back_nine:
            print(f"{course_hole.par:{COL_WIDTH}}", end="|")

        print(f"{sum(course_hole.par for course_hole in back_nine):>{SUMMARY_WIDTH}} ", end="|")
        print(f"{sum(course_hole.par for course_hole in self._course_holes):>{SUMMARY_WIDTH}} ", end="|") 

    def display_course_info(self):
        """Display course info to the command line in a scorecard-like format.
        Call each method to display the entirety of the scorecard."""        
        self.display_course_header()        
        self.display_course_hole_number()        
        print()
        self.display_course_yardage()        
        print()
        self.display_course_hcp()
        print()
        self.display_course_par()
        
