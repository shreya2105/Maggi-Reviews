#source:https://blog.datahut.co/scraping-amazon-reviews-python-scrapy/
import scrapy
# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
 
    # Spider name
    name = 'amazon_reviews'
 
    # Domain names to scrape
    allowed_domains = ['amazon.in']
 
    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.in/Maggi-2-Minute-Noodles-Masala-Pack/product-reviews/B07B4KQRZG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&amp;amp;pageNumber="
    start_urls=[]
 
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,176):
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
 
            # Combining the results
            #for review in star_rating:
            #    yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      
            #          'comment': ''.join(comments[count].xpath(".//text()").extract())}
                
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1
                
