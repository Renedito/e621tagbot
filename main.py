import os
import random
import requests
from atproto import Client
from tags import tagsList

def post_to_x(text):
    """Sends a POST request to the X API wrapper."""
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
        response = requests.post(url, json=payload, headers=headers)
        # Check if the request was successful
        if response.status_code == 200:
            print(f"Successfully posted to X: {text}")
        else:
            print(f"X API Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Request to X failed: {e}")

def post_to_bluesky(text):
    """Handles Bluesky login and posting."""
    try:
        client_bsky = Client()
        client_bsky.login(os.environ["BSKY_HANDLE"], os.environ["BSKY_PASSWORD"])
        client_bsky.send_post(text=text)
        print(f"Successfully posted to Bluesky: {text}")
    except Exception as e:
        print(f"Bluesky Error: {e}")

if __name__ == "__main__":
    # Select a random entry from your tagsList
    random_entry = random.choice(tagsList)
    print(f"Selected tag: {random_entry}")

    # Execute posts
    post_to_bluesky(random_entry)
    post_to_x(random_entry)