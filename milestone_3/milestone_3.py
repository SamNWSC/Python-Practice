import random

# Defines questions and answers and score, questions and correct_answers can be changed out for other questions 
score = 0
questions = ["Who won the 1994 F1 World Championship?", "Which Driver has the most wins?", "Which driver has the most Grand Prix starts?"]
correct_answers = {"Who won the 1994 F1 World Championship?": "micheal schumacher", "Which Driver has the most wins?": "lewis hamilton", "Which driver has the most Grand Prix starts?": "fernando alonso"}

# Asks question 
playing = True
while playing == True: 
    for i in questions:
        question = random.choice(questions)
        user_answer = input("What's the answer to '{}'? ".format(question)).strip().lower()
        # Checks if they got th answer right 
        if user_answer == correct_answers.get(question, ""):
            print("Good Job")
            score += 10 
        else:
            print("Incorrect answer.")
    print(score)
    playing_status = input("Are you still playing Y/N").strip().lower()
    if playing_status == "n":
        playing = False 
           
print("Thank You for playing")
quit()