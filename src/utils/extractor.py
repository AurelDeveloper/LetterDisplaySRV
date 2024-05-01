import json
from bs4 import BeautifulSoup
import datetime
from fetcher import fetch
from Article import Article

def calculate_readtime(content):
    words = content.split()
    num_words = len(words)
    readtime = num_words / 250
    return round(readtime)

def extract(email_content):
    soup = BeautifulSoup(email_content, 'html.parser')

    title = soup.find('h1').text if soup.find('h1') else None
    image = soup.find('img')['src'] if soup.find('img') else None
    date = datetime.datetime.now().isoformat()
    content = str(soup)
    snippet = soup.find('p').text[:40] if soup.find('p') else None
    readtime = calculate_readtime(content)

    article = Article(title, image, date, content, snippet, readtime)

    with open('../articles.json', 'w') as json_file:
        json.dump(article.__dict__, json_file)

if __name__ == "__main__":
    email_content = fetch()
    if email_content:
        extract(email_content)