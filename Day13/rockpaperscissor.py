import random

#choices are stored in list
choices = ["rock", "paper", "scissors"]

#taking the input from the user and converting to lower case for matching in the list choices
user = input("Enter rock, paper, or scissors: ").lower()

#taking the computer choices from choices using random.
computer = random.choice(choices)

#print the choice of the computer and user 
print("Computer chose: ", computer)
print("You choose :", user)

#logic building for the game
if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
    
#for everything except the user win and game tie, computer wins.    
elif user in choices:
    print("Computer wins!")
else:
    print("Invalid choice!")
