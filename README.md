[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](https://www.firsttimersonly.com/)
[![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-blueviolet.svg)](https://opensource.com/article/18/11/reasons-love-open-source)
[![Python](https://img.shields.io/badge/language-python-success.svg)](https://www.python.org/)

# tweetAnalysis

## Description

a website that analyses your 🏫's tweets

🚀Uses Twitter's API to collect your school's most recent tweets
and create a word cloud from it and execute sentiment analysis using ML

## 📌 Contributing Countries

🇬🇧

## 👨‍🎓 Example

Made with the 'oundleschool' twitter account

![oundle school twitter account word cloud](source/static/oundleschool.png "word cloud from oundleschool")

## Setup

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

## Todo
- [x] 🐦 collect tweets
- [ ] 💻️ create website
- [ ] 📲 get input from website and download png


## 📧 Contact
### Email
- Angelo Giacco | giacco.angelo.s@gmail.com

## 🖊 Credits
[@Macr0Nerd](https://github.com/Macr0Nerd) for showing me how to use Twitter's API
like this project? check out his [Elon Bot](https://github.com/Macr0Nerd/elon-bot)!
