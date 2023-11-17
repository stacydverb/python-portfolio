# This Twitter bot uses tweepy and the twitter API to post random movie quotes every half hour. 

import tweepy
import random
import schedule
import time
from datetime import datetime

api_key = "API KEY HERE"
api_secret = "API SECRET KEY HERE"
bearer_token = r"BEARER TOKEN HERE"
access_token = "ACCESS TOKEN HERE"
access_token_secret = "SECRET ACCESS TOKEN HERE"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

with open("quotes.txt", 'r') as file:
    quotes = file.readlines()

def tweet_now():
    quote = random.choice(quotes)
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M")
    print(f"{quote} {current_time}")
    client.create_tweet(text=quote)

tweet_now()

def tweet_quote():
    quote = random.choice(quotes)
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M")
    print(f"{quote} {current_time}")
    try:
        client.create_tweet(text=quote)
    except tweepy.Forbidden:
        print("Choosing different quote...")
        different_quote = random.choice(quotes)
        print(f"{different_quote} {current_time}")
        client.create_tweet(text=different_quote)


schedule.every(30).minutes.do(tweet_quote)

while True:
    schedule.run_pending()
    time.sleep(1)