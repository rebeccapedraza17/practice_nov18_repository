# Rebecca Pedraza
# Nov 18

# Create a function called make_random_list(num, range_start, range_end)
# The function will return a list filled with num random numbers
# Between num_start and num_end

import random

def make_random_list(num, range_start, range_end):
    a = [] # My function return something. # Num controls how many things in list
    for i in range(num):
        # Inside loop make a new random number and add it to list
        new = random.randint(start, end)
        # Add it to list
    a.append(new)
    return a
    pass

def ask_for_list(): # Create a function
    a = int(input("num"))
    b = int(input("range_start"))
    c = int(input("range_end"))
    # Input the values
    return make_random_list(a,b,c)
    # Call make_random_list with the values given
    
