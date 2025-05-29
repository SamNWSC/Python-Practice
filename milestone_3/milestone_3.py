import random

score = 0
questions = [
    "Who won the 1994 F1 World Championship?", 
    "Which Driver has the most wins?", 
    "Which driver has the most Grand Prix starts?"
]
correct_answers = {
    "Who won the 1994 F1 World Championship?": "micheal schumacher", 
    "Which Driver has the most wins?": "lewis hamilton", 
    "Which driver has the most Grand Prix starts?": "fernando alonso"
}

playing = True
while playing:
    # Shuffle the list so questions come in random order without repeats
    random.shuffle(questions)
    
    for question in questions:
        user_answer = input("What's the answer to '{}'? ".format(question)).strip().lower()
        if user_answer == correct_answers.get(question, ""):
            print("Good Job")
            score += 10
        else:
            print("Incorrect answer.")
    
    print("Score: {}".format(score))
    playing_status = input("Are you still playing? (Y/N): ").strip().lower()
    if playing_status == "n":
        playing = False

print("Thank You for playing")
