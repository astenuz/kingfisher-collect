import tarfile
from io import BytesIO

import scrapy

from kingfisher_scrapy.base_spider import BaseSpider
from kingfisher_scrapy.util import handle_http_error


class DigiwhistBase(BaseSpider):
    skip_latest_release_date = 'JSON Lines is not supported'

    def start_requests(self):
        # See scrapy.spiders.Spider.start_requests
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, meta={'file_name': 'file.tar.gz'})

    @handle_http_error
    def parse(self, response):
        yield self.build_file_from_response(response, data_type='tar.gz', post_to_api=False)

        # Load a line at the time, pass it to API
        with tarfile.open(fileobj=BytesIO(response.body), mode="r:gz") as tar:
            with tar.extractfile(tar.getnames()[0]) as readfp:
                yield from self.parse_json_lines(readfp, url=self.start_urls[0], data_type='release_package')
