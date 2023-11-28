# Exercises: Level 1

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years

your_age = int(input("Enter your age: "))
if your_age >= 18:
    print("You are old enough to drive")
else:
    print(f"You need {18 - your_age} more years to learn to drive.")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' 
# for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

my_age = 22
if your_age > my_age:
    print(f"You are {your_age - my_age} years older than me.")
elif your_age < my_age:
    print(f"I {my_age - your_age} years older than you.")
else:
    print("Equel")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b

first_num = int(input("Enter your age: "))
second_num = int(input("Enter your age: "))
if first_num > second_num:
    print(f"{first_num} > {second_num}")
elif first_num < second_num:
    print(f"{first_num} < {second_num}")
else:
    print("Equel")

# Exercises: Level 2

# Write a code which gives grade to students according to theirs scores

score = 61

if score >= 80 and score <= 100:
    print("A")
elif score >= 70 and score <= 79:
    print("B")
elif score >= 60 and score <= 69:
    print("C")
elif score >= 50 and score <= 59:
    print("D")
else:
    print("F")

# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

mounth = "Autumn"
if mounth == "September" or mounth == "October" or mounth == "November":
    print("Autumn")
elif mounth == "December" or mounth == "January" or mounth == "February":
    print("Winter")
else:
    print("Summer")

# The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruit = "lemon"
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)
