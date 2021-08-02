from bs4 import BeautifulSoup
import requests
import lxml


# SCRAPPING MY JOYONLINE'S ENTERTAINMENT NEWS
# scrapping the top news
def top_story_news_head():
    # requesting from the site
    res = requests.get('https://www.myjoyonline.com/').text
    # using bs4 to read the res
    soup = BeautifulSoup(res, 'lxml')
    # grabbing top story  news
    top_story_news = soup.find('div', class_="top-story-label")
    top_story = top_story_news.h4.text
    the_news = soup.find('div', class_='title-summary position-absolute dark-gradient p-3')
    top_news = the_news.h1.text
    link = the_news.a.get('href')
    print(top_story + '\n')
    print(top_news)
    print(f'=> {link}')
    print('')


# The whole section of the news sector
def news_sector():
    # requesting from the site
    res = requests.get('https://www.myjoyonline.com/news/').text
    # using bs4 to read the res
    soup = BeautifulSoup(res, 'lxml')
    # grabbing news
    news = soup.find_all('div', class_='row pl-3 pr-3 vertical-position')
    print('News Sector\n')
    for items in news:
        item = items.h1
        links = items.a.get('href')
        print(item.text)
        print(f'For more information:\n=> {links}\n')
    print('')

    # Main news
    # getting National news
    # national_news = soup.find_all('div', class_='home-section-label my-3')
    news_under_all = soup.find_all('div', class_='home-section-story-list tt-center')
    for items in news_under_all:
        news = items.h4.text
        itm = items.a.get('href')
        print(news.strip())
        print(f'For more information: \n=> {itm}\n')


# scrapping most popular news

def popular_news():
    # requesting from the site
    res = requests.get('https://www.myjoyonline.com/news/').text
    # reading html through bs4
    soup = BeautifulSoup(res, 'lxml')
    pp = soup.find('div', class_='label-yellow mt-3')
    pop = pp.a.h4.text
    print(pop)
    print('')
    # getting the information
    info = soup.find_all('li', class_='faded-bar')
    pop_info = info
    for items in pop_info:
        item = items.a.text
        links = items.a.get('href')
        print(f'{item.strip()}\nFor more information:')
        print(f'=> {links}\n')


def latest_news():
    # requesting from the site
    res = requests.get('https://www.myjoyonline.com/news/').text
    # reading html through bs4
    soup = BeautifulSoup(res, 'lxml')
    pps = soup.find_all('ul', class_='home-latest-list')
    print('Latest News\n')
    for items in pps:
        itm = items.li.a.text
        item = items.li.a.get('href')
        time = items.span.text
        print(f"{itm}\nFor more information:")
        print(f'=> {item}\n')


top_story_news_head()
latest_news()
news_sector()
popular_news()
