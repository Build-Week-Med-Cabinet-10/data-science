
from flask import Flask, Blueprint

from web_app.recommender import recommend_route

DATABASE_URI = ('sqlite:///Cannabis.db')


def create_app():

    APP = Flask(__name__)

    APP.register_blueprint(recommend_route)
    
    return APP

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)