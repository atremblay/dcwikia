from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class DCwikiaSpider(CrawlSpider):
    name = "dcwikia"
    allowed_domains = ["dc.wikia.com"]
    start_urls = [
        "http://dc.wikia.com/wiki/The_New_52"
    ]
    rules = (
        Rule(
            LinkExtractor(),
            callback='parse_textless',
            follow=True
        ),
    )
    textless_images = set()

    def parse_textless(self, response):
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
#                     self.textless_images.append(b.attrs['href'])
                    filename = 'textless.txt'
                    with open(filename, 'ab+') as f:
                        f.write(b.attrs['href'])
                        f.write('\n')
                        f.flush()
        except:
            pass
