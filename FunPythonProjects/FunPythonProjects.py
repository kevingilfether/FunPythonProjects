import random
#Dice Roller
def dice_roller(num_dice, num_sides, num_bonus):
    result = 0
    rolls = int[num_dice]
    for roll in rolls:
        roll = random.randint(1, num_sides)
        result +=roll
    result += num_bonus
    print(result)