from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re
linkList = []
linkURL = []
row = []


def wikiscrapper(url):

    x = 0
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    container = bs.find('div', {'id': 'bodyContent'})
    linkRe = re.compile('^(/wiki/)((?!:).)*$')
    links = container.find_all('a', href=linkRe)
    for link in links:
        if 'href' in link.attrs:
            x = + x

            column1 = link.attrs['title']
            column2 = link.attrs['href']
            rowit = [column1, column2]
            row.append(rowit)
            #row = (column1, column2)

            with open('wikires.csv', 'w', newline='') as csvfile:
                wikiwriter = csv.writer(csvfile)
                wikiwriter.writerows(row)
                #wikiwriter.writerow(linkURL)

            #q = len(link)
            linkList.append(link.attrs['title']) # regresa una lista que contiene los titulos de todos los articulos con referencias
            linkURL.append(link.attrs['href'])


    return linkList, linkURL

wikiscrapper('https://en.wikipedia.org/wiki/Combination')
print(linkList)
#csvLoader(linkList, linkURL)