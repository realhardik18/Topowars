import requests
import random
import json
import urllib.request
from creds import api_key_pixbay
import requests
from PIL import Image
import ast
from bs4 import BeautifulSoup

# returns random country


def randomCountry():
    with open('CountriesAndCities.json') as f:
        data = json.load(f)
        countries = [c['country'] for c in data['data']]
    return random.choice(countries)

# returns a random city from a country given


def randomCity(country):
    with open('CountriesAndCities.json') as f:
        data = json.load(f)
    for d in data['data']:
        if d['country'].lower() == country.lower():
            return random.choice(d['cities'])

# reutrns the flag of the country specified


def flagOfCountry(country):
    with open('CountriesAndCities.json') as f:
        data = json.load(f)
    for d in data['data']:
        if d['country'].lower() == country.lower():
            url = f"https://flagcdn.com/256x192/{d['iso2'].lower()}.png"
            fileid = random.randint(000000, 999999)
            #urllib.request.urlretrieve(url, f"{fileid}.png")
            urllib.request.urlretrieve(
                "http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")
            return f"flag of {country} saved as {fileid}.png"
            # work on this!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# returns a random picture of the country


def randomPicOfCountry(country):
    filename = random.randint(000000, 99999)
    country = country.replace(" ", "+")
    response = requests.get(
        f'https://pixabay.com/api/?key={api_key_pixbay}&q={country}&image_type=photo')
    urlToPic = random.choice(ast.literal_eval(
        response.text)['hits'])['largeImageURL']
    BASE = 'https://render-tron.appspot.com/screenshot/'
    path = f'{filename}.jpg'
    response = requests.get(BASE + urlToPic, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
    return [filename, country]

# returns n random country, where n is the input


def randomCountries(count):
    countries = []
    while len(countries) != count:
        country = randomCountry()
        if country not in countries:
            countries.append(country)
        else:
            pass
    return countries


def randomCities(count, country):
    cities = []
    while len(cities) != count:
        countryi = randomCountry()
        if countryi != country:
            city = randomCity(countryi)
            if city not in cities:
                cities.append(city)
    return cities


#print(randomCities(3, 'India'))

# random pic of country
# captial func

# randomPicOfCountry('india')
# print(flagOfCountry(randomCountry()))
# print(randomCountry())
#print(randomPicOfCountry(randomCountry().replace(' ', '')))
# print(randomCountries(5))

# work on better ooics
# print(randomPicOfCountry(randomCountry()))
