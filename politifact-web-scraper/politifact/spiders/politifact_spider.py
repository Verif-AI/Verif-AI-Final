from politifact.items import PolitifactItem

import scrapy

class PolitifactSpider(scrapy.Spider):

    name = "politifact"
    allowed_domains = ["politifact.com"]
    start_urls = [
        "https://www.politifact.com/factchecks/list/",
    ]

    CURR_PAGES = 0
    MAX_PAGES = 3

    def __init__(self, MAX_PAGES=3, **kwargs):
        self.MAX_PAGES = int(MAX_PAGES)
        super().__init__(**kwargs)

    def parse_article(self, response):
        '''
        Obtains information about the article i.e. https://www.politifact.com/factchecks/2024/feb/20/instagram-posts/biden-didnt-announce-housing-for-labor-program-for/
        '''
        politifact_item = PolitifactItem()

        # Retrieve article fields through css selector
        review_tags = response.css('a.c-tag span::text').getall()
        review_points = response.css('div.short-on-time ul li p::text').getall()
        review_article = response.css('article.m-textblock *::text').getall()
        stripped_review_article = ''.join(list(filter(lambda x: x != "\n", review_article)))

        # Homepage fields
        politifact_item['claim'] = response.meta['claim']
        politifact_item['claim_source'] = response.meta['claim_source']
        politifact_item['review_date'] = response.meta['review_date']
        politifact_item['review_author'] = response.meta['review_author']
        politifact_item['veracity'] = response.meta['veracity']

        # Article fields
        politifact_item['review_tags'] = review_tags
        politifact_item['review_points'] = review_points
        politifact_item['review_article'] = stripped_review_article
        politifact_item['review_url'] = response.url

        yield politifact_item

    def parse_homepage_item(self, item):
        '''
        Obtains information about the fact list https://www.politifact.com/factchecks/list/
        '''
        # author and date are both in footer (ex. "By Sofia Ahmed • February 28, 2024")
        footer = item.css("footer.m-statement__footer::text").get().strip()
        author_date_list = footer.split('•')

        # Information obtainable through fact check list
        claim = item.css("div.m-statement__quote a::text").get().strip()
        claim_source = item.css("a.m-statement__name::attr(title)").get()
        review_date = ' '.join(author_date_list[1].strip().split(' '))
        review_author = ' '.join(author_date_list[0].strip().split(' ')[1:])
        veracity = item.css("img.c-image__original::attr(alt)").get()

        return {
            "claim": claim,
            "claim_source": claim_source,
            "review_date": review_date,
            "review_author": review_author,
            "veracity": veracity
        }

    def parse(self, response):

        # Get the all items matching the css
        fact_check_items = response.css("li.o-listicle__item")

        for item in fact_check_items:

            homepage_item = self.parse_homepage_item(item)

            # Obtain article link
            article_link = item.css(
                "div.m-statement__quote a::attr(href)").get()
            article_link_absolute = response.urljoin(article_link)

            yield response.follow(
                url=article_link_absolute,
                callback=self.parse_article,
                meta=homepage_item
            )

            # yield homepage_item

        # Go to next page link
        next_page = response.css(
            "a.c-button.c-button--hollow:contains('Next')::attr(href)").get()
        self.CURR_PAGES += 1

        # Stop when there are no more next pages or reached MAX_PAGES
        if next_page is not None and self.CURR_PAGES < self.MAX_PAGES:
            next_page_absolute = response.urljoin(next_page)
            yield response.follow(
                url=next_page_absolute,
                callback=self.parse
            )
