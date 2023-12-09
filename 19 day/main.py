import json


# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words
# d) Read melina_trump_speech.txt file and count number of lines and words

with open('C:/Users/Nikita/Desktop/30DaysOfPython/19 day/files/obama_speech.txt') as f:
    lines = f.read().splitlines()
    print("Lines ", len(lines))
    sum = 0
    for line in lines:
        sum += len(line)
    print("Words ", sum)

with open('C:/Users/Nikita/Desktop/30DaysOfPython/19 day/files/michelle_obama_speech.txt') as f:
    lines = f.read().splitlines()
    print("Lines ", len(lines))
    sum = 0
    for line in lines:
        sum += len(line)
    print("Words ", sum)

with open('C:/Users/Nikita/Desktop/30DaysOfPython/19 day/files/donald_speech.txt') as f:
    lines = f.read().splitlines()
    print("Lines ", len(lines))
    sum = 0
    for line in lines:
        sum += len(line)
    print("Words ", sum)

with open('C:/Users/Nikita/Desktop/30DaysOfPython/19 day/files/melina_trump_speech.txt') as f:
    lines = f.read().splitlines()
    print("Lines ", len(lines))
    sum = 0
    for line in lines:
        sum += len(line)
    print("Words ", sum)

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

def most_spoken_languages(filename = 'C:/Users/Nikita/Desktop/30DaysOfPython/19 day/files/countries_data.json', count = 10):
    with open(filename) as f:
        lines = f.read()
        country_dist = {}
        country_str = []
        person_dct = json.loads(lines)
        for i in person_dct:
            for j in i['languages']:
                country_str.append(j)
        num = 0
        for i in country_str:
            if not i in country_dist:
                country_dist[i] = country_str.count(i)
            num = num + 1
        sorted_dict = dict(sorted(country_dist.items(), key=lambda item: item[1]))
        res = dict(reversed(list(sorted_dict.items())))
        num = 0
        for i in res:
            print(res[i], i)
            if num >= count - 1:
                break
            num = num + 1

most_spoken_languages('C:/Users/Nikita/Desktop/30DaysOfPython/19 day/files/countries_data.json', 3)

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

def most_populated_countries(filename = 'C:/Users/Nikita/Desktop/30DaysOfPython/19 day/files/countries_data.json', count = 10):
    with open(filename) as f:
        lines = f.read()
        country_list = []
        person_dct = json.loads(lines)
        num = 0
        for i in person_dct:
            arr = [i['name'], i['population']]
            country_list.append(arr)
        country_list.sort(key = lambda x: x[0], reverse = True)
        country_list.sort(key = lambda x: x[1], reverse=True)
        num = 0
        for i in country_list:
            if num > count - 1:
                break
            print(i)
            num = num + 1
most_populated_countries('C:/Users/Nikita/Desktop/30DaysOfPython/19 day/files/countries_data.json', 3)

# 