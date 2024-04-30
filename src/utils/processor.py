import json
from bs4 import BeautifulSoup
import datetime
from models.article import Article
from fetcher import fetch

def extract(email_content):
    soup = BeautifulSoup(email_content, 'html.parser')

    title = soup.find('h1').text if soup.find('h1') else None
    image = soup.find('img')['src'] if soup.find('img') else None
    date = datetime.datetime.now().isoformat()
    content = str(soup)
    snippet = soup.find('p').text[:40] if soup.find('p') else None

    article = Article(title, image, date, content, snippet)

    with open('../articles.json', 'w') as json_file:
        json.dump(article.__dict__, json_file)

if __name__ == "__main__":
    email_content = fetch()
    if email_content:
        extract(email_content)
