import random

# Defines questions and answers and score
score = 0
questions = ["x", "y", "z"]
correct_answers = {"x": "a", "y": "b", "z": "c"}

# Asks question 

for i in questions:
    question = random.choice(questions)
    user_answer = input(f"What's the answer to '{question}'? ").strip().lower()
    # Checks if they got th answer right 
    if user_answer == correct_answers.get(question, ""):
        print("Good Job")
        score += 10 
    else:
        print("Incorrect answer.")
print(score)
quit()

    

