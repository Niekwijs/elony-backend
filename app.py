# other files/ imports
from flask_cors import CORS
from flask import Flask, jsonify, request, send_file
from json import loads

# our files/ imports
import beursdata_tabel
from tweet_details import get_tweet_details
from utils.connector import DbConnector
from repositories.tsla_repo import TslaRepo
from repositories.tweet_repo import TweetRepo
from tweets import init_twitter_route
from beursdata_lijngrafiek import create_grafiek_matplotlib

app = Flask(__name__)
CORS(app)
init_twitter_route(app)

# db connection
db_con: DbConnector = DbConnector()

# repositories
tsla_repo: TslaRepo = TslaRepo(db_con)
tweet_repo: TweetRepo = TweetRepo(db_con)


@app.route("/tabel_tesla_beursdata")
def tesla_tabel():
    parsed_beursdata_tesla = tsla_repo.get_beursdata_DBD001()
    
    return jsonify({"parsed": parsed_beursdata_tesla})

@app.route("/tsla/get_all")
def get_all_tsla():
    res = tsla_repo.get_all()

    return jsonify({"res": res})

@app.route("/tsla/get_by_date_range")
def get_tsla_by_date_range():
    start_date = request.args["start_date"]
    end_date = request.args["end_date"]

    res = tsla_repo.get_by_date_range(start_date, end_date)

    return jsonify({"res": res})

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

    res = tweet_repo.save_tweet_by_id(tweet_id)

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
        

@app.route("/lijngrafiek_beursdata_matplotlib", methods=["GET"])
def tesla_beursdata_lijngrafiek_matplotlib():
    img_buffer = create_grafiek_matplotlib()
    return send_file(img_buffer, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)