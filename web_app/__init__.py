from flask import Flask
from data_base_models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.strain_routes import strain_routes

DATABASE_URI = "sqlite:////Users/jp/Desktop/data-science/web_app.db"

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(strain_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)