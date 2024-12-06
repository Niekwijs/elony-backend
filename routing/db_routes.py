from flask import jsonify, Blueprint
from repositories.db_repo import DikkeBuikenRepo
from utils.connector import DbConnector

# Maak de databaseverbinding, repository instantie en Blueprint voor de db-routes aan
db_con: DbConnector = DbConnector()
db_repo: DikkeBuikenRepo= DikkeBuikenRepo(db_con)
db_routes = Blueprint('db_routes', __name__)

# Route voor ophalen van gemiddelde gewicht data
@db_routes.route("/tabel_average_weight", methods=["GET"])
def weight_tabel():
    """
    Functie om gewichtsdata op te halen uit de database.

    Returns: 
    - Data in JSON format
    - Foutmelding als data ophalen niet is gelukt
    """
    try:
        parsed_weight_data = db_repo.get_all_weights()
        return jsonify({"res": parsed_weight_data}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500