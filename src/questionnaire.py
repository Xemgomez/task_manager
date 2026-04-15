"""
questionnaire.py

Collects lifestyle information from the user through a series of questions.
Each question maps to one of four personality dimensions: U, I, Q, S.

Functions:
    run_questionnaire() - Presents questions and collects answers from the user.
    compute_profile()   - Computes average dimension scores and dominant personality category.
"""

questions = [
    # Urgency Sensitivity (U)
    {"text": "How do you usually approach deadlines?", "dimension": "U", "options": [
        ("Start immediately when assigned", 1),
        ("Start well in advance", 2),
        ("Focus heavily near the deadline", 4),
        ("Rush at the last minute", 5)
    ]},
    {"text": "How do you feel when a deadline is approaching?", "dimension": "U", "options": [
        ("Calm, I'm already done", 1),
        ("Slightly motivated to wrap up", 2),
        ("Stressed but productive", 4),
        ("Panicked and overwhelmed", 5)
    ]},
    {"text": "When do you feel the most urgency to complete a task?", "dimension": "U", "options": [
        ("As soon as it's assigned", 1),
        ("A few days before it's due", 2),
        ("The day before it's due", 4),
        ("The moment it's due", 5)
    ]},

    # Importance Orientation (I)
    {"text": "How important are long-term goals in your daily decisions?", "dimension": "I", "options": [
        ("Extremely important", 5),
        ("Somewhat important", 4),
        ("Not a major factor", 2),
        ("I focus more on immediate tasks", 1)
    ]},
    {"text": "If you have limited time, you usually:", "dimension": "I", "options": [
        ("Tackle the hardest, highest-impact task first", 5),
        ("Work on what's due first", 3),
        ("Finish the quickest tasks first", 2),
        ("Do what feels easiest", 1)
    ]},

    # Quick-Win Preference (Q)
    {"text": "How do you prefer to complete tasks?", "dimension": "Q", "options": [
        ("One at a time until finished", 2),
        ("Short bursts with breaks", 4),
        ("Rotate between tasks", 3),
        ("Knock out the easiest ones first", 5)
    ]},
    {"text": "How do you feel about large tasks?", "dimension": "Q", "options": [
        ("I prefer completing them early", 2),
        ("I break them into smaller pieces", 4),
        ("I mix them with small tasks", 3),
        ("I avoid them until necessary", 1)
    ]},

    # Structure Preference (S)
    {"text": "How would you describe your planning style?", "dimension": "S", "options": [
        ("I follow a strict daily schedule", 5),
        ("I make a loose plan each day", 4),
        ("I plan occasionally when overwhelmed", 2),
        ("I rarely plan, I just react", 1)
    ]},
    {"text": "How would you describe your current workload management?", "dimension": "S", "options": [
        ("I track everything in a system", 5),
        ("I keep a mental to-do list", 3),
        ("I write things down occasionally", 2),
        ("I handle tasks as they come", 1)
    ]},
    {"text": "How do you feel when your schedule is disrupted?", "dimension": "S", "options": [
        ("Very uncomfortable, I need structure", 5),
        ("Slightly bothered but I adapt", 3),
        ("Indifferent, I'm flexible", 2),
        ("Relieved, I prefer spontaneity", 1)
    ]},
]

def run_questionnaire():
    print('\nWelcome! Please answer the following questions.\n')

    scores = {"U": [], "I": [], "Q": [], "S": []}

    for question in questions:
        print(question["text"])
        for i, (option_text, option_score) in enumerate(question["options"]):
            print(f'  {i + 1}. {option_text}')
        
        while True:
            try:
                answer = int(input("Your choice (1-4): "))
                if 1 <= answer <=4:
                    selected_score = question["options"][answer - 1][1]
                    scores[question["dimension"]].append(selected_score)
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        print()
    
    return scores

def compute_profile(scores):
    averages = {}
    for dimension, score_list in scores.items():
        averages[dimension] = sum(score_list) / len(score_list)
    
    dominant = max(averages, key=lambda x: averages[x])

    category_map = {
        "U": "Deadline-Driven",
        "I": "Strategist",
        "Q": "Sprinter",
        "S": "Planner"
    }

    category = category_map[dominant]

    return averages, category