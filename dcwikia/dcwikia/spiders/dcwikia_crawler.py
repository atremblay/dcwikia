from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
import scrapy
import urlparse


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
            tables = soup.findAll(
                    'table',
                    attrs={'class': 'collapsible collapsed'})

            for table in tables:
                try:
                    self.parse_table(table)
                except:
                    continue
        except:
            pass

    def parse_table(self, table):

        table_rows = table.findAll('tr')
        for row in table_rows:
            try:
                self.parse_row(row)
            except:
                continue

    def parse_row(self, row):

        links = row.findAll('a')
        for a in links:
            try:
                href = a.attrs['href']
                if "textless" in href.lower():
                    filename = 'textless.txt'
                    with open(filename, 'a') as f:
                        f.write(href)
                        f.write('\n')
                        f.flush()
            except:
                continue


class Vol2Spider(scrapy.Spider):
    name = "vol2spider"
    # allowed_domains = ["dc.wikia.com"]

    def __init__(self, category=None, *args, **kwargs):
        super(Vol2Spider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://dc.wikia.com/wiki/Category:%s?display=page&sort=mostvisited' % category
        ]
        self.textless_images = set()

    def parse(self, response):
        for href in response.xpath('//a/@href').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_textless)

    def parse_textless(self, response):

        try:
            soup = BeautifulSoup(response.body)
            tables = soup.findAll(
                    'table',
                    attrs={'class': 'collapsible collapsed'})

            for table in tables:
                try:
                    self.parse_table(table)
                except:
                    continue

        except Exception, e:
            print(response)
            print(e)

    def parse_table(self, table):

        table_rows = table.findAll('tr')
        for row in table_rows:
            try:
                self.parse_row(row)
            except:
                continue

    def parse_row(self, row):

        links = row.findAll('a')
        for a in links:
            try:
                href = a.attrs['href']
                if "textless" in href.lower():
                    filename = 'textless2.txt'
                    with open(filename, 'a') as f:
                        f.write(href)
                        f.write('\n')
                        f.flush()
            except:
                continue

        # divs = row.findAll('div')
        # for div in divs:
        #     try:
        #         if "textless" in div.text.lower():
        #             previous_div = div.findPreviousSibling()
        #             b = previous_div.find('a')
        #             filename = 'textless2.txt'
        #             with open(filename, 'a') as f:
        #                 f.write(b.attrs['href'])
        #                 f.write('\n')
        #                 f.flush()
        #     except:
        #         continue

