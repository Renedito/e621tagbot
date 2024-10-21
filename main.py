from tags import tagsList
from atproto import Client
import random
import tweepy
import os

try:
    clientTwitter = tweepy.Client(
        consumer_key = os.environ["API_key"],
        consumer_secret = os.environ["API_key_secret"],
        bearer_token = os.environ["Bearer_token"],
        access_token = os.environ["Access_Token"],
        access_token_secret = os.environ["Access_Token_Secret"]
    clientBsky = Client()
    clientBsky.login(os.environ["BSKY_HANDLE"], os.environ["BSKY_PASSWORD"])        
) 
except KeyError:
    print("Keys not available!") # DEBUG line to test if Actions can access the environment keys on Github

if __name__ == "__main__":
    random_entry = random.choice(tagsList)          # Select a random tag from tags list
    print(random_entry)                             # DEBUG: Makes Actions print the tag on the log 
    clientTwitter.create_tweet(text = random_entry) # Posts the tag on Twitter
    clientBsky.send_post(text = random_entry)       # Posts the tag on Bluesky