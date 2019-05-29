# schoolTweetsAnalysis

# Description

a website that analyses your 🏫's tweets

🚀Uses Twitter's API to collect your school's most recent tweets
and create a word cloud from it and execute sentiment analysis using ML

# 👨‍🎓 Example

Made with the 'oundleschool' twitter account

![alt text](oundleschoolimage.png "word cloud from oundleschool")

# Setup

1: clone the repository
2: navigate to the repository in the terminal
```
cd your/path/here
```
2: install all the requirements:

```
pip install -r requirements.txt
```

or

```
pip install tweepy
pip install wordcloud
pip install requests
pip install matplotlib
pip install numpy
```

3: select the twitter account you want to analyse
change the string parameter of the user_tweet() function
in line 58 of the tweet_collector.py file.

4: run tweet_collector.py and save the file that is produced
```
python path/to/repo/source/tweet_collector.py
```
