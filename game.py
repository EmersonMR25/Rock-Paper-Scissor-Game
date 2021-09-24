# game.py

#import random modeule to allow the application to choose "rock," "paper," or "scissors" at random
import random

#use OS module to let x = "PLAYER_ONE"
import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_ONE")

print ("-------------------")
#print ("WELCOME 'PLAYER_ONE' TO MY ROCK-PAPER-SCISSORS GAME... ")
print ("WELCOME,", x, "TO MY ROCK-PAPER-SCISSORS GAME... ")
print ("-------------------")

# PROMPT USER FOR INPUT

#user_choice = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("PLEASE CHOOSE EITHER 'rock' OR 'paper' OR 'scissors': ")
print ("-------------------")
print("YOU CHOSE:")
print(user_choice)
print ("-------------------")


#If user choice's not spelled correctly, the program will stop 

if user_choice not in ["rock", "paper", "scissors"]:
    print ("YOUR CHOICE IS INVALID. CHECK YOUR SPELLING AND TRY AGAIN!! ")
    print ("-------------------")
    exit()

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
        print ("OH, THE COMPUTER WON")
        #If the computer chooses 'scissors' you win.
        #Else 'paper' is the other choice left. Therefore, you loose.

elif user_choice == 'paper':
    if computer_choice == 'rock':
        print ("AWESOME! YOU WIN")
    else: 
        print ("OH, THE COMPUTER WON")
        #If the computer chooses 'rock' you win.
        #Else 'scissors' is the other choice left. Therefore, you loose.

elif user_choice == 'scissors':
    if computer_choice == 'paper':
        print ("AWESOME! YOU WIN")
    else: 
        print ("OH, THE COMPUTER WON")
        #If the computer chooses 'paper' you win.
        #Else 'rock' is the other choice left. Therefore, you loose.

print ("-------------------")
print ("THANK'S FOR PLAYING. PLEASE PLAY AGAIN")
print ("-------------------")