import tweepy
from Twitter_credentials import *

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
api = tweepy.API(auth)

tweeds = api.user_timeline(screen_name='Sunny_Tter',
                           count=10, include_rts=False, tweet_mode='extended')
for tweed in tweeds:
    print(tweed.full.text)
