from flask import Blueprint, jsonify, request, render_template #, flash, redirect
from data_base_models import db,Recommendation,parse_records

stats_routes = Blueprint('stats_routes', __name__)
MODEL_FILEPATH = #TODO

def train_and_save_model():
    print("TRAINING THE MODEL...")
    #TODO 
    print("SAVING THE MODEL...")
    with open(MODEL_FILEPATH, "wb") as model_file:
        pickle.dump(classifier, model_file)

    return classifier

def load_model():
    print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model

if __name__ == "__main__":

    

