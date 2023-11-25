# Exercises: Level 1

# Create an empty tuple

emptyTuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothersTuple = ('Koliy', 'Zhenia')
sistersTuple = ('Nastya', 'Alena')

# Join brothers and sisters tuples and assign it to siblings

sublingsTuple = brothersTuple + sistersTuple

# How many siblings do you have?

print(len(sublingsTuple))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

parent = ('Nadezda', 'Mikhail')
family_members = parent + sublingsTuple

# Exercises: Level 2

# Unpack siblings and parents from family_members

mother, father, *sublings = family_members

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp

fruits = ('Apple', 'Banana', 'Peach')
vegetables = ('Tomato', 'Cucumber', 'Carrot')
animal = ('Chicken', 'Cow', 'Fish')

food_stuff_tp = fruits + vegetables + animal

# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

middleIndex = len(food_stuff_tp) // 2
print(food_stuff_tp[0:middleIndex - 1] + food_stuff_tp[middleIndex + 1: ])

# Slice out the first three items and the last three items from food_staff_lt list

print(food_stuff_lt[3: len(food_stuff_lt) - 3])

# Delete the food_staff_tp tuple completely

del food_stuff_tp

# Check if an item exists in tuple:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estoni' in nordic_countries)
print('Iceland' in nordic_countries)