# Write a function which generates a six digit/character random_user_id. 

import string
from random import random, randint

dit_and_characters = string.digits + string.ascii_letters + string.digits

def random_user_id():
    a = ""
    for i in range(7):
        a += dit_and_characters[randint(0, 71)]
    return a
print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user():
    num_characters = 7
    num_IDs = 4
    for i in range(num_IDs - 1):
        a = ""
        for i in range(num_characters + 1):
            a += dit_and_characters[randint(0, 71)]
        print(a)
user_id_gen_by_user()

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    return f"rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})"
print(rgb_color_gen())
