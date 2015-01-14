from urllib import request
from bs4 import BeautifulSoup
from comic import Comic


class Series(object):
    """docstring for Series"""
    def __init__(self, url):
        self.url = url
        self.comics = list()

        req = request.urlopen(self.url)
        the_page = req.read()
        soup = BeautifulSoup(the_page)
        div = soup.findAll('div', attrs={'id': 'mw-content-text'})[0]
        ul = div.findAll('ul')[0]
        links = ul.findAll('a')
        for link in links:
            self.add_comic('http://dc.wikia.com' + link.attrs['href'])

    def add_comic(self, url):
        self.comics.append(Comic(url))
