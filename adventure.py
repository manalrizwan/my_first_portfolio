start = '''
You're in your bed dreaming that you are falling through a rabbit hole; you end up in a farm with a shovel.
There is a barn up in front of you. Behind you there are traintracks.
'''

print(start)

print("Type 'north' to go north or 'south' to go south or 'dig' to dig")
user_input = input()

if user_input == "north":
    print("You decide to go north towards the barn...") # finished the story by writing what happens

    print("Type 'walk' to keep walking and go away from the barn or type 'go in' to go inside the barn")
    user_input = input()
    if user_input == "walk":
        print("You start walking south towards the traintracks and walk into a train and die")

    elif user_input == "go in":
        print("You encounter the clucking chicken")
        print("The cluckling chicken asks you if you want to eat chicken")

    print("Type 'yes' to grab and eat the chicken or type 'no' to not")
    user_input = input()
    if user_input == "yes":
        print("You try to eat the chicken but then it screams")
    elif user_input == "no":
        print("The chicken turns into a witch and eats you")

if user_input == "south":
    print("You choose to go south towards the traintracks. There is a masquerade ball...") # finished the story writing what happens

    print("Do you go the ball, spy on them, or don't go?")
    user_input = input()
    if user_input == "go to the ball":
        print("You dance & live happily ever after")
    elif user_input == "spy on them":
        print("You are seen and get shot")
    elif user_input == "don't go":
        print("You die anyway")

if user_input == "dig":
    print("You decide to dig a hole in the ground and you keep digging ...")
    print("2 weeks after digging you die due to hunger/thirst")
