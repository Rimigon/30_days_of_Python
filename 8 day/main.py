# Create an empty dictionary called dog

dog = {}

# Add name, color, breed, legs, age to the dog dictionary

dog['name'] = 'Bars'
dog['color'] = 'Black'
dog['legs'] = 4
dog['age'] = 5
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name': 'Nik',
    'last_name': 'Rad',
    'gender': "male",
    'age': 22,
    'marital_status': 'single',
    'skills': ['HTML', 'CSS', 'JS'],
    'country': 'Russia',
    'city': 'Moscow'
}

# Get the length of the student dictionary

print(len(student))

# Get the value of skills and check the data type, it should be a list

print(student['skills'])
print(type(student['skills']))

# Modify the skills values by adding one or two skills

student['skills'].append("C#")
print(student['skills'])

# Get the dictionary keys as a list

print(student.keys())

# Get the dictionary values as a list

print(student.values())

# Change the dictionary to a list of tuples using items() method

print(student.items())

# Delete one of the items in the dictionary

student.popitem()
print(student)

# Delete one of the dictionaries

del student
