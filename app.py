from flask import Flask
from flask_cors import CORS
import beursdata_tabel
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)


@app.route("/tabel_tesla_beursdata")
def jacobinestrial():
    parsed_beursdata_tesla = beursdata_tabel.create_tabel()
    return jsonify({"parsed": parsed_beursdata_tesla})