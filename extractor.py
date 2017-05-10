import configparser

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

config = configparser.ConfigParser()
config.read('.twitter')


#config keys
consumer_key = config.get('apikey', 'key')
consumer_secret = config.get('apikey', 'secret')
access_token = config.get('token', 'token')
access_token_secret = config.get('token', 'secret')

#oauth
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

import csv
with open('tweetsOutput.csv', mode='a') as f:
    writer = csv.writer(f)
    writer.writerow(['Id', 'Name', 'Text'])
#query and search
    api = API(auth, wait_on_rate_limit=True)
    search_query = 'Reforma da previdência OR Reforma da previdencia' \
        ' OR reforma da previdencia OR previdencia'
    for tweet in Cursor(api.search, q=search_query).items(500):
        writer.writerow([tweet.id, tweet.user.screen_name, tweet.text])
    search_query = 'Terceirização OR terceirizacao OR ' \
            'projeto de lei da terceirização'
    for tweet in Cursor(api.search, q=search_query).items(500):
        writer.writerow([tweet.id, tweet.user.screen_name, tweet.text])
