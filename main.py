import os
import random
import sys
import requests
from atproto import Client
from tags import tagsList

def post_to_x(text):
    """Sends a POST request to the X API wrapper. Returns True on success."""
    url = 'https://api.getxapi.com/twitter/tweet/create'
    
    headers = {
        'Authorization': f'Bearer {os.environ["Authorization"]}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "auth_token": os.environ["auth_token"],
        "text": text
    }

    try:
        # No retries: every call to the wrapper is billed
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        # Check if the request was successful
        if response.status_code == 200:
            print(f"Successfully posted to X: {text}")
            return True
        print(f"X API Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Request to X failed: {type(e).__name__}: {e}")
    return False

def post_to_bluesky(text):
    """Handles Bluesky login and posting. Returns True on success."""
    try:
        client_bsky = Client()
        client_bsky.login(os.environ["BSKY_HANDLE"], os.environ["BSKY_PASSWORD"])
        client_bsky.send_post(text=text)
        print(f"Successfully posted to Bluesky: {text}")
        return True
    except Exception as e:
        print(f"Bluesky Error: {type(e).__name__}: {e}")
        return False

if __name__ == "__main__":
    # Select a random entry from your tagsList
    random_entry = random.choice(tagsList)
    print(f"Selected tag: {random_entry}")

    if os.environ.get("DRY_RUN") == "1":
        print("DRY_RUN=1: skipping Bluesky and X posts")
        sys.exit(0)

    # Execute posts independently so one failing doesn't skip the other
    bluesky_ok = post_to_bluesky(random_entry)
    x_ok = post_to_x(random_entry)

    if not (bluesky_ok and x_ok):
        sys.exit(1)
