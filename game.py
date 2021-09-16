# game.py
import random

print("ROCK, PAPER, SCISSORS ... SHOOT!")

#PROMT USER FOR IMPUT

user_choice = input("CHOOSE 'rock', 'paper' or 'scissors': ")
print("USER HAS CHOSEN:")
print(user_choice)


#COMPUTER CHOICE AT RANDOM TABLE

computer_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_options)
print("COMPUTER HAS CHOSEN:")
print(computer_choice)

# DETERMING THE WINNER

if computer_choice == user_choice:
    print("Both chose the same. It is a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors. YOU WIN!")
    else:
        print("Paper covers rock. YOU LOOSE!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper convers rock. YOU WIN!")
    else:
        print("Scissors cuts paper. YOU LOOSE!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Paper cuts paper. YOU WIN!")
    else:
        print("Rock smashes paper. YOU LOOSE!")


# PLAY AGAIN 
## (Got ir from GOOGLE)

