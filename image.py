import os
from urllib import request


class Image(object):
    """docstring for Image"""
    def __init__(self, url):
        super(Image, self).__init__()
        self.url = url
        self.name = os.path.basename(self.url)

    def download(self, destination=None):
        if destination is None:
            destination = self.name
        else:
            destination = os.path.join(destination, self.name)
        request.urlretrieve(self.url, destination)

    def is_textless(self):
        return 'textless' in self.name.lower()
