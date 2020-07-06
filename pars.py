from lxml import html
import requests
from sqlescapy import sqlescape
from news import News
from connect import path_ffin

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}



class Parser:

    def parse(self):
        response = requests.get(path_ffin, headers=header)
        dom = html.fromstring(response.text)

        news = []
        items = dom.xpath("//div[@class='article']")

        for item in items:
            nv = {}
            title = item.xpath('.//a/text()')
            link = item.xpath('.//a/@href')
            article_date = item.xpath(".//div[@class='article_date']/text()")
            description = item.xpath(".//p/text()")
            external_id = item.xpath("./@id")

            news.append(News(
                sqlescape(title[0]),
                sqlescape(link[0]),
                sqlescape(article_date[0].replace('\n', '').replace('\t', '')),
                sqlescape(description[0]),
                sqlescape(external_id[0].split('_')[-1])
            ))

        return news



