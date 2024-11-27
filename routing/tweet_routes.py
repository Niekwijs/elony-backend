from flask import jsonify, request 
from utils.connector import DbConnector
from repositories.tweet_repo import TweetRepo
from tweet_details import get_tweet_details
from datetime import datetime

db_con: DbConnector = DbConnector()
tweet_repo: TweetRepo = TweetRepo(db_con)


def init_tweet_routes(app):
    @app.route('/tweet/get_by_id')
    def get_tweet_by_id():
        tweet_id = request.args["tweet_id"]
        res = tweet_repo.get_tweet_by_id(tweet_id)

        return jsonify({'res': res})
    
    @app.route('/tweet/get_all')
    def get_all_tweets():
        res = tweet_repo.get_all()

        return jsonify({'res': res})
    
    @app.route('/tweet/save_by_id', methods=['POST'])
    def save_by_id():
        tweet_id = request.args["tweet_id"]
        save_date = request.args["save_date"]
        save_date = datetime.fromisoformat(save_date)

        res = tweet_repo.save_tweet_by_id(tweet_id, save_date)

        return jsonify({'res': res})
    
    @app.route('/tweet/check_if_saved')
    def check_if_saved():
        tweet_id = request.args["tweet_id"]
        res = tweet_repo.check_if_saved(tweet_id)

        return jsonify({'res': res})
    
    @app.route('/tweet/<tweet_id>', methods=['GET'])
    def tweet_details(tweet_id):

        tweet_data = get_tweet_details(tweet_id)

        return jsonify(tweet_data)
    
    @app.route('/tweet/get_three_after_date')
    def get_three_after_date():
        date = request.args["date"]
        res = tweet_repo.get_three_after_date(date)

        return jsonify({'res': res})
    