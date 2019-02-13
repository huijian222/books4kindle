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
        ('36kr', 'http://www.36kr.com/feed?1.0'),
        (u'TechCrunch 中国', 'http://techcrunch.cn/feed/'),
        (u'爱范儿', 'http://www.ifanr.com/feed'),
        ('Top News - MIT Technology Review', 'http://www.technologyreview.com/topnews.rss'),
        ('Hacker News', 'https://news.ycombinator.com/rss'),
        (u'麻省理工科技评论', 'http://zhihurss.miantiao.me/section/id/14'),
        (u'大公司日报', 'http://zhihurss.miantiao.me/daily/id/5'),
        (u'极客公园', 'http://www.geekpark.net/rss'),
        (u'人人都是产品经理', 'http://iamsujie.com/feed/'),
        (u'豆瓣一刻', 'http://yikerss.miantiao.me/rss'),
        (u'科普公园', 'http://www.scipark.net/feed/'),
        (u'科学松鼠会', 'http://songshuhui.net/feed'),
        (u'泛科学', 'http://pansci.tw/feed'),
        (u'果壳网', 'http://www.guokr.com/rss/'),
        (u'简书推荐', 'http://jianshu.milkythinking.com/feeds/recommendations/notes'),
        ('Quora', 'http://www.quora.com/rss', True),
        ('The Economist: China', 'http://www.economist.com/feeds/print-sections/77729/china.xml'),
        ('The Economist: Science and technology',
         'http://www.economist.com/feeds/print-sections/80/science-and-technology.xml'),
        (u'知乎日报', 'http://zhihurss.miantiao.me/dailyrss'),
        (u'深夜食堂', 'http://zhihurss.miantiao.me/section/id/1'),
        ('Matrix67', 'http://www.matrix67.com/blog/feed'),
    ]
