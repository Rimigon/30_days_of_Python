# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Find the length of the set it_companies

print(len(it_companies))

# Add 'Twitter' to it_companies

it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies

it_companies.update({'Intel', 'AMD'})
print(it_companies)
      
# Remove one of the companies from the set it_companies

it_companies.pop()

# What is the difference between remove and discard 
# discard - without errors, remove - error

# Exercises: Level 2

# Join A and B

print(A.isdisjoint(B))

# Find A intersection B

print(A.intersection(B))