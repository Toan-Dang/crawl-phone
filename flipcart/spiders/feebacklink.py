
import scrapy
import pandas as pd
from collections import defaultdict
base_url = 'https://www.flipkart.com'
def read_csv():
    df = pd.read_csv('Products.csv')
    return df['url'].values.tolist()

class feedbacklinkSpider(scrapy.Spider):
    name = 'feedbacklink'


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
      
                
                
        if int(response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div:nth-child(5) > div > div.row._3AjFsn._2c2kV- > div._2e3Uck > div > div.col-4-12 > div > div:nth-child(3) > div > span::text').get().replace(' Reviews','')) > 3:

            fburl = base_url + response.xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[9]/div[7]/div/a/@href')[0].extract()
            yield {
                'productid': id,
                'rate': '',
                'cmt': '',
                'username': '',
                'url' : fburl
            }
        else:
            for pro in response.css('div._2wzgFH'):
                rate = pro.css('div._3LWZlK._1BLPMq::text').get()
                cmt = pro.css('div.t-ZTKy div::text').get()
                username = pro.css('div._3n8db9 p span::text')[1].get().replace(', ','')
                yield{
                    'productid': id,
                    'rate': rate,
                    'cmt': cmt,
                    'username': username,
                    'url': ''
                }



   
       
          

    

        