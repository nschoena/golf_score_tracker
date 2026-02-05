"""
File: score.py

This module defines the data structures for a score, mirroring the established
JSON schema as defined in score.schema.json.

Classes defined:
- ScoreHole: defines what a hole is as used in the Score class
- Score: defines the components and methods of a score associated with a round
    played

"""
import json
from pathlib import Path
from typing import List, TYPE_CHECKING
from datetime import date, datetime

class ScoreHole:
    """
    The ScoreHole class will represent a score as it was played or would appear
    on a scorecard. There will be a normal score and a detailed score depending
    on what was tracked during the round.

    """
    def __init__(self, 
                 hole_number: int, 
                 strokes: int, 
                 putts: int | None = None, 
                 drive: str | None = None, 
                 gir: bool | None = None):
        """
        All:
        :param hole_number: number of the hole on the golf course
        :param strokes: total strokes including putts

        Detailed:
        :param putts (detailed): total number of putts
        :param drive (detailed): accuracy result of the drive (Left, 
        Fairway, Right, Par3)
        :param gir (detailed): boolean for if green was hit in regulation. You could 
        calculate this using the formula: 
           if ((strokes-putts) <= (par-2)):
             return true 
           else
             return false
        """
        self.hole_number = hole_number
        self.strokes = strokes
        self.putts = putts
        self.drive = drive
        self.gir = gir

    # Inside ScoreHole class
    def __str__(self) -> str:
        """Returns a readable string for a single hole's performance"""
        base = f"Hole {self.hole_number}: {self.strokes} strokes"
        
        # Add details only if they exist
        if self.is_detailed:
            gir = "GIR" if self.gir else "No GIR"
            details = f" ({self.putts} putts, {self.drive} drive), {gir}." 
        else:
            details = ""
        
        return base + details
    
    @property
    def is_detailed(self) -> bool:
        """Returns true if all Detailed properties are included"""
        return all((
            self.putts is not None,
            self.drive is not None,
            self.gir is not None
        ))

    # Notice: no setter is required for is_detailed because it doesn't change 
    # the state of the object.

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
    def strokes(self) -> int:
        return self._strokes

    @strokes.setter
    def strokes(self, value: int):
        """setter for strokes, validating it is between 1-12 and that it's 
        greater than number of putts"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Strokes number must be an integer, received {type(value).__name__}.")
        
        # Validation Logic
        MIN_STROKE_NUMBER = 1
        MAX_STROKE_NUMBER = 15
        if not (MIN_STROKE_NUMBER <= value <= MAX_STROKE_NUMBER):
            raise ValueError(f"Strokes must be between {MIN_STROKE_NUMBER} and {MAX_STROKE_NUMBER}. Received: {value}")
        
        # Make sure strokes is greater than putts
        # Because strokes is set before putts, I need to handle the situation
        # where putts hasn't been set yet
        current_putts = getattr(self, '_putts', None)
        if current_putts is not None and value <= current_putts:
            raise ValueError(f"Strokes must be greater than putts. Putts is {self.putts} and you entered: {value}")

        # Store the validated value in the internal variable
        self._strokes = int(value)
        
    @property
    def putts(self) -> int | None:
        return self._putts
    
    @putts.setter
    def putts(self, value: int | None):
        """setter for putts, validating it is between 0-10 and it's less than
        than number of strokes"""
        if not isinstance(value, (int, float, type(None))):
            raise TypeError(f"Putts number must be an integer or None, received {type(value).__name__}.")
        
        # early exit if None (not detailed)
        if value is None:
            self._putts = None
            return

        # Validation Logic
        MIN_PUTTS_NUMBER = 0
        MAX_PUTTS_NUMBER = 10

        # Make sure putts is less than strokes
        # Because putts could be set before strokes, I need to handle the 
        # situation where strokes hasn't been set yet.
        current_strokes = getattr(self, '_strokes', None)
        if current_strokes is not None and value >= current_strokes:
            raise ValueError(f"Putts must be less than strokes. Strokes is {self.strokes} and you tried entering {value}.")

        if not MIN_PUTTS_NUMBER <= value <= MAX_PUTTS_NUMBER:
            raise ValueError(f"Putts must be between {MIN_PUTTS_NUMBER} and {MAX_PUTTS_NUMBER}. Received: {value}")
        
        # Store the validated value in the internal variable
        self._putts = int(value)

    @property
    def drive(self) -> str | None:
        return self._drive
    
    @drive.setter
    def drive(self, value: str | None):
        """setter for drive which indicates drive result. Must be None or string 
        that is either Left, Fairway, Right, or Par3"""        
        if not isinstance(value, (str, type(None))):
            raise TypeError(f"Drive must be a string or None, received {type(value).__name__}.")
        
        # early exit if None (not detailed)
        if value is None:
            self._drive = None
            return
        
        # Case sensitivity consideration
        value_to_check = value.upper()

        # Validation Logic
        ALLOWED_DRIVE_VALUES: list[str] = ['LEFT', 'FAIRWAY', 'RIGHT', 'PAR3']
        if value_to_check not in ALLOWED_DRIVE_VALUES:
            raise ValueError(f"Drive must be either 'Left', 'Fairway', " 
                             f"'Right', or 'Par3' (Capitalization doesn't"
                             f" matter). You entered {value}.")
        
        # Store the validated value in the internal variable
        self._drive = value.upper()

    @property
    def gir(self) -> bool | None:
        return self._gir
    
    @gir.setter
    def gir(self, value: bool | None):
        """setter for gir (greens in regulation). Is either True or False"""
        if not isinstance(value, (bool, type(None))):
            raise TypeError(f"GIR must be a bool or None, received {type(value).__name__}.")
        
        # early exit if None
        if value is None:
            self._gir = None
            return

        # Store the validated value in the internal variable
        self._gir = value
        
class Score:
    """
    The Score class is the basic unit for recording a score. It is aligned with 
    score.schema.json which is found in /data/scores.
    """
    def __init__(self, score_id: int, course_id: int, course_name: str, 
                 tees: str, course_side: str, date_played: date,  
                 holes_played: List[ScoreHole]):
        """
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
        self.holes_played = holes_played

    # Used for testing before the display function is written
    def __str__(self) -> str:
        """Print a human-readable summary of the score"""
        # Use a ternary operator to indicate if the score is detailed or not
        score_type = "detailed" if self.is_detailed else "not detailed"
        
        # Start with the Header info (course, date, etc)
        output = [f"Score was recorded at {self.course_name.title()} on "
                  f"{self.date_played}.\nThe score was {score_type.title()}."]
        
        # Display scoreHole information by utilizing scoreHole's __str__ method 
        for sh in self.holes_played:
            output.append(str(sh))

        # Use .join(output) to display all entries in the output array, 
        # separated by a line break.
        return "\n".join(output)
    
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
        for sh in value:
            if not isinstance(sh, ScoreHole):
                raise TypeError(f"elements in holes_played list must be of "
                                f"ScoreHole type. "
                                f"Received {type(sh).__name__}.")

        # Store the validated list in the internal variable
        self._holes_played = value

    #
    # assign calculated properties
    #
    
    # is_detailed - to indicate if the scoreHole objects are all detailed. If 
    # even one hole is not detailed, the entire score should be considered not
    # detailed
    @property
    def is_detailed(self) -> bool:
        return all(sh.is_detailed for sh in self.holes_played)

    # round_score
    @property
    def round_score(self) -> int:
        """calculates total strokes"""
        return sum(sh.strokes for sh in self.holes_played)
    
    # round_putts
    @property
    def round_putts(self) -> int:
        """calculates total putts. Check if the score is detailed and return
        None if it is"""
        if not self.is_detailed:
            return 0        
        
        return sum(sh.putts or 0 for sh in self.holes_played)
    
    # gir_percent
    @property
    def gir_percent(self) -> float:
        """Calculates green in regulation percentage. Check if score is detailed 
        and return None if it is"""
        if not self.is_detailed:
            return 0.0
        
        # sum() treats True as 1, False as 0
        girs = sum(1 for sh in self.holes_played if sh.gir)
        
        return (girs / len(self.holes_played))

    @property
    def drive_accuracy(self) -> List[float]:
        """returns a 3-member list of float values for driving accuracy in
        order of LEFT, FAIRWAY, RIGHT"""
        if not self.is_detailed:
            return [0.0, 0.0, 0.0]

        total_drives = 0
        left, fairway, right = 0, 0, 0
        
        for sh in self.holes_played:
            # Use 'or' to provide a fallback string for Intellisense
            res = (sh.drive or "").upper()
            
            if res == 'PAR3': 
                continue
            total_drives += 1
            if res == 'LEFT':
                left += 1
            elif res == 'FAIRWAY':                
                fairway += 1
            elif res == 'RIGHT':                
                right += 1
        
        # Guard against division by zero (could be all par3 course)
        if total_drives == 0:
            return [0.0, 0.0, 0.0]

        return [left / total_drives, fairway / total_drives, right / total_drives]
    
    #
    # Class methods
    #
    @classmethod
    def load_from_json(cls, filepath: str | Path):
        """Reads a JSON file and returns a new Score instance"""
        # Load the score data json file and deserialize into raw_data
        with open(filepath, 'r') as file:
            raw_data = json.load(file)

        # Create empty array to store ScoreHole objects
        score_holes_played = []

        # iterate through the hole info in the dictionary and create a hole
        # object. On each loop, append the newly created hole to the 
        # hole_objects array.
        for hole_dict in raw_data['holesPlayed']:
            # Create a ScoreHole instance 'sh' by passing in data from hole_dict
            sh = ScoreHole(
                hole_number=hole_dict['holeNumber'],
                strokes=hole_dict['strokes'],
                putts=hole_dict['putts'],
                drive=hole_dict['driveResult'],
                gir=hole_dict['gir']                
            )
            # Append ScoreHole instance sh to score_hole_objects array
            score_holes_played.append(sh)
        
        # assign the remaining properties
        # score_id
        score_id = raw_data['scoreId']

        # course_id
        course_id = raw_data['courseId']

        # course_name
        course_name = raw_data['courseName']

        # tees
        tees = raw_data['tees']

        # course_side
        course_side = raw_data['courseSide']

        # date_played
        date_played = raw_data['datePlayed']        

        # return the class object
        return cls(
            score_id=score_id,
            course_id=course_id,
            course_name=course_name,
            tees=tees,
            course_side=course_side,
            date_played=date_played,
            holes_played=score_holes_played
        )       
    
    #
    # instance methods
    #    
    def display_score_horizontal_lines(self):
        """Display the hole numbers"""
        # Set the column width to use in the display
        LABEL_WIDTH = 10
        COL_WIDTH = 5
        SUMMARY_WIDTH = 7
        TOTAL_WIDTH = (LABEL_WIDTH) + (18 * COL_WIDTH) + (3 * SUMMARY_WIDTH)
        print("-" * TOTAL_WIDTH)     

    def display_score_hole_number(self):
        """Display the hole numbers"""
        # Set the column width to use in the display
        LABEL_WIDTH = 10
        COL_WIDTH = 5
        SUMMARY_WIDTH = 7

        self.display_score_horizontal_lines()  
        
        # Define front_nine, back_nine because I need to break them up to 
        # display OUT/IN/TOT
        front_nine = self.holes_played[:9]
        back_nine = self.holes_played[9:18]

        # print the Holes for first 9, OUT, back 9, IN, and TOT
        print(f"{'HOLE':{LABEL_WIDTH}}", end="|")

        for hole in front_nine:
            print(f"{hole.hole_number:{COL_WIDTH}}", end="|")

        print(f"{'OUT':>{SUMMARY_WIDTH}} ", end="|")

        for hole in back_nine:
            print(f"{hole.hole_number:{COL_WIDTH}}", end="|")

        print(f"{'IN':>{SUMMARY_WIDTH}} ", end="|")
        print(f"{'TOT':>{SUMMARY_WIDTH}} ", end="|")  

    def display_score_strokes(self):
        """Display strokes for each hole, with totals for OUT/IN/TOT"""
        # Set the column width to use in the display
        LABEL_WIDTH = 9
        COL_WIDTH = 4
        SUMMARY_WIDTH = 5
        
        # Define front_nine, back_nine because I need to break them up 
        front_nine = self.holes_played[:9]
        back_nine = self.holes_played[9:18]

        # print the Par for first 9, OUT, back 9, IN, and TOT
        print(f"{'Strokes':<{LABEL_WIDTH}}", end="|")

        for hole in front_nine:
            print(f"{hole.strokes:{COL_WIDTH}}", end="|")

        print(f"{sum(hole.strokes for hole in front_nine):>{SUMMARY_WIDTH}} ", end="|")

        for hole in back_nine:
            print(f"{hole.strokes:{COL_WIDTH}}", end="|")

        print(f"{sum(hole.strokes for hole in back_nine):>{SUMMARY_WIDTH}} ", end="|")
        print(f"{sum(hole.strokes for hole in self.holes_played):>{SUMMARY_WIDTH}} ", end="|")

    def display_score_putts(self):
        """Display putts for each hole, with totals for OUT/IN/TOT"""
        # Set the column width to use in the display
        LABEL_WIDTH = 9
        COL_WIDTH = 4
        SUMMARY_WIDTH = 5
        
        # Define front_nine, back_nine because I need to break them up 
        front_nine = self.holes_played[:9]
        back_nine = self.holes_played[9:18]

        # print the Putts for first 9, OUT, back 9, IN, and TOT
        print(f"{'Putts':<{LABEL_WIDTH}}", end="|")

        for hole in front_nine:
            print(f"{hole.putts:{COL_WIDTH}}", end="|")

        print(f"{sum(hole.putts or 0 for hole in front_nine):>{SUMMARY_WIDTH}} ", end="|")

        for hole in back_nine:
            print(f"{hole.putts:{COL_WIDTH}}", end="|")

        print(f"{sum(hole.putts or 0 for hole in back_nine):>{SUMMARY_WIDTH}} ", end="|")
        print(f"{sum(hole.putts or 0 for hole in self.holes_played):>{SUMMARY_WIDTH}} ", end="|")

    def display_score_gir(self):
        """Display if a green in regulation occurred on this hole"""
        # Set the column width to use in the display
        LABEL_WIDTH = 9
        COL_WIDTH = 4
        SUMMARY_WIDTH = 5
        
        # Define front_nine, back_nine because I need to break them up 
        front_nine = self.holes_played[:9]
        back_nine = self.holes_played[9:18]
        
        # print the GIR for first 9, OUT, back 9, IN, and TOT
        print(f"{'GIR':<{LABEL_WIDTH}}", end="|")

        # define a check mark to be used for GIR        
        check_mark = "\u2713"

        # display check mark if GIR, blank if no GIR        
        for hole in front_nine:
            symbol = check_mark if hole.gir else ""
            print(f"{symbol:^{COL_WIDTH}}", end="|")

        # print total GIRs on the front nine
        front_nine_girs = sum(1 for hole in front_nine if hole.gir)
        print(f"{front_nine_girs:>{SUMMARY_WIDTH}} ", end = "|")
        
        # display check mark if GIR, blank if no GIR        
        for hole in back_nine:
            symbol = check_mark if hole.gir else ""
            print(f"{symbol:^{COL_WIDTH}}", end="|")

        # print total GIRs on the back nine
        back_nine_girs = sum(1 for hole in back_nine if hole.gir)
        print(f"{back_nine_girs:>{SUMMARY_WIDTH}} ", end = "|")

        # print total GIRs for the whole course
        total_girs = front_nine_girs + back_nine_girs
        print(f"{total_girs:>{SUMMARY_WIDTH}} ", end = "|")

    def display_score_fairway(self):
        """Display result of the drive on this hole"""
        # Set the column width to use in the display
        LABEL_WIDTH = 9
        COL_WIDTH = 4
        SUMMARY_WIDTH = 5
        
        # Define front_nine, back_nine because I need to break them up 
        front_nine = self.holes_played[:9]
        back_nine = self.holes_played[9:18]
        
        # print the GIR for first 9, OUT, back 9, IN, and TOT
        print(f"{'Fairway':<{LABEL_WIDTH}}", end="|")

        # Print L, F, R for drive result. If par 3, print nothing
        # define the drive symbols to return based on result
        drive_symbol = {
            "LEFT": "\u2190",
            "FAIRWAY": "\u25c9",
            "RIGHT": "\u2192",
            "PAR3": "",
            None: ""
        }        
        
        for hole in front_nine:            
            symbol = drive_symbol.get(hole.drive, "") 
            print(f"{symbol:^{COL_WIDTH}}", end="|")

        print(f"{"":>{SUMMARY_WIDTH}} ", end = "|")

        for hole in back_nine:            
            symbol = drive_symbol.get(hole.drive, "") 
            print(f"{symbol:^{COL_WIDTH}}", end="|")

        print(f"{"":>{SUMMARY_WIDTH}} ", end = "|")
        print(f"{"":>{SUMMARY_WIDTH}} ", end = "|")

    def display_score_summary(self):
        """Display the calculated statistics for the round
            Total Strokes 
            Total Putts
            Driving accuracy
                Left
                Fairway
                Right
            Greens in regulation percentage            
        """
        # Totals
        print(f"Total Strokes: {self.round_score}") 
        if self.is_detailed:
            print(f"Total Putts: {self.round_putts}") 
            print(f"GIR: {self.gir_percent:.0%}")         
            print(f"Fairways: {self.drive_accuracy[1]:.0%}")
            print(f"Drives missed left: {self.drive_accuracy[0]:.0%}")
            print(f"Drives missed right: {self.drive_accuracy[2]:.0%}")
    
    def display_score_info(self):
        """Display all score information"""
        print()
        self.display_score_horizontal_lines()
        self.display_score_strokes()
        print()
        self.display_score_putts()
        print()
        self.display_score_gir()
        print()
        self.display_score_fairway()
        print()
        self.display_score_horizontal_lines()
        self.display_score_summary()