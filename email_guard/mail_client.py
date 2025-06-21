import imaplib
import email
from bs4 import BeautifulSoup


def fetch_emails(username, password, imap_server="imap.gmail.com"):
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)
    mail.select("inbox")

    _, data = mail.search(None, "ALL")
    email_ids = data[0].split()

    messages = []

    for eid in email_ids[-10:]:
        _, msg_data = mail.fetch(eid, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if "plain" in content_type:
                    body = part.get_payload(decode=True).decode(errors="ignore")
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")
        clean_body = BeautifulSoup(body, "html.parser").text
        messages.append({
            "from": msg["From"],
            "subject": msg["Subject"],
            "body": clean_body
        })
    return messages
