#! python3
# Saves and loads pieces of text to the clipboard

"""
=============================================
Octavio Perez
Web scrapping Tutorial 1
IN: https://www.linkedin.com/in/operezbravo/
GIT: https://github.com/OctavioPB
=============================================
"""

import os, requests, bs4

url = 'https://xkcd.com' #Main Url
os.makedirs('xkcd', exist_ok=True) #Create a folder for downloads in root

while not url.endswith('#'): # iterates as long as the page is valid
    print('Downloading page %s...' %url) 
    res = requests.get(url) #Download the html from the page as a request object
    res.raise_for_status()# raise a status error for HHTP errors

    soup = bs4.BeautifulSoup(res.text) # create the BS object
    comicElem = soup.select('#comic img')# select img element inside comic element
    if comicElem == []: # in the case bs is not able to find a 'comic' tag it will print
        print('Could not find comic image')
        
    else:

        try: # Try to go to the URL of an especific page
            comicUrl = 'http:' + comicElem[0].get('src') # Access the url where the img is hosted
            print('Downloading Image %s...' % (comicUrl))# print url source
            res = requests.get(comicUrl)# Create a requests get object from comic url source
            res.raise_for_status() # Raise a HTTP error if something goes wrong
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            # create the img file by merging the base path and the xkcd folder, and write binary the file
            
            for chunk in res.iter_content(1000000): # Generate data chunks from the image bit content 
                imageFile.write(chunk) # create a file by merging the data chunks
            imageFile.close() # close image file
            
        except: # In case the image could not be downloaded it will print message and go to next iteration
            print('Image could not be saved')

    prevLink = soup.select('a[rel="prev"]')[0]# Bs select the location with the link to previous comic
    url = 'http://xkcd.com' + prevLink.get('href')# Navigate to the previous comic
print('DONE!') # Congrats
