import requests
from bs4 import BeautifulSoup
import pprint

# url of HN page 1 and 2
url1 = 'https://news.ycombinator.com/news'
url2 = 'https://news.ycombinator.com/news?p=2'
def scrape(url):
    res = requests.get(url1)
    parse = BeautifulSoup(res.text, 'html.parser')
    links = parse.select('.titleline > a')
    subtexts = parse.select('.subtext')
    # you can set the points benchmark here
    set_points = 99

    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtexts[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > set_points:
                hn.append({'title': title, 'votes': points, 'link': href})
    return sorted_by_votes(hn)

def sorted_by_votes(news_links):
    return sorted(news_links, key=lambda k: k['votes'], reverse=True)
# both pages consolidated. you can add nth number of pages
page1 = scrape(url1)
page2 = scrape(url2)
scrapped_pages = page1 + page2

pprint.pprint(scrapped_pages)















