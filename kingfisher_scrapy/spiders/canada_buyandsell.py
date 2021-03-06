from kingfisher_scrapy.base_spider import SimpleSpider
from kingfisher_scrapy.util import components


class CanadaBuyAndSell(SimpleSpider):
    """
    API documentation
      https://buyandsell.gc.ca/procurement-data/open-contracting-data-standard-pilot/download-ocds-pilot-data
    Spider arguments
      sample
        Downloads a release package with data for the oldest fiscal year available (2013-2014).
    """
    name = 'canada_buyandsell'
    data_type = 'release_package'
    ocds_version = '1.0'

    def start_requests(self):
        urls = [
            'https://buyandsell.gc.ca/cds/public/ocds/tpsgc-pwgsc_ocds_EF-FY-16-17.json',
            'https://buyandsell.gc.ca/cds/public/ocds/tpsgc-pwgsc_ocds_EF-FY-15-16.json',
            'https://buyandsell.gc.ca/cds/public/ocds/tpsgc-pwgsc_ocds_EF-FY-14-15.json',
            'https://buyandsell.gc.ca/cds/public/ocds/tpsgc-pwgsc_ocds_EF-FY-13-14.json',
        ]
        if self.sample:
            urls = [urls[0]]

        for url in urls:
            yield self.build_request(url, formatter=components(-1))
