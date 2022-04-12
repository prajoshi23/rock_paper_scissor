import random
while True:
    
    choices = ["rock","paper","scissor"]
    comp = random.choice(choices)
    user = None
    while user not in choices:
        user = input("select your choice (rock/paper/scissor): ")
    print(f"Computer choice: {comp} \nYour choice: {user}")
    if comp == "rock":
        if user.lower() == "scissor":
            print("Computer wins")
        elif user.lower() == "paper":
            print("You win")
        else:
            print("draw")
    if comp == "paper":
        if user.lower() == "rock":
            print("Computer wins")
        elif user.lower() == "scissor":
            print("You win")
        else:
            print("draw")

    if comp == "scissor":
        if user.lower() == "paper":
            print("Computer wins")
        elif user.lower() == "rock":
            print("You win")
        else:
            print("draw")

    option = input("Want to play again? (yes/no): ").lower()
    
    if option != "yes":
        break
    

        