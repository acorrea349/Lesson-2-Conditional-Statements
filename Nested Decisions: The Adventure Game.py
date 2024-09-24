# Task 1: Code Correction You are provided with a Python script that 
# is supposed to guide a user through an adventure game, but it has some errors. 
# Identify and fix them.

# Buggy Code:

# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")

# Task 2: Setting the Scene

# Based on your corrected code from Task 1, expand the game. 
# If the user chooses "cave", ask them if they want to "light a torch" or "proceed 
# in the dark", and provide outcomes for each decision.


# Task 3: Default Path

# If the user makes an invalid choice at any point, incorporate a pass statement 
# to handle it. HINT: How can an else statement be of use here?

place = input("Choose a place: forest or cave? ")



if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    print("You find a hidden treasure!")
    cave = input("Would you like want to light a torch or proceed in the dark? ")
    if cave == "light a torch":
        print("Congratulations you found your way out.")
    elif cave == "proceed in the dark":
        print("You have been walking around for hours, you are lost")
        torch = input("Would you like to light a torch, yes/no? ")
        if torch == "yes":
            print("Congratulations you found your way out.")
        elif torch == "no":
            print("You have fallen asleep, try again tomorrow.")
        else:
            pass
    else:
        pass
else:
    pass