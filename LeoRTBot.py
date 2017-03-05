import tweepy, time, sys, sched
from tweepy.auth import OAuthHandler
import logging


#Twitter Auth
CONSUMER_KEY = "PDXIyLYTKeIkgthFIDz6O8X0a"
CONSUMER_SECRET = "Ov9gqNPkPExTHWM2fg69RdpujFx9NUEp7G6BNpXMfqtrwAPwy6"
ACCESS_TOKEN = "838172993675268096-vJOtTCqNu8rpXFbASQAYBdsdF26RKD3"
ACCESS_TOKEN_SECRET = "E2CAA7Bf4h1NwWMUm4yIM8IktMRFQipbEZtnFjp9LKb2s"
auth_handler = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_handler.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter_client = tweepy.API(auth_handler)
logger = logging.getLogger("Bot")

while True:

    print("Beginnging to retweet..")
    try:
        for status in twitter_client.home_timeline():
            print "tweet id: " + str(status.id)
            twitter_client.retweet(status.id)


    except tweepy.TweepError as e:
        print(e.reason)

    print("Waiting 300 seconds")
    time.sleep(300)