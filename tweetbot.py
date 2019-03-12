import tweepy
import markovify
from twitter_credentials import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

with open('TEXT') as corpus_file:
          corpus = corpus_file.read()

model = markovify.Text(corpus)

message = model.make_short_sentence(100).lower()



api.update_status(message)
