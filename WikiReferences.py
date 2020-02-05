from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

linkList = []
linkURL = []
row = []

def wikiscrapper(urllist):
    for url in urllist:
        print(url)
        html = urlopen(url)

        bs = BeautifulSoup(html, 'html.parser')
        container = bs.find('div', {'id': 'bodyContent'})
        linkRe = re.compile('^(/wiki/)((?!:).)*$')
        links = container.find_all('a', href=linkRe)
        for link in links:
            if 'href' in link.attrs:

                column1 = link.attrs['title']
                column2 = link.attrs['href']
                row.append([column1.encode(encoding="UTF-8"), column2.encode(encoding="UTF-8")])

                with open('wikires.csv', 'w', newline='') as csvfile:
                    try:
                        wikiwriter = csv.writer(csvfile)
                        wikiwriter.writerows(row)
                    except:
                        print(column1+' Skipped because encoding')

                linkList.append(link.attrs['title']) # regresa una lista que contiene los titulos de todos los articulos con referencias
                linkURL.append(link.attrs['href'])

    return #linkList, linkURL

def urlmaker(list):
    urllist = []
    for article in list:
        article = article.replace(' ', '_')
        url = ('https://en.wikipedia.org/wiki/' + article)
        urllist.append(url)
    return urllist

articles = ('Combination', 'Computer scientist', 'Mathematician', 'Charles Kingsley', 'Evolution')
urllist = urlmaker(articles)
#wikiscrapper(urllist)
wikiscrapper(urllist)
#print(urllist)
