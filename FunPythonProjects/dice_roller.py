import random
import guess_a_number
#Dice Roller
def dice_roller(num_dice, num_sides, num_bonus):
    result = 0
    rolls = []
    for i in range(num_dice):
        rolls.append(None)
    for roll in rolls:
        roll = random.randint(1, num_sides)
        result += roll
    result += num_bonus
    print(result)
