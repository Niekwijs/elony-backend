from flask import jsonify, request 
from repositories.tsla_repo import TslaRepo
from utils.connector import DbConnector
db_con: DbConnector = DbConnector()
tsla_repo: TslaRepo = TslaRepo(db_con)
def init_tsla_routes(app):
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