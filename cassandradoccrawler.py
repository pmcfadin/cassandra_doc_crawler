from scrapy.crawler import CrawlerProcess
from cassandradocspider import CassandraDocSpider

deny_list = ['https://www.apache.org', 'https://cassandra.apache.org/_/blog/',
             'https://cassandra.apache.org/_/case-studies', 'https://cassandra.apache.org/doc/3.11']  # List of URLs to deny
process = CrawlerProcess()

process.crawl(CassandraDocSpider, start_url='https://cassandra.apache.org/doc/latest/',
              output_dir='output/cassandra_docs', deny_list=deny_list)

process.start()
