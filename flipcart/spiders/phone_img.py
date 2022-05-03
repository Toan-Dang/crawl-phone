
import scrapy
import pandas as pd


def read_csv():
    df = pd.read_csv('Products.csv')
    return df['url'].values.tolist()

class detailSpider(scrapy.Spider):
    name = 'image'


    def start_requests(self):
        for url in read_csv():
            yield scrapy.Request(url)


    def parse(self, response):
        url_csv = response.url
        id = ''
        df = pd.read_csv('Products.csv')
        for i in range(df['url'].shape[0]):
            if url_csv == df['url'][i]:
                id = df['_id/$oid'][i]

        for r in response.css('img.q6DClP'):
            img = r.attrib['src']
            yield{
                'id': id,
                'img': img,
              
            }

        