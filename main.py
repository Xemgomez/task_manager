from src.questionnaire import run_questionnaire, compute_profile
from src.task_features import get_task_input

#Lifestyle questionnaire
scores = run_questionnaire()
averages, category = compute_profile(scores)

print(f"Your dimension averages: {averages}")
print(f"Your personality category: {category}")

#To-Do list input
tasks = get_task_input()

print("\n---Task list---")
for task in tasks:
    print(task)