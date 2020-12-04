import os
import re
from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps, loads

app = Flask(__name__)

mongo_client = mongo_client = MongoClient(f'mongodb://{os.environ["MONGO_INITDB_ROOT_USERNAME"]}'
                                          f':{os.environ["MONGO_INITDB_ROOT_PASSWORD"]}'
                                          f'@{os.environ["MONGODB_HOST"]}')
movies_db = mongo_client.movies_recommendation
col = movies_db.recommendation
success = 200
bad_request = 400


@app.route('/movies/<movie_id>', methods=["GET"])
def get_movie_by_id(movie_id):
    movie = dumps(col.find_one({"movieId": int(movie_id)}))
    return loads(movie), success


@app.route('/movies/search', methods=["GET"])
def search():
    term = request.args.get('q')
    if len(term) < 2:
        return {"message": "Put more than one Charecter"}, bad_request
    regx = re.compile(f"^{term}", re.IGNORECASE)
    movies = dumps(col.find({"title": regx}))
    response_search = {"movies": loads(movies)}
    return response_search, success


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
