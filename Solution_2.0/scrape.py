import urllib
from bs4 import BeautifulSoup


def scrape(url):

    return urllib.request.urlopen(url).read()
