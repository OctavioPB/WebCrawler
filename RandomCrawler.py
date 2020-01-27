from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

''' This program crawls wikipedia and obtains the title, the first paragraph, and navigate to a random wiki article'''

random.seed(datetime.datetime.now())
# Set the random seed


def getLinks(articleUrl):
    # Method to parse and format the article URL and return the articles in the html div containers
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    # Regular expression to format the urls obtained to the format '/wiki/article'


links = getLinks('/wiki/Combinatorics')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    # Set of the random article navigated
    print(newArticle)
    links = getLinks(newArticle)


