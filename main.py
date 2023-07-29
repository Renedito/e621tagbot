from tags import tagsList
import random
import tweepy
import os

try:
    client = tweepy.Client(
        consumer_key = os.environ["API_key"],
        consumer_secret = os.environ["API_key_secret"],
        bearer_token = os.environ["Bearer_token"],
        access_token = os.environ["Access_Token"],
        access_token_secret = os.environ["Access_Token_Secret"]        
) 
except KeyError:
    print("Keys not available!")

if __name__ == "__main__":
    random_entry = random.choice(tagsList)
    print(random_entry)
    client.create_tweet(text = random_entry)