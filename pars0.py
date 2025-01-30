import scrapy


class LightingSpider(scrapy.Spider):
    name = 'lighting'
    allowed_domains = ['https://divan.ru']
    start_urls = ['https://www.divan.ru/category/svet']
    def parse(self, response):
        # Измените селекторы на актуальные для сайта divan.ru
        electriclamps = response.css('div._Udok')

        for electriclamp   in electriclamps :

            yield {
                'name': electriclamp.css('div.DqOqS span::text') ,
                'price': electriclamp.css('div.ui-LD-ZU span::text'),
                'link': electriclamp.css('a').attrib('href')
            }
