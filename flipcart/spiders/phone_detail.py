
import scrapy
import pandas as pd
from collections import defaultdict

def read_csv():
    df = pd.read_csv('Products.csv')
    return df['url'].values.tolist()

class imageSpider(scrapy.Spider):
    name = 'detail'


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
        config = {}
  
        for product in response.css('div._3k-BhJ'):
            title = product.css('div.flxcaE::text').get()
            config.clear()
            for detail in product.css('tr._1s_Smc'):
                left = detail.css('td._1hKmbr::text').get()
                right = detail.css('li._21lJbe::text').get()
                config[left]= right
            yield{
                'ProductId': id,
                'title': title,
                'detail': config
            }  

    

        