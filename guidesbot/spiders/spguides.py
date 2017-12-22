# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from guidesbot.items import SpringGuide


class SpguidesSpider(CrawlSpider):
    name = 'spguides'
    allowed_domains = ['spring.io']
    start_urls = ['https://spring.io/guides']

    rules = (
        Rule(LinkExtractor(allow=r'/guides/gs/'), callback='parse_guide', follow=True),
    )

    def parse_guide(self, response):
        name = response.xpath('//article[@class="content--container"]/h1[@class="title"]/text()').extract_first()
        description = response.xpath('//article[@class="content--container"]/div[@class="article-body"]/div[1]/p').extract_first()
        url = response.url
        clone_url = response.xpath('//*[@id="clone-url-https"]').xpath('@value').extract_first()
        repo_url = response.xpath('//*[@id="sidebar"]/div[1]/div/div[@class="go-to-repo--container"]/a').xpath(
            '@href').extract_first()
        zip_url = response.css(
            '#sidebar > div.right-pane-widget--container.desktop-only > div > a.github_download.btn.btn-black.uppercase').xpath(
            '@href').extract_first()
        return SpringGuide(name=name, description=description, url=url, clone_url=clone_url, repo_url=repo_url,
                           zip_url=zip_url)
