
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
        
  
        for pro in response.css('div.col._2wzgFH.K0kLPL'):
           rate = pro.css('div._3LWZlK._1BLPMq::text').get()
           cmt = pro.css('#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div::text').get()
           username = pro.css('p._2mcZGG span::text')[1].get().replace(', ','')
           if username is None:
               username = 'anonymous'
           yield{
               'productid': id,
                'rate': rate,
                'cmt': cmt,
                'username': username,
           }
        try:
            next_page = response.css('a._1LKTO3')[1].attrib['href']
            print('************************try*******************')
        except:
            next_page = response.css('a._1LKTO3').attrib['href']
            print('************************catch*******************')

        print('-----------------------------------------------------------------')
        print(next_page)
        print('-----------------------------------------------------------------')

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)  
            
       
          

    

        