#source:https://blog.datahut.co/scraping-amazon-reviews-python-scrapy/
import scrapy

# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
 
    # Spider name
    name = 'amazon_reviews'
 
    # Domain names to scrape
    allowed_domains = ['amazon.in']
 
    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.in/JBL-T205BT-Wireless-Earbud-Headphones/product-reviews/B07B9G75Z9/ref=cm_cr_arp_d_paging_btm_next_2?pageNumber="
    start_urls=[]
 
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,500):
        start_urls.append(myBaseUrl+str(i))
    #print (start_urls)
 
    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
 
            # Collecting product star ratings
            star_rating = data.css('.review-rating')
 
            # Collecting user reviews
            comments = data.css('.review-text')
        
            #Collecting review date
            review_date = data.css('.review-date')
            
            count = 0
      
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract()),
                      'date': ''.join(review_date[count].xpath(".//text()").extract())
                     }
                count=count+1
                
