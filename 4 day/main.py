# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
thirty = "Thitry"
days = "Days"
of = "of"
python = "Python"
str = (f"{thirty} {days} {of} {python}")
print(str)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

coding = "Coding"
forStr = "For"
all = "All"
str = (f"{coding} {forStr} {all}")
print(str)

# Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# Print the variable company using print().

print(company)

# Print the length of the company string using len() method and print().

print(len(company))

# Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Change all the characters to lowercase letters using lower() method.

print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.

print(company[1:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.index("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.

print(company.replace("Coding", "Python"))