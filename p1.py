from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

#############main############
title = getTitle('http://pythonscraping.com/pages/page1.html')


if title == None:
    print('Title coule not be found')
else:
    print(title)