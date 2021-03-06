import scrapy

from kingfisher_scrapy.base_spider import LinksSpider
from kingfisher_scrapy.util import parameters


class HondurasPortalRecords(LinksSpider):
    """
    API documentation
      http://www.contratacionesabiertas.gob.hn/manual_api/
    Swagger API documentation
      http://www.contratacionesabiertas.gob.hn/servicio/
    Spider arguments
      sample
        Download only the first record package in the dataset.
    """
    name = 'honduras_portal_records'
    data_type = 'record_package'
    data_pointer = '/recordPackage'
    next_pointer = '/next'
    next_page_formatter = staticmethod(parameters('page'))
    skip_latest_release_date = 'Already covered (see code for details)'  # honduras_portal_releases

    download_delay = 0.9

    def start_requests(self):
        url = 'http://www.contratacionesabiertas.gob.hn/api/v1/record/?format=json'
        yield scrapy.Request(url, meta={'file_name': 'page-1.json'})
