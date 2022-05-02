from gc import callbacks
import scrapy

class phoneSpider(scrapy.Spider):
    name = 'phone'
    start_urls = ['https://www.flipkart.com/search?q=mobile+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_12_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+phone%7CMobiles&requestId=bfedeada-5cc1-41f0-a300-80eb0016bae0&as-searchtext=mobile%20phone']
    base_url = 'https://www.flipkart.com'
    def parse(self, response):
        for product in response.css('a._1fQZEK'):

            try: 
                MSRP = product.css('div._3I9_wc._27UcVY::text')[1].get(),
            except: 
                MSRP  = 0

            try: 
                rate = product.css('div._3LWZlK::text').get(),
            except: 
                rate  = 0

            try: 
                rating = product.css('span._2_R_DZ span::text').get().replace('\u00a0', ''),
            except: 
                rating  = 0

            try: 
                review = product.css('span._2_R_DZ span::text')[2].get().replace('\u00a0', ''),
            except: 
                review  = 0

            yield{
                'name' : product.css('div._4rR01T::text').get(),
                'price' : product.css('div._30jeq3::text').get().replace('₹',''),
                'img' :  product.css('img._396cs4').attrib['src'], 
                'MSRP': MSRP, 
                'rate' : rate, 
                'rating' : rating, 
                'review' : review,
                'url' : self.base_url +  product.attrib['href']
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

