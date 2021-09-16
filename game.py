# game.py
import random

print("ROCK, PAPER, SCISSORS ... SHOOT!")

#PROMT USER FOR IMPUT

user_choice = input("CHOOSE 'rock', 'paper' OR 'scissors': ")
print("USER HAS CHOSEN:")
print(user_choice)


#COMPUTER CHOICE AT RANDOM TABLE

computer_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_options)
print("COMPUTER HAS CHOSEN:")
print(computer_choice)

# DETERMING THE WINNER

if computer_choice == user_choice:
    print("BOTH CHOSE THE SAME OUTCOME. IT IS A TIE!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("ROCK SMASHES SCISSORS. YOU WIN!")
    else:
        print("PAPER COVERS ROCK. YOU LOOSE!")

    print("THANK YOU FOR PLAYING!!!!!!!!")

elif user_choice == "paper":
    if computer_choice == "rock":
        print("PAPER COVERS ROCK. YOU WIN!")
    else:
        print("SCISSORS CUTS PAPER. YOU LOOSE!")
    
    print("THANK YOU FOR PLAYING!!!!!!!!")

elif user_choice == "scissors":
    if computer_choice == "paper":
        print("SCISSORS CUTS PAPER. YOU WIN!")
    else:
        print("ROCK SMASHES SCISSORS. YOU LOOSE!")
    
    print("THANK YOU FOR PLAYING!!!!!!!!")
    
else:
    print("THAT IS NOT A VALID PLAY. CHECK YOUR SPELLING!!")



