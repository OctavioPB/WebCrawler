"""
=============================================
Octavio Perez

Web scrapping Tutorial 1
IN: https://www.linkedin.com/in/operezbravo/
GIT: https://github.com/OctavioPB
=============================================
"""

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
                    wikiwriter = csv.writer(csvfile)
                    wikiwriter.writerows(row)
                linkList.append(link.attrs['title'])
                linkURL.append(link.attrs['href'])
    return None

def urlmaker(list):
    urllist = []
    for article in list:
        article = article.replace(' ', '_')
        url = ('https://en.wikipedia.org/wiki/' + article)
        urllist.append(url)
    return urllist

articles = ('Combination',
            'Computer scientist',
            'Mathematician',
            'Charles Kingsley',
            'Charlemagne',
            'Reference')
urllist = urlmaker(articles)
wikiscrapper(urllist)
