
import scrapy
import pandas as pd
from collections import defaultdict
base_url = 'https://www.flipkart.com'
def read_csv():
    df = pd.read_csv('Products.csv')
    return df['url'].values.tolist()

class feedbacksmallSpider(scrapy.Spider):
    name = 'feedbacksmall'
    def start_requests(self):
        for url in read_csv():
            yield scrapy.Request(url)


    def parse(self, response):
        url_csv = response.url
        id = ''
        lent = 0
        df = pd.read_csv('Products.csv')
        for i in range(df['url'].shape[0]):
            if url_csv == df['url'][i]:
                id = df['_id/$oid'][i]
                lent = df['review'][i]
                break
        

        if len(lent) > 3:
           lent = lent.replace(',','')
        if int(lent) < 4:
            for pro in response.css('div._2wzgFH'):
                rate = pro.css('div._3LWZlK._1BLPMq::text').get()
                cmt = pro.css('div.t-ZTKy div::text').get()
                username = pro.css('div._3n8db9 p span::text')[1].get().replace(', ', '')
                if username is None: username = '' 
                if cmt is None : cmt = ''
                if rate is None : rate = 0
                
                yield{
                    'productid': id,
                    'rate': rate,
                    'cmt': cmt,
                    'username': username,
                }



   
       
          

    

        