"""
prepare_data.py

Loads and preprocesses the survey dataset for model training.
Reshapes data from wide format (one row per participant) to long format
(one row per task per participant). Generates synthetic personality scores
(U, I, Q, S) for each participant since the dataset does not include them.
Derives the target label 'completed' using the proxy rule: hours_per_week > 0.

Functions:
    load_and_prepare() - Loads Excel data, reshapes it, and returns a clean DataFrame.
"""

import pandas as pd
import numpy as np

from src.constants import CATEGORY_MAP, TASK_CATEGORIES

def load_and_prepare(filepath):
    #Load file with multi-level header
    df = pd.read_excel(filepath, header=[0, 1])

    rows = []

    for _, participant in df.iterrows():
        # Generate random personality scores for this participant
        U = round(np.random.uniform(1, 5), 2)
        I = round(np.random.uniform(1, 5), 2)
        Q = round(np.random.uniform(1, 5), 2)
        S = round(np.random.uniform(1, 5), 2)
    
        for category in TASK_CATEGORIES:
                try:
                    hours = float(participant[(category, "Hours/Week")])
                    stress = float(participant[(category, "Stress")])
                    urgency = float(participant[(category, "Urgency")])
                    importance = float(participant[(category, "Importance")])
                    mental_effort = float(participant[(category, "Mental Effort")])

                    completed = 1 if hours > 0 else 0

                    rows.append({
                        "U": U,
                        "I": I,
                        "Q": Q,
                        "S": S,
                        "category": CATEGORY_MAP[category],
                        "hours_per_week": hours,
                        "stress": stress,
                        "urgency": urgency,
                        "importance": importance,
                        "mental_effort": mental_effort,
                        "completed": completed
                    })
                except:
                    continue

    return pd.DataFrame(rows)