#This is a number guessing program
import random
number_to_guess = random.randint(1,10)

guess = None

print("Let's play a guessing game")
print("Try to guess a number between 1 and 10!")
guess = int(input())

while guess != number_to_guess:
    if guess > number_to_guess:
        print("You're too high! Try again.")
        guess = int(input())
    elif guess < number_to_guess:
        print("You're too low. Try again.")
        guess = int(input())

print("You got it!")