
import scrapy
import pandas as pd


def read_csv():
    df = pd.read_csv('feedbacklink.csv')
    return df['url'].values.tolist()

class feedbackSpider(scrapy.Spider):
    name = 'feedback'

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
        
  
        for pro in response.css('div.col.JOpGWq'):
            pass
       
          

    

        