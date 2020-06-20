from flask import Flask
#from sqlalchemy import create_engine
#from web_app.db_models import db, migrate, DATABASE_URI, DF_FILEPATH
from web_app.routes.stats_routes import stats_routes
import pandas




def create_app():
    app = Flask(__name__)
    


    ######## Configure Database for Strain and User Recommendation Storage 
    # app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    # db.init_app(app)
    # migrate.init_app(app, db)
    
    # engine = create_engine(DATABASE_URI, echo=False)
    # df = pandas.read_csv(DF_FILEPATH)
    # df.to_sql(name = 'Strains',con=engine, if_exists='replace',index_label= 'id')

    
    app.register_blueprint(stats_routes)
    
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)