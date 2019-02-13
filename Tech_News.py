#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return tech


class tech(BaseFeedBook):
    title = u'Tech News'
    __author__ = 'calibre'
    description = u'每日科技新闻精选，知乎问答精选，Quora精选，豆瓣，博客，经济学人China和Tech部分，各种科普，果壳天文，深夜食堂，数学精选。'
    language = 'zh-cn'
    feed_encoding = "utf-8"
    page_encoding = "utf-8"
    mastheadfile = "mh_default.gif"
    coverfile = "cv_default.jpg"
    network_timeout = 60
    oldest_article = 1
    max_articles_per_feed = 10
    feeds = [
        ('36kr', 'https://rsshub.app/36kr/search/article/8%E7%82%B91%E6%B0%AA'),
        (u'TechCrunch 中国', 'http://techcrunch.cn/feed/'),
        (u'the verge', 'https://rsshub.app/verge'),
        ('Top News - MIT Technology Review', 'http://www.technologyreview.com/topnews.rss'),
        ('Hacker News', 'https://news.ycombinator.com/rss'),
        (u'麻省理工科技评论', 'http://zhihurss.miantiao.me/section/id/14'),
        (u'大公司日报', 'http://zhihurss.miantiao.me/daily/id/5'),
        (u'环球科学', 'https://feedx.net/rss/huanqiukexue.xml'),
        (u'极客公园', 'http://www.geekpark.net/rss'),
        (u'人人都是产品经理', 'http://iamsujie.com/feed/'),
        (u'豆瓣一刻', 'http://yikerss.miantiao.me/rss'),
        (u'科普公园', 'http://www.scipark.net/feed/'),
        ('v2ex', 'https://rsshub.app/v2ex/topics/hot'),
        (u'科学松鼠会', 'http://songshuhui.net/feed'),
        (u'泛科学', 'http://pansci.tw/feed'),
        (u'果壳网', 'https://rsshub.app/guokr/scientific'),
        ('The Economist', 'https://feedx.net/rss/economist.xml'),
        (u'知乎日报', 'http://zhihurss.miantiao.me/dailyrss'),
        (u'深夜食堂', 'http://zhihurss.miantiao.me/section/id/1'),
        ('Matrix67', 'http://www.matrix67.com/blog/feed'),
        (u'IT橘子', 'https://rsshub.app/itjuzi/invest', True),
        (u'FT 中文网', 'https://rsshub.app/ft/chinese/hotstoryby7day'),
        ('ruanyifen', 'http://www.ruanyifeng.com/blog/atom.xml'),
    ]

