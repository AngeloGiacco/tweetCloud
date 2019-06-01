from flask import Flask, request, render_template
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
word_cloud_lst = []
tweet_lst = []

def user_tweet(twitter_handle):
    tweets = api.user_timeline(screen_name=twitter_handle, count=10, tweet_mode="extended")
    clean = []
    for tweet in tweets:
        for word in tweet.full_text.split():
            if 'https:' in word or 'http:' in word or 'www' in word or '.com' in word:
                continue
            else:
                word_cloud_lst.append(word)
                clean.append(word)
        tweet_lst.append(" ".join(clean))
        clean = []

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    global tweet_lst
    account = request.form['account']
    user_tweet(account)
    tweet_text = ("<br><br>").join(tweet_lst)
    tweet_lst = []
    return tweet_text

if __name__ == '__main__':
    app.run(debug=True)
