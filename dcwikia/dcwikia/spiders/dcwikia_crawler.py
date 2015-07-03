import scrapy
from bs4 import BeautifulSoup
import urlparse

class DCwikiaSpider(scrapy.Spider):
    name = "dcwikia"
    # allowed_domains = ["http://dc.wikia.com/"]
    start_urls = [
        "http://dc.wikia.com/wiki/The_New_52",
        "http://dc.wikia.com/wiki/Earth_2_Vol_1"
    ]

    def parse(self, response):
        # print("url: {}".format(response.url))
        self.parse_textless(response)

        for href in response.xpath('//a/@href'):
            url = urlparse.urljoin(response.url, href.extract())
            print("\thref: {}".format(url))
            # url = response.urljoin(href.extract())

            yield scrapy.Request(url, callback=self.parse)


    def parse_textless(self, response):
        print("url: {}".format(response.url))
        try:
            soup = BeautifulSoup(response.body)
            table = soup.find(
                    'table',
                    attrs={'class': 'collapsible collapsed'})
            table_rows = table.findAll('tr')
            for table_row in table_rows:
                div = table_row.findChild('div')
                if "textless" in div.text.lower():
                    b = div.find('a')
#                     textless_images.append(b.attrs['href'])
                    filename = 'textless.txt'
                    with open(filename, 'wb') as f:
                        f.write(b.attrs['href'])
        except:
            pass