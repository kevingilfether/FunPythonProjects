print("We're gonna play some madlibs!")

adjective1 = input("Adjective: ")
plural_noun1 = input("Plural Noun: ")
adjective2 = input("Adjective: ")
plural_noun2 = input("Plural Noun: ")

print("""
                Driving with a trailer
So, the {0} day is here. You've packed all the {1}, moved the {2} {3}
and are ready to bid "adieu" to the old digs! Congratulations!

But... wait. Something mysterious lurks in the background. That's right, you get to drive
with a trailer in tow. Literally, in tow.

Here are some helpful trailer tips:

1. Be sure to load the trailer evenly, but with a little more weight at the front!
A 60-40 balance is best.

2. Always remember, slow and steady wins the race. Driving a little more slowly helps
you and your gas consumption. 

3. Pull out a little further into the intersection than you are used to on right turns. 
Otherwise, your trailer might hop the curb!

4. Most of all, keep your wits about you and drive with normal safe technique.
There is no substitute for careful work.
""".format(adjective1, plural_noun1, adjective2, plural_noun2))