from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


def get_soup(url,userAgent=False):
    if userAgent:
        headers={'User-Agent':'Snorks'}
        response = requests.get(url,headers=headers)
        return BeautifulSoup(response.text)

    else:
        response  = requests.get(url)
        return BeautifulSoup(response.text)




def codeup_article(soup):
    article = soup.find(class_='mk-blog-single').text
    title = soup.title.text
    return {'title': title, 'content':article}

def codeup_article_list():
    urls = [
        'https://codeup.com/codeups-data-science-career-accelerator-is-here/',
        'https://codeup.com/data-science-myths/',
        'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
        'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
        'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/'
    ]
    soups = [get_soup(url,True) for url in urls]
    return [codeup_article(soup) for soup in soups]

def get_categories(soup):
    return soup.find(class_='category-list').text.lower().split()[2:]

def get_news_cards(soup):
    return soup.find_all(class_='news-card')

def news_article(news_card,category):
    title = news_card.find(itemprop='headline').text
    body = news_card.find(itemprop='articleBody').text
    return {
        'title':title,
        'content':body,
        'category':category
    }


def inshorts_articles():

    articles = {}
    url = 'https://inshorts.com/en/read/'
    categories = get_categories(get_soup(url))
    for category in categories:
        cards=get_news_cards(get_soup(url+category))
        articles[category]=[news_article(card,category) for card in cards]

    return articles


def save_articles():
    inshorts = inshorts_articles()
    articles =[]
    for key in inshorts:
        for article in inshorts[key]:
            articles.append(article)

    pd.DataFrame(articles).to_csv('inshorts.csv')
    pd.DataFrame(codeup_article_list()).to_csv('codeupblog.csv')


def acquire_articles(reload=False):

    if reload or not (os.path.exists('inshorts.csv') and os.path.exists('codeupblog.csv')):
        save_articles()
    return [pd.read_csv('inshorts.csv').drop(columns = 'Unnamed: 0'), pd.read_csv('codeupblog.csv').drop(columns = 'Unnamed: 0')]
