# Exercises: Level 1

# Iterate 0 to 10 using for loop, do the same using while loop.

for num in range(11):
    print(num)

i = 0
while i <= 10:
    print(i)
    i += 1

# Iterate 10 to 0 using for loop, do the same using while loop.

for num in reversed(range(11)):
    print(num)

i = 10
while i >= 0:
    print(i)
    i -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

sharp = "#"
for num in range(8):
    print(sharp)
    sharp += "#"

# Use nested loops to create the following:

for i in range(8):
    for j in range(8):
        print('#', end='  ')
    print()

# Print the following pattern

for i in range(11):
    print(f"{i} x {i} = {i * i}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lang in languages:
    print(lang)

# Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(101):
    if i % 2 == 0:
        print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(101):
    if i % 2 != 0:
        print(i)

# Exercises: Level 2

# Use for loop to iterate from 0 to 100 and print the sum of all numbers

sum = 0
for i in range(101):
    sum += i
print("The sum of all numbers is ", sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

odd_sum = 0
even_sum = 0
for i in range(101):
    if i % 2 != 0:
        odd_sum += i
    else:
        even_sum += i

print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")