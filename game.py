# game.py

#import random modeule to allow the application to choose "rock," "paper," or "scissors" at random
import random

#use OS module to let x = "PLAYER_ONE"
import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_ONE", default="PLAYER_ONE")

print ("-------------------")
#print ("WELCOME 'PLAYER_ONE' TO MY ROCK-PAPER-SCISSORS GAME... ")
print ("WELCOME,", x, "TO MY ROCK-PAPER-SCISSORS GAME... ")
print ("-------------------")

# PROMPT USER FOR INPUT
#user_choice = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("PLEASE CHOOSE EITHER 'rock', 'paper', OR 'scissors': ")
print ("-------------------")
print("YOU CHOSE:")
print(user_choice)

#If user choice's not spelled correctly, the program will stop 
if user_choice not in ["rock", "paper", "scissors"]:
    print ("-------------------")
    print ("YOUR CHOICE IS INVALID. CHECK YOUR SPELLING AND TRY AGAIN! ")
    print ("-------------------")
    exit()

# COMPUTER CHOICE (AT RANDOM)
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("COMPUTER CHOSE:")
print(computer_choice)
print ("-------------------")

# DETERMINING THE WINNER (3 WINNING AND LOOSING ROUTES AND 1 TIE ROUTE)

# TIE (1)
#user_choice == computer_choice
if user_choice == computer_choice:
    print ("IT IS A TIE!")

# WIN (1)
#user_choice == 'rock, so if the computer_choice=='scissors' you win
# LOOSE(1)
#Else 'paper' is the other choice left. Therefore, you loose
elif user_choice == 'rock':
    if computer_choice == 'scissors':
        print ("AWESOME! YOU WIN")
    else: 
        print ("OH, THE COMPUTER WON")

# WIN (2)
#user_choice == 'paper', so if the computer chooses 'rock' you win
# LOOSE (2)
#Else 'scissors' is the other choice left. Therefore, you loose.
elif user_choice == 'paper':
    if computer_choice == 'rock':
        print ("AWESOME! YOU WIN")
    else: 
        print ("OH, THE COMPUTER WON")

# WIN (3)
#user_choice == 'scissors', so if the computer chooses 'paper' you win
#LOOSE (3)
#Else 'rock' is the other choice left. Therefore, you loose
elif user_choice == 'scissors':
    if computer_choice == 'paper':
        print ("AWESOME! YOU WIN")
    else: 
        print ("OH, THE COMPUTER WON")

print ("-------------------")
print ("THANK'S FOR PLAYING. PLEASE PLAY AGAIN")
print ("-------------------")