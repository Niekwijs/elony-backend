import os
import pandas as pd
from json import loads, dumps
from flask import jsonify

#tweets = None

#def init_twitter_route(app):
#    global tweets
#    tweets = pd.read_csv("./data/TweetsElonMusk.csv")
#    tweets['id'] = range(len(tweets))

def init_twitter_route(app):
    #tweets = pd.read_csv("./data/TweetsElonMusk.csv")
    @app.route("/ELONTWITTERANALYSE", methods = ['GET'])
    def get_tweets():
        try:
            #CSV-bestand inladen
            
            #Alleen relevante kolommen selecteren
            relevant_data = tweets[["date", "time", "tweet", "id"]]
            #Converteer naar JSON
            tweets_json = relevant_data.to_dict(orient="records")
            return jsonify(tweets_json)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    @app.route("/ELONTWITTERDETAIL/<tweet_id>", methods=['GET'])

    def get_tweet_details(tweet_id):
        print("qq")
        try:
            # Zoek de specifieke tweet op basis van ID
            tweet_details = tweets[tweets['id'] == int(tweet_id)].to_dict(orient="records")
            
            # Als geen tweet gevonden wordt
            if not tweet_details:
                return jsonify({"error": "Tweet not found"}), 404

            # Retourneer alle velden van de gevonden tweet
            return jsonify(tweet_details[0])  # Retourneer de eerste match als JSON
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Dataset één keer inladen en meegeven bij het initialiseren
tweets = pd.read_csv("./data/TweetsElonMusk.csv")
#tweets['id'] = range(len(tweets))  # Voeg een unieke ID-kolom toe
