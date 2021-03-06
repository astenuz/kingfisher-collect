import scrapy

from kingfisher_scrapy.base_spider import SimpleSpider


class ArgentinaVialidad(SimpleSpider):
    """
    API documentation
      https://datosabiertos.vialidad.gob.ar/ui/index.html#!/datos_abiertos
    Spider arguments
      sample
        Ignored, data is downloaded from a single JSON file.
    """
    name = 'argentina_vialidad'
    data_type = 'release_package_list'

    def start_requests(self):
        url = 'https://datosabiertos.vialidad.gob.ar/api/ocds/package/all'
        yield scrapy.Request(url, meta={'file_name': 'all.json'})
