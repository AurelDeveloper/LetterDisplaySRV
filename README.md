# letter-display-database

This project is a Python-based newsletter emails fetching, processing, and storage system. It fetches emails from a Gmail account, processes the HTML content of the emails, and stores the processed data in a JSON file. The data is then uploaded to a Supabase database.

**Note**: The frontend is in `letter-display` repository.

## Explication

It's a backend script for a website template that automatically displays the newsletter articles on a Next.js frontend website. (The frontend is not included in this repository and is not yet developed)

1. Run the `src/main.py`.
2. The `src/main.py` will execute `src/utils/fetcher.py`, which checks if there is a new email from the newsletter sender. If yes, it checks the subject for a filter word; if no, it fetches the email content.
3. The `src/main.py` will execute `src/utils/extractor.py`, which extracts the main title, main image, a snippet from the article text, and calculates the reading time.
4. The `src/main.py` will execute `src/utils/uploader.py`, which uploads all the data to the Supabase table.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- A Supabase account for storing processed data

### Installing

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Configuration

1. Rename the `modules` directory to your preferred name.
2. Update the `.env.local` file with your Supabase URL and API key.
3. Update the `fetcher.py` file with the Gmail account credentials from which you want to fetch emails.
4. Update the `test.py` file with the Gmail account credentials for sending test newsletters.

## Built With

- Python
- BeautifulSoup
- imaplib
- smtplib
- Supabase

