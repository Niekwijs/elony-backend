# other files/ imports
from flask_cors import CORS
from flask import Flask, send_file

# our files/ imports
from routing import tsla_routes, tweet_routes
from tweets import init_twitter_route
from beursdata_lijngrafiek import create_grafiek_matplotlib

app = Flask(__name__)
CORS(app)
init_twitter_route(app)
tsla_routes.init_tsla_routes(app)
tweet_routes.init_tweet_routes(app)

@app.route("/lijngrafiek_beursdata_matplotlib", methods=["GET"])
def tesla_beursdata_lijngrafiek_matplotlib():
    img_buffer = create_grafiek_matplotlib()
    return send_file(img_buffer, mimetype='image/png')
