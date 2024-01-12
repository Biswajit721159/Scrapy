import pdb
import scrapy


class AmbissionboxSpider(scrapy.Spider):
    name = "ambissionbox"
    allowed_domains = ["www.ambitionbox.com"]
    start_urls = ["https://www.ambitionbox.com/overview/riktam-technologies-overview"]

    def parse(self, response):
        # company_name=response.xpath('//h1[@class="newHInfo__cNtxt"]/text()').get()
        # url = "https://www.ambitionbox.com/overview/riktam-technologies-overview"
        
        # last_segment = url.split("/")[-1]
        # desired_string = last_segment.split("-")[-1]
        # print(desired_string)
        alldata=response.xpath('//ul[@class="nav-tabs__content"]/li[@class="slider-item"]')
        # pdb.set_trace()


        
        for i in range(1, len(alldata)):
            data=alldata[i]
            url=data.xpath('./a/@href').get()
            last_segment = url.split("/")[-1]
            desired_string = last_segment.split("-")[-1]
            original="https://www.ambitionbox.com"+url
            if(desired_string=="reviews"):
                yield scrapy.Request(original, callback=self.findReviews)
            elif(desired_string=="salaries"):   
                yield scrapy.Request(original,callback=self.salaries) 
        pass

    def overview(self,response):
        pass
    
    def salaries(self,response):
        allsalaries=response.xpath('//tr[@class="jobProfiles-table__row"]')
        for salarie in allsalaries:
            item=salarie.xpath('td[@class="left-content"]/div[@class="card-content"]')
            insiderole=item.xpath('div[@class="content-wrapper"]')
            role=item.xpath('a/p[@class="card-content__company"]/text()').get()
            experience=insiderole.xpath('span/text()').get()
            noOfsalaries=insiderole.xpath('span[@class="datapoints"]/text()').get()

            rightside=salarie.xpath('td[@class="right-content"]/div[@class="right-content__text"]/div[@class="avg-salary"]')
            avgsalary=rightside.xpath('div/text()').get()
            yearOrmonth=rightside.xpath('div/span[@class="colored"]/text()').get()
            howMuchSalary=rightside.xpath('p[@class="salary-range"]/text()').get()
            print(avgsalary,yearOrmonth,howMuchSalary)
            
            print("*****************************")
            pdb.set_trace()
            # print(role)
        pass

    def findReviews(self,response):
        reviewBody=response.xpath('//div[@class="review-body"]')
        for data in reviewBody:
            review=data.xpath('div[@class="content"]/p[@class="body-medium overflow-wrap"]/text()').getall()
            # print("*********")
            # print(review)
        pass
        


