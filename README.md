# letter-display-database

This project is a Python-based system for fetching, processing, and storing newsletter emails. It retrieves emails, processes the HTML content of the emails, and stores the processed data in a Supabase database.

**Note:** The front-end is in `letter-display` repository. 

## Files and their roles

- `main.py`: This is the main entry point of the application. It runs the `fetcher.py` and `extractor.py` scripts.

- `fetcher.py`: This script fetches new emails from a specified Gmail account. It filters the emails based on the subject and uploads the content of the emails to a Supabase database.

- `extractor.py`: This script downloads the latest email content from the Supabase database, extracts the necessary information from the email content, creates an `Article` object with the extracted information and the most common tag from a list of tags defined in the `.env` file, and uploads the article data to the Supabase database. If no tag is found in the content, a default tag defined in the `.env` file is used.

- `supabase_client.py`: This script sets up the connection to the Supabase database using the URL and API key from the environment variables.

- `.env`: This file contains environment variables such as the Supabase URL and API key, IMAP server details, email user and password, non-newsletter keywords, a list of tags, and a default tag.

- `Article.py`: This file contains the class `Article`, the class is used to structure the data for each article. It has attributes for the `title`, `img`, `date`, `content`, `snippet`, `readtime`, `tag` of an article.

## Roadmap

- [ ] Improve the `extractor.py`.
- [ ] Implement a multi-newsletter fetcher and extractor.
- [ ] Split and organize the Supabase tables.

## How to run the project

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages using pip:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Update the `.env` file with your Supabase URL, API key, and email details.
5. Run the `main.py` script:

```bash
python src/main.py
```

## Built With

- Python
- BeautifulSoup
- imaplib
- Supabase
