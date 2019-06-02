from flask import Flask, request, render_template
try:
    import tweepy
except ImportError:
    print("ENSURE YOU HAVE INSTALLED tweepy")
try:
    from credentials import *
except ImportError:
    print("ENSURE YOU HAVE CREATED credentials.py IN THE SAME FOLDER")
try:
    from wordcloud import WordCloud, STOPWORDS
except ImportError:
    print("ENSURE YOU HAVE INSTALLED wordcloud")
try:
    import requests
except ImportError:
    print("ENSURE YOU HAVE INSTALLED requests")
try:
    import numpy as np
except ImportError:
    print("ENSURE YOU HAVE INSTALLED numpy")
from PIL import Image
import urllib

meaningless_words = [
                    "il","la","az","ez","un","una",
                    "uno","gli","le","the","with","RT",
                    "amp","what","who","which","that",
                    "che","chi","con","I","del","di","della",
                    "ma","da","will"
                    ]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
tweet_lst = []

def user_tweet(twitter_handle,tweet_count):
    try:
        tweets = api.user_timeline(screen_name=twitter_handle, count=200, tweet_mode="extended")
        clean = []
        for tweet in tweets:
            for word in tweet.full_text.split():
                if 'https:' in word or 'http:' in word or 'www' in word or '.com' in word:
                    continue
                elif word[0] == "@":
                    continue
                else:
                    word_cloud_lst.append(word)
                    clean.append(word)
            clean = []
    except tweepy.TweepError:
        word_cloud_lst.append("invalid username")#a cool error message

def generate_wordcloud(words, mask,handle):
    stopwords = set(STOPWORDS)
    for word in meaningless_words:
        stopwords.add(word)
    word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=stopwords, mask=mask).generate(words)
    path = 'static/images/'+handle+'.png'
    word_cloud.to_file(path)
    word_cloud_lst = []

def getMask(mask_link):
    default = "http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png"
    try:
        response = requests.get(mask_link,stream = True)
    except Exception:
        response = requests.get(default,stream = True)
        mask = np.array(Image.open(response.raw))
        return mask
    if response.status_code == 200:
        mask = np.array(Image.open(response.raw))
    else: #elif response.status_code == 404:
        response = requests.get(default,stream = True)
        mask = np.array(Image.open(response.raw))
    return mask

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    global word_cloud_lst
    word_cloud_lst = []
    handle = request.form['account']
    if handle == "" or handle == " ":
        return "invalid input"
    else:
        tweet_count = request.form['tweet_count']
        try:
            tweet_count = int(tweet_count)
            if tweet_count <= 0:
                return "number of tweets to be analysed must be bigger than zero"
            elif tweet_count > 200:
                return "this script can not handle more than 200 tweets to be analysed"
        except ValueError:
            return "invalid number entered"
        mask_link = request.form['template']
        if mask_link == " " or mask_link == "":
            mask_link = "http://"
        mask = getMask(mask_link)
        user_tweet(handle,tweet_count)
        words = " ".join(word_cloud_lst)
        generate_wordcloud(words, mask,handle)
        filename = "images/{}.png".format(handle)
        return render_template('body.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
