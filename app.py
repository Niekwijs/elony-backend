# other files/ imports
from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify
from json import loads

# our files/ imports
import beursdata_tabel
from data_loader import Loader
from tweet_details import get_tweet_details


app = Flask(__name__)
CORS(app)
csv_loader = Loader()


@app.route("/tabel_tesla_beursdata")
def tesla_tabel():
    parsed_beursdata_tesla = beursdata_tabel.create_tabel()
    
    return jsonify({"parsed": parsed_beursdata_tesla})


@app.route("/tabel_tesla_beursdata/<start_date>/<end_date>", methods=["get"])
def get_tesla_bearsdata_date_range(start_date, end_date):
        df_tesla_stock = csv_loader.get_tesla_stock_range(start_date, end_date)
        json_res = df_tesla_stock.to_json(orient = "records")
        parsed_data = loads(json_res)

        return parsed_data

@app.route('/tweet/<tweet_id>', methods=['GET'])
def tweet_details(tweet_id):
    tweet_data = get_tweet_details(tweet_id)
    
    return jsonify(tweet_data)
