try:
    import tweepy
except ImportError:
    print("ENSURE YOU HAVE INSTALLED tweepy")
try:
    from credentials import *
except ImportError:
    print("ENSURE YOU HAVE CREATED credentials.py IN THE SAME FOLDER")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def user_tweet(twitter_handle):
    statuses = api.user_timeline(screen_name=twitter_handle, count=2, tweet_mode="extended")
    return statuses.full_text.split()

print(user_tweet("oundleschool"))
