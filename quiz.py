questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

def display():
    q_num=0
    correct_ans = 0
    guesses = []
    for q in questions:
        print(q)
        for option in options[q_num]:
            print(option)
        q_num += 1
        guess = input("your answer: ").upper()
        guesses.append(guess)
        correct_ans += check(guess,questions[q])
        print("#-------------------------------------#")
    
    score(correct_ans,guesses)
    
        
def check(guess,answer):
    if guess == answer:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
def score(correct_ans,guesses):
    print("correct answers: ")
    for i in questions:
        print(questions[i],end=" ")
    print()    
    print("your answers: ")
    for g in guesses:
        print(g,end=" ")
    score = (correct_ans / len(questions)) * 100
    print()
    print("Your score is: " + str(score) +"%")
def new_game():
    response = input("Want to play again?: (yes/no)").lower()
    if response not in ["yes","no"]:
        raise Exception("Not a valid input")
    if response == "yes":
        return True
    else:
        return False
display()
while new_game():
    display()

print("Thank you for playing,Bye!")


    
