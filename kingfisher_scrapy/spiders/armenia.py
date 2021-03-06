import scrapy

from kingfisher_scrapy.base_spider import LinksSpider
from kingfisher_scrapy.util import parameters


class Armenia(LinksSpider):
    """
    Spider arguments
      sample
        Download only the first release package in the dataset.
    """
    name = 'armenia'
    data_type = 'release_package'
    next_pointer = '/next_page/uri'
    next_page_formatter = staticmethod(parameters('offset'))

    def start_requests(self):
        url = 'https://armeps.am/ocds/release'
        yield scrapy.Request(url, meta={'file_name': 'offset-0.json'})
