# letter-display-database

This project is a Python-based system for fetching, processing, and storing newsletter emails. It retrieves emails, processes the HTML content of the emails, and stores the processed data in a Supabase database.

**Note:** The front-end is in `letter-display` repository. 
**Note:** The project is finished but not the front-end.

## Files and their roles

- `main.py`: This is the main entry point of the application. It runs the `fetcher.py` and `extractor.py` scripts.

- `fetcher.py`: This script fetches new emails from a specified Gmail account. It filters the emails based on the subject and uploads the content of the emails to a Supabase database.

- `extractor.py`: This script downloads the latest email content from the Supabase database, extracts the necessary information from the email content, creates an `Article` object, and uploads the article data to the Supabase database.

- `supabase_client.py`: This script sets up the connection to the Supabase database using the URL and API key from the environment variables.

- `.env`: This file contains environment variables such as the Supabase URL and API key, IMAP server details, email user and password, and non-newsletter keywords.

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

## Note

The `Article` class is used to structure the data for each article. It has attributes for the title, image, date, content, snippet, and read time of an article. This class is defined in a separate file and imported into `extractor.py`.
