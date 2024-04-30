from utils.fetcher import fetch
from utils.processor import extract
from subprocess import call
import json

def main():
    email_content = fetch()
    if email_content is None:
        print("No new email found.")
        return

    article = extract(email_content)

    data = {
        "title": article.title,
        "image": article.image,
        "date": article.date,
        "content": article.content,
        "snippet": article.snippet
    }

    data_json = json.dumps(data)

    call(["./supabase.sh", "insert_row", data_json])

if __name__ == "__main__":
    main()
