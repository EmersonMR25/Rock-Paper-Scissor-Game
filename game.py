# game.py

import random

print ("-------------------")
print ("ROCK, PAPER, SCISSORS ... SHOOT! ")
print ("-------------------")

# PROMPT USER FOR INPUT

#x = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("CHOOSE'rock' OR 'paper' OR 'scissors': ")
print ("-------------------")
print("USER CHOSE:")
print(user_choice)
print ("-------------------")

# COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("COMPUTER CHOSE:")
print(computer_choice)
print ("-------------------")

# DETERMINING THE WINNER

# TIE
#user_choice == computer_choice

# WIN 
#user_choice == 'rock' and computer_choice == 'scissors'
#user_choice == 'paper' and computer_choice == 'rock'
#user_choice == 'scissors' and computer_choice == 'paper'

# LOSE
#user_choice == 'rock' and computer_choice == 'paper'
#user_choice == 'paper' and computer_choice == 'scissors'
#user_choice == 'scissors' and computer_choice == 'rock'

if user_choice == computer_choice:
    print ("IT IS A TIE!")

elif user_choice == 'rock':
    if computer_choice == 'scissors':
        print ("AWESOME! YOU WIN")
    else: 
        print ("OH, THE COMPUTER WON. IT'S OKAY")
        #If the computer chooses 'scissors' you win.
        #Else 'paper' is the other choice left. Therefore, you loose.

elif user_choice == 'paper':
    if computer_choice == 'rock':
        print ("AWESOME! YOU WIN")
    else: 
        print ("OH, THE COMPUTER WON. IT'S OKAY")
        #If the computer chooses 'rock' you win.
        #Else 'scissors' is the other choice left. Therefore, you loose.

elif user_choice == 'scissors':
    if computer_choice == 'paper':
        print ("AWESOME! YOU WIN")
    else: 
        print ("OH, THE COMPUTER WON. IT'S OKAY")
        #If the computer chooses 'paper' you win.
        #Else 'rock' is the other choice left. Therefore, you loose.

print ("-------------------")
print ("THANK'S FOR PLAYING. PLEASE PLAY AGAIN")
print ("-------------------")