# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import json
import requests
from bs4 import BeautifulSoup
url = 'https://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
# print(soup.body) # gives the whole page on the website
print(response.status_code)

row_list = soup.find_all('li', {"class": "list-item"})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
# row = row_list[0] # the result is a list, we are taking out data from it
text = ''
# print(row_list[0])
for td in row_list:
    text = text + td.get_text()
text = [i for i in text.split("\n") if i]
# print(text)


trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_json = {'stat': text}

with open('C:/Users/Nikita/Desktop/30DaysOfPython/22 day/sw_templates.json', 'w') as f:
    f.write(json.dumps(to_json, indent=4))

