from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
#from sqlalchemy import create_engine
from web_app.models import db, migrate, DATABASE_URI
from web_app.routes.stats_routes import stats_routes
import pandas




def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(stats_routes)

    ######## Configure Database Recommendation Storage 
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)
    
    
    
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)