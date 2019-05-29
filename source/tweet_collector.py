import tweepy
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

def user_tweet(twitter_handle):
    statuses = api.user_timeline(screen_name=twitter_handle, count=2, tweet_mode="extended")
    return statuses

print(user_tweet("oundleschool"))
