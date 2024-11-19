# other files/ imports
from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify, send_file
from json import loads

# our files/ imports
import beursdata_tabel
from data_loader import Loader
from tweet_details import get_tweet_details
from beursdata_lijngrafiek import create_grafiek_matplotlib

#DBD-006
from tweets import init_twitter_route

# init_twitter_route(app)

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
        json_res = df_tesla_stock.to_json(orient = "columns")
        parsed_data = loads(json_res)   
        
        print(f'[+] This is bieng send to the frontend: {parsed_data}')
        return parsed_data


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

