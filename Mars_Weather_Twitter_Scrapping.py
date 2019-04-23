import sys
import string
import pandas as pd
from twython import Twython

# Twitter API Keys
keys =  pd.read_csv('Oauths.csv')
APP_KEY = str(keys.iloc[0,0])
APP_SECRET = str(keys.iloc[0,1])
OAUTH_TOKEN = str(keys.iloc[0,2])
OAUTH_TOKEN_SECRET = str(keys.iloc[0,3])

# create twitter instance
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Access_token = twitter.obtain_access_token()
# t = Twython(APP_KEY, access_token=Access_token)

user_timeline = twitter.search(q='@MarsWxReport',
        count= 10,
        lang= 'en')


for tweets in user_timeline['statuses']:
    print tweets['text'] +"\n"

results = twitter.cursor(twitter.search, q='@MarsWxReport', include_rts=0)
for result in results:
    print(result)
