"""
combine_features.py

Merges personality dimension scores from the questionnaire with
task features collected from the user into a single row per task.
This combined row is what gets passed to the machine learning model.

Functions:
    combine_features() - Takes questionnaire averages and task list, returns combined feature rows.
"""

from src.constants import CATEGORY_MAP

#Combining the features into one dataset
def combine_features(averages, tasks):
    combined = []

    for task in tasks:
        row = {
            "name": task["name"],
            "U": round(averages["U"], 2),
            "I": round(averages["I"], 2),
            "Q": round(averages["Q"], 2),
            "S": round(averages["S"], 2),
            "category": CATEGORY_MAP[task["category"]],
            "hours_per_week": task["hours_per_week"],
            "stress": task["stress"],
            "urgency": task["urgency"],
            "importance": task["importance"],
            "mental_effort": task["mental_effort"]
        }
        combined.append(row)

    return combined