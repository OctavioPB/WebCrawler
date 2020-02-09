"""
=============================================
Octavio Perez

Web scrapping Tutorial 2
IN: https://www.linkedin.com/in/operezbravo/
GIT: https://github.com/OctavioPB
=============================================
"""


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import csv
import pandas as pd

linkList = []
infoIterable = []
urllist = []

''' Custom made function to scrap Yellow Pages website'''

def scrapper(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    infoContainer = bs.find_all('div', {'class': 'v-card'})

    for info in infoContainer:
        try:
            name = info.find('a', {'class': 'business-name'}).get_text()
            categories = info.find('div', {'class': 'categories'}).get_text()
            try:
                phone = info.find('div', {'class': 'phones phone primary'}).get_text()
            except:
                phone = "No phone"
            try:
                address = info.find('div', {'class': 'street-address'}).get_text()
            except:
                address = info.find('p', {'class': 'adr'}).get_text()
            try:
                locality = info.find('div', {'class': 'locality'}).get_text()
            except:
                locality = url.replace('https://www.yellowpages.com/search?search_terms=dairy+farm&geo_location_terms=',
                                       '')
                locality = locality.replace('%2C+CA', '')
                locality = locality.capitalize()

            row = (name, categories, phone, address, locality)
            infoIterable.append(row)

            with open('results.csv', 'w', newline='') as scrappy:
                writer = csv.writer(scrappy)
                writer.writerows(infoIterable)
        except:
            print('Class Error')
            continue

''' Generate the list of yellow pages URLs '''

def urlmaker(citylist):
    for city in citylist:
        # print(city)
        city = city.replace(' ', '+')
        url = 'https://www.yellowpages.com/search?search_terms=dairy+farm&geo_location_terms=' + city + '%2C+CA'
        urllist.append(url)
    return urllist
    # scrapper(url)


''' Start of the program'''

cities = ('arbuckle', 'alameda', 'alamo', 'albany',
          'albion', 'alderpoint', 'alhambra',
          'aliso viejo', 'alleghany', 'alpaugh',
          'alpine', 'alta', 'altadena',
          'angelus oaks', 'Sacramento', 'Los Angeles')

iter = urlmaker(cities)
print(iter)
for url in iter:
    try:
        scrapper(url)
        print(url)

    except HTTPError as e:
        print(url, ' No farms found')
        continue

infoIterable = pd.DataFrame(infoIterable)
tttessstttt = infoIterable.to_csv(r'C:\\Users\\IT\\Documents\\python\\testit.csv')

