import tweepy
from Twitter_credentials import *



import os  # MS-Struktur laden
# Wechsle ins Unterverzeichniss
os.chdir("youtube-gravitar_pythonuebungen\\6-Twitter")

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wordcloud = WordCloud(width=1920, height=1200)

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
api = tweepy.API(auth)
text = ''

tweeds = api.user_timeline(screen_name='Sunny_Tter',
                           count=10, include_rts=False, tweet_mode='extended')
for tweed in tweeds:
    text = text + ' '+ tweed.full_text

STOPWORDS.update(['http', 'co', 'https'])
wordcloud.generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()