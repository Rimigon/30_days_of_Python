# Exercises: Level 1

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(2, 4))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(radius):
    return 3.14 * radius * radius
print(area_of_circle(5))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    sum = 0
    for i in nums:
        if(type(i) == int):
            sum += i
        else:
            return "Error"
    return sum
print("Sum all: ", add_all_nums(2, 5, 7, 1, 5))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit

def convert_celsius_to_fahrenheit(cels):
    return (cels * 9 / 5) + 32
print(convert_celsius_to_fahrenheit(50))
