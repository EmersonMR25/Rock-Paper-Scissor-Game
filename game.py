# game.py
import random
print("Rock, Paper, Scissors, Shoot!")

#PROMT USER FOR IMPUT

user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("User chose:")
print(user_choice)


#COMPUTER CHOICE AT RANDOM TABLE

computer_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_options)
print("Computer chose:")
print(computer_choice)

