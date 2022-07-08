from datetime import datetime, timedelta
import locale
import platform

from bs4 import BeautifulSoup

from webapp.news.parsers.utils import save_news, get_html



if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')


def parse_investing_date(date_str):
    if 'minutes' in date_str or 'hours' in date_str:
        value = date_str.split(' ')[0].replace('\xa0-\xa0', '')
        value = int(value)
        if 'minutes' in date_str:
            published_time = datetime.now() - timedelta(minutes=value)
        else:
            published_time = datetime.now() - timedelta(hours=value)
        return published_time
    else:
        try:
            return datetime.strptime(date_str, '%b %d, %Y')
        except ValueError:
            return datetime.now()

    
def get_investing_snippets():
    html = get_html('https://www.investing.com/news/most-popular-news')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('div', class_='largeTitle').findAll('div', class_='textDiv')
        for news in all_news:
            title = news.find('a', class_='title').text
            url = news.find('a', class_='title')['href']
            published = news.find('span', class_='date').text
            published = parse_investing_date(published)
            save_news(title, url, published)