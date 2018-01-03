import random
#Dice Roller
def dice_roller(num_dice, num_sides, num_bonus):
    result = 0
    rolls = [num_dice]
    for roll in rolls:
        roll = random.randint(1, num_sides)
        result +=roll
    result += num_bonus
    print(result)

def main ():
    go_again = True
    while go_again:
        print("Let's roll some dice! (or type \"quit\" to, well, you know).")
        num_dice = int(input("How many dice are you rolling?\n"))
        num_sides = int(input("How many sides do the dice have?\n"))
        num_bonus = int(input("Any modifiers?\n"))
        print("Voila!")
        dice_roller(num_dice,num_sides,num_bonus)

main()