import imaplib
import email
import re
import os

NEWSLETTER_KEYWORDS = ['newsletter', 'update', 'weekly', 'monthly']
NON_NEWSLETTER_KEYWORDS = ['werbung', 'danke', 'preis erhöhung']

def filter(email_content):
    return any(re.search(keyword, email_content, re.IGNORECASE) for keyword in NEWSLETTER_KEYWORDS) and \
        not any(re.search(keyword, email_content, re.IGNORECASE) for keyword in NON_NEWSLETTER_KEYWORDS)

def fetch():
    mail = imaplib.IMAP4_SSL(os.environ['IMAP_SERVER'])
    mail.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASS'])
    mail.select("inbox")

    result, data = mail.uid('search', None, f'(FROM \'{os.environ["EMAIL_FROM"]}\')', 'UNSEEN')
    if not data[0]:
        return None

    latest_email_uid = data[0].split()[-1]
    result, email_data = mail.uid('fetch', latest_email_uid, '(BODY.PEEK[TEXT])')
    if not email_data[0][1]:
        return None

    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    email_content = email_message.get_payload()

    return email_content if filter(email_content) else None

if __name__ == "__main__":
    email_content = fetch()
    if email_content:
        print(email_content)
