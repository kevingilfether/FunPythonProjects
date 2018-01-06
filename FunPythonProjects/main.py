import Room
import Portal

portal_entrance_hall_to_dragon_lair = Portal.Portal(entrance_hall, dragon_lair)
entrance_hall = Room.Room("biggish", 
                 "A richly appointed banquet hall. Incense floats in the air, and a sumptious feast seems like it might occur at any moment. There is a faint glow throw the door to the north",
                 portal_n = portal_entrance_hall_to_dragon_lair,
                 portal_e = None,
                 portal_s = None,
                 portal_w = None)

dragon_lair = Room.Room("Vast, cavernous even!",
                        "Oh man, you've really stepped in it now! A giant dragon is sleeping ahead of you on a pile of gold and stuff. It looks asleep and like it didn't need anymore description.",
                        portal_n = "A dragon is there, you dimwit!",
                        portal_e = None,
                        portal_s = portal_entrance_hall_to_dragon_lair,
                        portal_w = None)

#Main Copy!
print("Greetings, yon dungeon spelunker!")
print("You behold in front of you a 'donjon' of great power 'n' promise.")
while(dungeon_enter != "yes" or "no"):
    dungeon_enter = input("Do you enter, brave adventurer?\n")
    if dungeon_enter.lower == "yes":
        player_location = entrance_hall
    elif dungeon_enter.lower == "no":
        print("Fine, ya weenie!")
    else:
        print("Come again?")
        dungeon_enter =input("Try again, sport. \"Yes\" or \"No?\"\n")