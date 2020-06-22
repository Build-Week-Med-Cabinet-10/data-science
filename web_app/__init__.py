

import os 
from dotenv import load_dotenv
from flask import Flask

from flask_sqlalchemy import SQLAlchemy 
from web_app.models import db, migrate, DATABASE_URI
from web_app.routes.stats_routes import stats_routes
import pandas


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    db.init_app(app)
    migrate.init_app(app, db)
    
    
    app.register_blueprint(stats_routes)
    
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)