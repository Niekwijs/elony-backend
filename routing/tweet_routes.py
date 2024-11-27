from flask import jsonify, request, Blueprint
from utils.connector import DbConnector
from repositories.tweet_repo import TweetRepo
from datetime import datetime


tweet_routes = Blueprint('tweet_routes', __name__)
db_con: DbConnector = DbConnector()
tweet_repo: TweetRepo = TweetRepo(db_con)


@tweet_routes.route('/tweet/get_by_id', methods=["GET"])
def get_tweet_by_id():
    tweet_id = request.args.get("tweet_id")
    res = tweet_repo.get_tweet_by_id(tweet_id)

    if not tweet_id:
        return jsonify({"error": "tweet_id is required"}), 400
    
    try:
        res = tweet_repo.get_tweet_by_id(tweet_id)
        if not res:
            return jsonify({"message": "Tweet not found"}), 404
        return jsonify({"res": res}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@tweet_routes.route('/tweet/get_all', methods=["GET"])
def get_all_tweets():
    try:
        res = tweet_repo.get_all()
        return jsonify({"res": res}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@tweet_routes.route('/tweet/save_by_id', methods=['POST'])
def save_by_id():
    tweet_id = request.args.get("tweet_id")
    save_date_str = request.args["save_date"]

    res = tweet_repo.save_tweet_by_id(tweet_id, save_date)

    if not tweet_id or not save_date_str:
            return jsonify({"error": "tweet_id and save_date are required"}), 400

    try:
        save_date = datetime.fromisoformat(save_date_str)
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400
    
    try:
        res = tweet_repo.save_tweet_by_id(tweet_id, save_date)
        return jsonify({"message": "Tweet saved successfully", "res": res}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@tweet_routes.route('/tweet/check_if_saved', methods=["GET"])
def check_if_saved():
    tweet_id = request.args.get("tweet_id")
    
    if not tweet_id:
        return jsonify({"error": "tweet_id is required"}), 400
    
    try:
        res = tweet_repo.check_if_saved(tweet_id)
        return jsonify({"data": res}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@tweet_routes.route('/tweet/get_three_after_date', methods=["GET"])
def get_three_after_date():
    date_str = request.args.get("date")
    
    if not date_str:
        return jsonify({"error": "date is required"}), 400
    
    try:
        date = datetime.fromisoformat(date_str)
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400
    
    try:
        res = tweet_repo.get_three_after_date(date)
        return jsonify({"data": res}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500