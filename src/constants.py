"""
constants.py

Defines shared constants used across the project.

CATEGORY_MAP: Maps task category names to numerical values for the model.
TASK_CATEGORIES: List of all task category names derived from CATEGORY_MAP.
"""

CATEGORY_MAP = {
    "School Work": 0,
    "Physical Activity": 1,
    "Hobbies": 2,
    "Social Activities": 3,
    "Errands": 4,
    "Leisure / Down Time": 5,
    "Health / Grooming": 6,
    "Miscellaneous Projects": 7,
    "Work": 8
}

TASK_CATEGORIES = list(CATEGORY_MAP.keys())