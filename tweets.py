import os
import pandas as pd
from json import loads, dumps
from flask import jsonify

def init_twitter_route(app):
    @app.route("/ELONTWITTERANALYSE", methods = ['GET'])
    def get_tweets():
        try:
            #CSV-bestand inladen
            tweets = pd.read_csv("./data/TweetsElonMusk.csv")
            #Alleen relevante kolommen selecteren
            relevant_data = tweets[["date", "time", "tweet"]]
            #Converteer naar JSON
            tweets_json = relevant_data.to_dict(orient="records")
            return jsonify(tweets_json)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    @app.route("/ELONTWITTERDETAIL/<tweet_id>", methods=['GET'])
    def get_tweet_details(tweet_id):
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
