"""
File: score_hole.py

This module defines the data structure for a golf Hole to be used in Score 
object, mirroring the established JSON schema as defined in score.schema.json.
"""

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
        Docstring for __init__
        
        Normal
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


    @property
    def is_detailed(self) -> bool:
        """Returns true if all Detailed properties are included"""
        return all((
            self.putts is not None,
            self.drive is not None,
            self.gir is not None
        ))

    # Notice: no setter is required here because it doesn't change the state
    # of the object.

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
        
        # make sure strokes is greater than putts
        if self.putts is not None and value <= self.putts:
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

        if self.strokes and value >= self.strokes:
            raise ValueError(f"Number of putts is more than number of strokes. Strokes is {self.strokes} and you tried entering {value}.")

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
                             f"matter). You entered {value}.")
        
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
        
