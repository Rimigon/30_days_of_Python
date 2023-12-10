import requests
url = 'https://api.thecatapi.com/v1/breeds'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
cats = response.json()
for i in cats:
    print(i['weight'])
    print("----------------------")