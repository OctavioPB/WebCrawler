from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

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
            phone = info.find('div', {'class': 'phones phone primary'}).get_text()
            address = info.find('div', {'class': 'street-address'}).get_text()
            locality = info.find('div', {'class': 'locality'}).get_text()

            row = (name, categories, phone, address, locality)
            infoIterable.append(row)

            with open('results2.csv', 'w', newline='') as scrappy:
                writer = csv.writer(scrappy)
                writer.writerows(infoIterable)
        except:
            print(infoIterable)

def urlmaker(citylist):

    for city in citylist:
        #print(city)
        city = city.replace(' ', '+')
        url = 'https://www.yellowpages.com/search?search_terms=dairy+farm&geo_location_terms=' + city + '%2C+CA'
        urllist.append(url)
    return urllist
    #scrapper(url)

''' Start of the program'''

cities = ('Fresno', 'Los Angeles', 'Sacramento', 'San Diego', 'Modesto', 'Irvine', 'San Bernardino')
iter = urlmaker(cities)
print(iter)
for url in iter:
    scrapper(url)
