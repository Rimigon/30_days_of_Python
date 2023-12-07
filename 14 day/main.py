countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_new = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from functools import reduce

# Use for loop to print each country in the countries list.

for i in countries:
    print(i)

# Use for to print each name in the names list.

for i in names:
    print(i)

# Use for to print each number in the numbers list. 

for i in numbers:
    print(i)

# Use map to create a new list by changing each country to uppercase in the countries list

upper_countries = map(lambda country: country.upper(), countries)
print(list(upper_countries))

# Use map to create a new list by changing each number to its square in the numbers list

square_list = list(map(lambda x: x ** 2, numbers))
print(square_list)

# Use map to change each name to uppercase in the names list

upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)

# Use filter to filter out countries containing 'land

def is_land(country):
    if 'land' in country:
        return True
    return False
countries_with_land = list(filter(is_land, countries))
print(countries_with_land)

# Use filter to filter out countries having exactly six characters.

def six_characters(country):
    if len(country) == 6:
        return True
    return False
countries_six_characters = list(filter(six_characters, countries))
print(countries_six_characters)

# Use filter to filter out countries containing six letters and more in the country list.

def six__more_characters(country):
    if len(country) >= 6:
        return True
    return False
countries_six_more_characters = list(filter(six__more_characters, countries))
print(countries_six_more_characters)

# Use filter to filter out countries starting with an 'E'

def start_with_E(country):
    if country.startswith("E"):
        return True
    return False
countries_start_E = list(filter(start_with_E, countries))
print(countries_start_E)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

def get_string_lists(lst):
    return list(filter(lambda x : isinstance(x, str), lst))
print(get_string_lists([1, 2, "hello", "qwe"]))

# Use reduce to sum all the numbers in the numbers list.

def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers)
print(total)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

def countries_conc(x, y):
    if y == "Iceland":
        return x + " and " + y + " are north European countries"
    return x +", " + y
total = reduce(countries_conc, countries)
print(total)

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

def caregorize_countries():
    return filter(lambda country: "land" in country, countries_new)
print(list(caregorize_countries()))
