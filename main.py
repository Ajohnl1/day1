# screen output
first_name: str = "Fred"
#first_name is a variable after the = sign in quotes is called a string. ex. "Fred"
print(first_name)

# initalizing variales
my_first_int: int = 3
#int claims integer for numbers
print(my_first_int)

'''
prompt = "What is your name? "
n = input()
print()
'''
# triple quotes creates string to comment out code if needed
# PEP = Python Enhancement Proposal (Good practice standards for coding in python for users to have universal understanding)

    # Getting input from the user
#prompt: str = "What is your name? "
#response = input(prompt)
#print(response)
    # input is a keyword.
    # Try to document what each each variable is to help self document what inputs are for.
    # Try to comment for each section for yourself and other users if they are looking at your code

# division: /
    # adding division for math
# backslash: \
    # if you need to add a backslash in code add two Ex. (first_name: str = "Fred \\")
# adding\n after will add a new line after print
    # Ex. (first_name: str = "Fred\n")

# exploring backslash
# Screen output
first_name: str = "Fred \\ \n"
print(first_name)

# exploring f-string
print(f"The first name is: {first_name}")
print(f"The first integer is: {my_first_int}")