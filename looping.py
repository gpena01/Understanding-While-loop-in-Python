name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
response = input("{}, do you understand Python while loops?\n(Enter yes/no)".format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops

while response.lower() != "yes":
    response = input("Ok, {}, while loops in Python repeat as long as a certain Boolean condition is met.\n{}, now do you understand Python while loops?\n(Enter yes/no)  ".format(name,name))

print("That's great, {}. I'm pleased that you understand while loops now. That was getting repetitive.".format(name))
    
# TODO: Since the user doesn't understand while loops, let's explain them.


# TODO: Ask the user again, by name, if they understand while loops.

  
# TODO: Outside the while loop, congratulate the user for understanding while loops
 
