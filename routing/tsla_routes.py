from flask import jsonify, request, send_file, Blueprint
from repositories.tsla_repo import TslaRepo
from utils.connector import DbConnector
from utils.beursdata_lijngrafiek import create_grafiek_matplotlib
from datetime import datetime

db_con: DbConnector = DbConnector()
tsla_repo: TslaRepo = TslaRepo(db_con)

tsla_routes = Blueprint('tsla_routes', __name__)

@tsla_routes.route("/tabel_tesla_beursdata", methods=["GET"])
def tesla_tabel():
    try:
        parsed_beursdata_tesla = tsla_repo.get_beursdata_DBD001()
        return jsonify({"res": parsed_beursdata_tesla}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@tsla_routes.route("/tsla/get_all", methods=["GET"])
def get_all_tsla():
    try:
        res = tsla_repo.get_all()
        return jsonify({"res": res}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@tsla_routes.route("/tsla/get_by_date_range", methods=["GET"])
def get_tsla_by_date_range():
    
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    if not start_date or not end_date:
        return jsonify({"error": "start_date and end_date are required"}), 400

    try:
        datetime.fromisoformat(start_date)  
        datetime.fromisoformat(end_date)  
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    try:
        res = tsla_repo.get_by_date_range(start_date, end_date)
        return jsonify({"res": res}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@tsla_routes.route("/lijngrafiek_beursdata_matplotlib", methods=["GET"])
def tesla_beursdata_lijngrafiek_matplotlib():
    try:
        img_buffer = create_grafiek_matplotlib()
        return send_file(img_buffer, mimetype='image/png', as_attachment=True, attachment_filename='tsla_graph.png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500