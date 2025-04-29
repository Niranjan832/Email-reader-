from googleapiclient.discovery import build
from google.oauth2 import service_account

# Load Gmail API credentials
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
creds = service_account.Credentials.from_service_account_file( ""json file to be attached to access mail"json", scopes=SCOPES)

# Connect to Gmail API
service = build("gmail", "v1", credentials=creds)

def mark_all_as_read():
    user_id = "me"
    query = "is:unread"
    
    # Fetch unread messages
    results = service.users().messages().list(userId=user_id, q=query).execute()
    messages = results.get("messages", [])

    if not messages:
        print("No unread emails found.")
        return

    # Mark emails as read
    for msg in messages:
        service.users().messages().modify(
            userId=user_id, 
            id=msg["id"], 
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()

    print(f"Marked {len(messages)} emails as read.")

mark_all_as_read()
