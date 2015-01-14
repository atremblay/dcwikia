from image import Image
from urllib import request
from bs4 import BeautifulSoup

class Comic(object):
    """docstring for Comic"""
    def __init__(self, url):
        self.url = url
        self.covers = list()

        req = request.urlopen(self.url)
        the_page = req.read()
        soup = BeautifulSoup(the_page)

        div = soup.findAll('div', attrs={'class': 'floatnone'})[0]
        main = div.findAll('a')[0]
        self.add_cover(main.attrs['href'])

        table = soup.findAll('table',
            attrs={'class': 'collapsible collapsed'})[0]
        links = table.findAll('a', attrs={'class': 'image image-thumbnail'})
        for link in links:
            self.add_cover(link.attrs['href'])
        
    def add_cover(self, url):
        self.covers.append(Image(url))

    def download_covers(self):
        for cover in self.covers:
            cover.download()
