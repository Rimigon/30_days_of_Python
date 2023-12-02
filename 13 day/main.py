# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero)

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

dimensional_list = [number for row in list_of_lists for number in row]
print(dimensional_list)

# Using list comprehension create the following list of tuples:

numbers = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i** 5 ) for i in range(11)]
for row in numbers:
    print(row)

