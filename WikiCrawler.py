from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
''' This program crawls wikipedia articles that the program hsve not visited before to avoid duplicate entries, 
then obtains the title, the first paragraph, and navigate to another article'''
pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org/wiki/Combinatorics'.format(pageUrl))  # Read the wikipedia article
    bs = BeautifulSoup(html, 'html.parser')  # Uses the html parser in the BS object
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span')
              .find('a').attrs['href'])
    except AttributeError:  # if something is missing it will print it
        print('This page is missing something! Continuing.')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We have encountered a new page
                newPage = link.attrs['href']# Get attributes unly from href html tag
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks('')# Call the getLinks Function
