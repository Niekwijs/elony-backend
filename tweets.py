import pandas as pd
from json import loads, dumps

def init_twitter_route():
    @app.route("/ELONTWITTERANALYSE", methods = ['GET'])
    def get_tweets():
        try:
            #CSV-bestand inladen
            tweets = pd.read_csv("TweetsElonMusk.csv")
            #Alleen relevante kolommen selecteren
            relevant_data = tweets[["date", "time", "tweet"]]
            #Converteer naar JSON
            tweets_json = relevant_data.to_dict(orient="records")
            return jsonify(tweets_json)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
