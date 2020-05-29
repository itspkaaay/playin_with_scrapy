import scrapy


# Creating a spider class
class quoteSpider(scrapy.Spider):
    name = "quoteSpider"

    def start_requests(self):
        url_list = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/']

        # parse the url list to request html from the websites list
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_id = response.url.split('/')[-2]
        print(page_id)
        filename = 'quotes-%s.html' % page_id
        with open(filename, 'wb') as file:
            file.write(response.body)
        self.log('Saved file %s' % filename)