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
    parsed_beursdata_tesla = beursdata_tabel.create_tabel()
    
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
     

@app.route('/tweet/<tweet_id>', methods=['GET'])
def tweet_details(tweet_id):
    tweet_data = get_tweet_details(tweet_id)

    return jsonify(tweet_data)


# @app.route("/lijngrafiek_beursdata")
# def tesla_beursdata_lijngrafiek():
#     parsed_beursdata_tesla = create_grafiek()
#     return jsonify({"parsed": parsed_beursdata_tesla})

@app.route("/lijngrafiek_beursdata_matplotlib", methods=["GET"])
def tesla_beursdata_lijngrafiek_matplotlib():
    img_buffer = create_grafiek_matplotlib()
    return send_file(img_buffer, mimetype='image/png')
