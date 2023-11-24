# Declare an empty list

emptyList = []

# Declare a list with more than 5 items

fiveItems = [1, 2, 3, 4, 5]

# Find the length of your list

print(len(fiveItems))

# Get the first item, the middle item and the last item of the list

print(fiveItems[0])
print(fiveItems[2])
print(fiveItems[len(fiveItems) - 1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Nikita", 22, 174, "single", "Russia..."]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()

print(it_companies)

# Print the number of companies in the list

print(len(it_companies))

# Print the first, middle and last company

middle = (len(it_companies)) // 2
print(it_companies[0])
print(it_companies[middle])
print(it_companies[len(fiveItems) - 1])

# Print the list after modifying one of the companies

it_companies[0] = "VK"
print(it_companies)

# Add an IT company to it_companies

it_companies.append("Facebook")
print(it_companies)

# Insert an IT company in the middle of the companies list

middle = (len(it_companies)) // 2
it_companies.insert(middle, "Intel")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '

# Check if a certain company exists in the it_companies list.

print("IBM" in it_companies)

# Sort the list using sort() method

it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method

it_companies.sort(reverse=True)
print(it_companies)