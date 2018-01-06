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