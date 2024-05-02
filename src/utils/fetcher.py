import imaplib
import email
import re
import os
from dotenv import load_dotenv
from supabase_client import supabase

load_dotenv('.env.local')

NON_NEWSLETTER_KEYWORDS = os.getenv('NON_NEWSLETTER_KEYWORDS').split(',')

def filter(subject, email_id):
    email_id_str = email_id.decode("utf-8")
    data = supabase.table("emails").select("content").order("emails_id", desc=True).limit(1).execute()
    if len(data.data) > 0:
        return False
    return not any(re.search(keyword, subject, re.IGNORECASE) for keyword in NON_NEWSLETTER_KEYWORDS)

def fetch():
    mail = imaplib.IMAP4_SSL(os.environ['IMAP_SERVER'])
    mail.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASS'])
    mail.select("inbox")

    result, data = mail.uid('search', None, f'(FROM \'{os.environ["EMAIL_FROM"]}\')', 'UNSEEN')
    if not data[0]:
        return None

    latest_email_uid = data[0].split()[-1]
    result, email_data = mail.uid('fetch', latest_email_uid, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    if not email_data[0][1]:
        return None

    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    subject = email_message['Subject']

    if not filter(subject, latest_email_uid):
        return None

    result, email_data = mail.uid('fetch', latest_email_uid, '(BODY.PEEK[TEXT])')
    if not email_data[0][1]:
        return None

    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    email_content = email_message.get_payload()

    latest_email_uid_str = latest_email_uid.decode("utf-8")
    upload(latest_email_uid_str, email_content)

def upload(email_id, email_content):
    supabase.table("emails").insert({"emails_id": email_id, "content": email_content}).execute()

if __name__ == "__main__":
    fetch()