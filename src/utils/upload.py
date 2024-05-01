from fetcher import fetch
from supabase_client import supabase
from extractor import extract

def upload():
    email_content = fetch()
    if email_content is None:
        print("No new email found.")
        return

    article = extract(email_content)

    data = {
        "title": article.title,
        "content": article.content,
        "date": article.date,
        "snippet": article.snippet,
        "readtime": article.readtime,
        "img": article.image
    }

    response = supabase.table('posts').insert(data)

    if response.error:
        print(f"Failed to insert data: {response.error}")
    else:
        print("Data inserted successfully.")


if __name__ == "__main__":
    upload()


