# LetterDisplay

This project is a Python-based newsletter emails fetching, processing, and storage system. It fetches emails from a Gmail account, processes the HTML content of the emails, and stores the processed data in a JSON file. The data is then uploaded to a Supabase database.

## Explication

It's a backend script for a website template that automatically displays the newsletter articles on a Next.js frontend website. (The frontend is not included in this repository and is not yet developed)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- A Gmail account for fetching emails
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

## Running the Scripts

1. Run the `main.sh` script to fetch, process, and store email data:

```bash
./main.sh
```

2. Run the `test.py` script to send a test newsletter:

```python
python3 test.py
```

## Built With

- Python
- BeautifulSoup
- imaplib
- smtplib
- Supabase
