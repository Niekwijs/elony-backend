import pandas as pd 
from json import loads, dumps

def get_tweet_details(tweet_id):
    filepath = "data/TweetsElonMusk.csv"
    df_tweet_details = pd.read_csv(filepath)
    print(df_tweet_details.columns)

    tweet_row = df.iloc[int(tweet_id)]  # select tweetrow in dataframe

    tweet_data = tweet_row.fillna("N/A").to_json()

    return tweet_data