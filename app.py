# other files/ imports
from flask_cors import CORS
from flask import Flask

# our files/ imports
from utils.connector import DbConnector
from repositories.tsla_repo import TslaRepo
from repositories.tweet_repo import TweetRepo
from routing import tsla_routes, tweet_routes


app = Flask(__name__)
CORS(app)

# db connection
db_con: DbConnector = DbConnector()

# add different routing
tsla_routes.init_tsla_routes(app)
tweet_routes.init_tweet_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)