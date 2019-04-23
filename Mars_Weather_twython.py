# Import the Twython class
from twython import Twython
import pandas as pd

# Twitter API Keys
keys =  pd.read_csv('Oauths.csv')
APP_KEY = str(keys.iloc[0,0])
APP_SECRET = str(keys.iloc[0,1])
OAUTH_TOKEN = str(keys.iloc[0,2])
OAUTH_TOKEN_SECRET = str(keys.iloc[0,3])

# Instantiate an object
python_tweets = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Create our query
query = {'q': 'learn python',
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        }

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)