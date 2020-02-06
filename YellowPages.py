from urllib.request import urlopen
from urllib.error import  HTTPError
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
            try:
                phone = info.find('div', {'class': 'phones phone primary'}).get_text()
            except:
                phone = 'No phone'
            try:
                address = info.find('div', {'class': 'street-address'}).get_text()
            except:
                address = info.find('p', {'class': 'adr'}).get_text()
            try:
                locality = info.find('div', {'class': 'locality'}).get_text()
            except:
                locality = info.find('p', {'class': 'adr'}).get_text()
            row = (name, categories, phone, address, locality)
            infoIterable.append(row)

            with open('results3.csv', 'w', newline='') as scrappy:
                writer = csv.writer(scrappy)
                writer.writerows(infoIterable)
        except:
            print('class Error')
            continue

def urlmaker(citylist):

    for city in citylist:
        #print(city)
        city = city.replace(' ', '+')
        url = 'https://www.yellowpages.com/search?search_terms=dairy+farm&geo_location_terms=' + city + '%2C+CA'
        urllist.append(url)
    return urllist


''' Start of the program'''

cities =  ('alameda', 'alamo', 'albany',
          'albion', 'alderpoint','arbuckle', 'alhambra', 'aliso viejo',
          'alleghany', 'alpaugh', 'alpine', 'alta', 'altadena',
          'angelus oaks')

iter = urlmaker(cities)
print(iter)

for url in iter:
    try:
        scrapper(url)
        print(url)

    except HTTPError as e:
        print(url, ' No farms founded')
        continue
