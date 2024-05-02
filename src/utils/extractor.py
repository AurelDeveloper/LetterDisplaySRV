from bs4 import BeautifulSoup
import datetime
from Article import Article
from supabase_client import supabase

def download():
    data = supabase.table("emails").select("content").order("emails_id", desc=True).limit(1).execute()
    email_content = data.data[0]['content'] if data.data else None
    return email_content

def calculate_readtime(email_content):
    words = email_content.split()
    num_words = len(words)
    readtime = num_words / 250
    return round(readtime)

def extract(email_content):
    soup = BeautifulSoup(email_content, 'html.parser')

    title = soup.find('h1').text if soup.find('h1') else "No title found"
    image = soup.find('img')['src'] if soup.find('img') else "No image found"
    date = datetime.datetime.now().isoformat()
    content = str(soup)
    snippet = soup.find('p').text[:40] if soup.find('p') else "No snippet found"
    readtime = calculate_readtime(content)

    article = Article(title, image, date, content, snippet, readtime)

    return article

def upload(article):
    supabase.table("posts").insert({
        "title": article.title,
        "img": article.image,
        "date": article.date,
        "content": article.content,
        "snippet": article.snippet,
        "readtime": article.readtime
    }).execute()

if __name__ == "__main__":
    email_content = download()
    if email_content:
        article = extract(email_content)
        if article:
            upload(article)