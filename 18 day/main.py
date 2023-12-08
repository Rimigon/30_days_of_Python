import re

# What is the most frequent word in the following paragraph?

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
split_p = paragraph.replace(".", " ").split()
print(split_p)

result = {}

for elem in split_p:
    result[elem] = f'количество: {split_p.count(elem)}'

print(result)

