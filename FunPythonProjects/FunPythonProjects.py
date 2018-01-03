import random
#Dice Roller
def dice_roller(num_dice, num_sides, num_bonus):
    result = 0
    roll = random.randint(1, num_sides)
    print(roll)

num_sides = None
while num_sides != "quit":
    num_sides = input("How many sides on the die?")
    dice_roller(1,int(num_sides),0)
    num_sides = input("Enter a number to roll again, or \"quit\" to stop.")


    
