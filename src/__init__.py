# golf_tracker/__init__.py

# ----------------------------------------------
# 1. Package Metadata
# ----------------------------------------------
__version__ = "0.1.0"
__author__ = "Nathan Schoenack"
__email__ = "nschoena@hotmail.com"


# ----------------------------------------------
# 2. Public API Imports (Making key functions easy to access)
# ----------------------------------------------
# from .calculations import calculate_handicap
# from .scoring import record_score
# from .data import load_course_definitions # Assuming this loads your static JSON

# ----------------------------------------------
# 3. Explicit Export Control
# ----------------------------------------------
# __all__ = [
#     "__version__",
#     "calculate_handicap",
#     "record_score",
#     "load_course_definitions",
# ]

# ----------------------------------------------
# 4. (Optional) Initialization Code
# ----------------------------------------------
# For example, to ensure your internal data directory exists on first import
# import os
# if not os.path.exists('./.golf_tracker_data'):
#     os.makedirs('./.golf_tracker_data')