#This is a number guessing program
import random

number_to_guess = random.randint(1,10)

guess = None

while guess != number_to_guess:
    print("Let's play a guessing game")
    print("Try to guess a number between 1 and 10!")
    guess = input()