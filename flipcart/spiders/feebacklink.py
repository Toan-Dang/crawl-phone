
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
        lent = 0
        df = pd.read_csv('Products.csv')
        for i in range(df['url'].shape[0]):
            if url_csv == df['url'][i]:
                id = df['_id/$oid'][i]
                lent = df['review'][i]
                break
        

        if len(lent) > 3:
           lent = lent.replace(',','')
        if int(lent) > 3:
            try:
                url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div:nth-child(4) > div > a').attrib['href']
            except:
                try:
                    url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div:nth-child(5) > div > a').attrib['href']
                except:
                    try:
                       url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div:nth-child(6) > div > a').attrib['href']
                    except:
                        try:
                            url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div:nth-child(7) > div > a').attrib['href']
                        except:
                            try:
                                url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div:nth-child(8) > div > a').attrib['href']
                            except:
                                try:
                                    url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div > div > div:nth-child(3) > div > a').attrib['href']
                                except:
                                    try: 
                                        url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div > div > div:nth-child(4) > div > a').attrib['href']
                                    except:
                                        try:
                                            url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div > div > div:nth-child(5) > div > a').attrib['href']
                                        except:
                                            try:
                                                url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div > div > div:nth-child(6) > div > a').attrib['href']
                                            except:
                                                try:
                                                    url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div > div > div:nth-child(7) > div > a').attrib['href']
                                                except:
                                                    url = response.css('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div > div > div:nth-child(8) > div > a').attrib['href']


            yield {
                'productid': id,
                'url' : base_url + url
            }
        # else:
        #     for pro in response.css('div._2wzgFH'):
        #         rate = pro.css('div._3LWZlK._1BLPMq::text').get()
        #         cmt = pro.css('div.t-ZTKy div::text').get()
        #         username = pro.css('div._3n8db9 p span::text')[1].get()
        #         if username is None: username = '' 
        #         if cmt is None : cmt = ''
        #         if rate is None : rate = 0
                
        #         yield{
        #             'productid': id,
        #             'rate': rate,
        #             'cmt': cmt,
        #             'username': username,
        #             'url': ''
        #         }



   
       
          

    

        