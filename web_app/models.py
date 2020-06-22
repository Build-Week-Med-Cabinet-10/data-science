
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DF_FILEPATH = 'web_app/data/cannabis.csv'
DATABASE_URI = 'sqlite:////Users/jp/Desktop/data-science/web_app/Cannabis.db'

db = SQLAlchemy()

migrate = Migrate()


          

class User_Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(128))
    strain = db.Column(db.String(128), nullable=False)
    strain_type = db.Column(db.String)
    rating = db.Column(db.String)
    effect = db.Column(db.String(128))
    flavor = db.Column(db.String(128))
    description= db.Column(db.String)



    
def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records


