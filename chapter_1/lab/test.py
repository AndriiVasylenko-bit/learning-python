import tweepy
import pandas as pd

# Your API/Consumer key
# Your API/Consumer Secret Key
# Your Access token key
# Your Access token Secret key
consumer_key = "B6fcmPXQ5aGjZSTfYlYiDa2gW"
consumer_secret = "SrqBg5SGWzLL2bcsx70bp2llfPYznIi1WmRcIE0ghptnSZKSwy"
access_token = "1525100515079643138-us0b2dblbzEbiZ3uEyrzowmOgUkqUI"
access_token_secret = "jufZOZPoDkvQv8We6RGYPD9tdw0bXZpTIyGuTc4YgWAHw"

# Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret)

# Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

search_query = "'Elon Musk''fired'-filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 100

try:
    # The number of tweets we want to retrieved from the search
    tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode='extended')

    # Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for
                            tweet in tweets]

    # Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

    # Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On, ', str(e))
