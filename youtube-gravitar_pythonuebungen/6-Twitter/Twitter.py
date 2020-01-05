import tweepy
from Twitter_credentials import *



import os  # MS-Struktur laden
# Wechsle ins Unterverzeichniss
os.chdir("youtube-gravitar_pythonuebungen\\6-Twitter")

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("Teil_05_Alice_in_wonderland.txt") as f:
    text = f.read()

wordcloud = WordCloud(width=1920, height=1200)

STOPWORDS.add('said')
STOPWORDS.add('illustration')

wordcloud.generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()


auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
api = tweepy.API(auth)

tweeds = api.user_timeline(screen_name='Sunny_Tter',
                           count=10, include_rts=False, tweet_mode='extended')
for tweed in tweeds:
    print(tweed.full.text)