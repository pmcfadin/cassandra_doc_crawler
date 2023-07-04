from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse
import json
import os
from bs4 import BeautifulSoup


class CassandraDocSpider(CrawlSpider):
    name = 'cassandra_doc_spider'

    def __init__(self, *args, **kwargs):
        self.start_urls = [kwargs.get('start_url')]
        self.allowed_domains = [urlparse(self.start_urls[0]).netloc]
        self.rules = [
            Rule(LinkExtractor(deny=kwargs.get('deny_list')), callback=self.parse_item, follow=True),
        ]
        self.output_dir = kwargs.get('output_dir')
        super(CassandraDocSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title using BeautifulSoup
        title = soup.title.string if soup.title else ''

        # Extract body text using BeautifulSoup
        body = ' '.join(soup.body.stripped_strings) if soup.body else ''

        # Store the parsed data
        item = {
            'url': response.url,
            'title': title,
            'body': body,
        }

        # Convert URL to filename by replacing '/' with '_' in the path
        filename = urlparse(response.url).path.replace('/', '_') + ".json"

        # Ensure filename doesn't start with '_'
        if filename[0] == "_":
            filename = filename[1:]

        file_path = os.path.join(self.output_dir, filename)

        with open(file_path, 'w') as f:
            json.dump(item, f)

        return item
