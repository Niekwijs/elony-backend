# other files/ imports
from flask_cors import CORS
from flask import Flask

# our files/ imports
from utils.connector import DbConnector
from routing.tweet_routes import tweet_routes
from routing.tsla_routes import tsla_routes

app = Flask(__name__)
CORS(app)


# add different routing
app.register_blueprint(tweet_routes)
app.register_blueprint(tsla_routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)