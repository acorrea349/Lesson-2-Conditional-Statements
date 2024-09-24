# Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)


# Task 2: Venue Selection

# Based on the corrected code from Task 1, further enhance your code to recommend additional things like 
# "audio system" or "projector" based on the number of attendees.


attendees = int(input("Enter number of attendees: "))
venue = input("""Large Hall
Would you like to add an audio system or a projector? """) if attendees > 100 else input("""Conference Room
Would you like to add an audio system or a projector? """)

if venue == "audio system":
    print("Great we will add an Audio System to your venue.")
    food = input("Do you want vegetarian food, yes/no? ")
    if food == "yes":
        print("Excellent, we will recommend Veggie Delight Caterers")
    elif food == "no":
        print("Excellent, we will recommend Gourmet Meals Caterers")
    else:
        pass
elif venue == "projector":
    print("Great we will add a Projector to your venue.")
    food = input("Do you want vegetarian food, yes/no? ")
    if food == "yes":
        print("Excellent, we will recommend Veggie Delight Caterers")
    elif food == "no":
        print("Excellent, we will recommend Gourmet Meals Caterers")
    else:
        pass
else:
    pass
print("Thank you for booking with us, we hope to exceed your expectations.")


