# other files/ imports
from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify
from json import loads

# our files/ imports
import beursdata_tabel
from data_loader import Loader


app = Flask(__name__)
CORS(app)
csv_loader = Loader()


@app.route("/tabel_tesla_beursdata")
def jacobinestrial():
    parsed_beursdata_tesla = beursdata_tabel.create_tabel()
    return jsonify({"parsed": parsed_beursdata_tesla})


@app.route("/tabel_tesla_beursdata/<start_date>/<end_date>", methods=["get"])
def get_tesla_bearsdata_date_range(start_date, end_date):
        df_tesla_stock = csv_loader.get_tesla_stock_range(start_date, end_date)
        json_res = df_tesla_stock.to_json(orient = "columns")
        parsed_data = loads(json_res)   

        print(f'[+] This is bieng send to the frontend: {parsed_data}')
        return parsed_data