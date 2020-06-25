

import os 
import requests
from flask import Flask, request, jsonify, Blueprint

import pickle
import sklearn
import pandas



recommend_route = Blueprint('recommend_route',__name__)


@recommend_route.route('/predict', methods=['GET','POST'])

def predict():
    '''
    Returns a JSON object of the recommended strain information 
    calculated from a users flavor and effect. 

    '''
    ### Load Files
    #Load Model
    KNN_FILEPATH = 'web_app/data/knn.pkl'
    print("LOADING THE MODEL...")
    with open(KNN_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    
    # Load Effects
    EFFECTS_FILEPATH = 'web_app/data/effects.pkl'
    print("LOADING EFFECTS..")
    with open(EFFECTS_FILEPATH, "rb") as effect_file:
        effects = pickle.load(effect_file)
    
    # Load Flavors
    FLAVOR_FILEPATH = 'web_app/data/flavors.pkl'
    print("LOADING FLAVORS...")
    with open(FLAVOR_FILEPATH, "rb") as flavors_file:
        flavors = pickle.load(flavors_file)

    
    # Load web request
    
    #from_web = dict(request.json) or dict(request.args) or dict(request.data)
    from_web = request.args or request.get_json()
    e = from_web['effect']
    f = from_web['flavor']

    ### Generate Recommendation
    # Use info to get vectors from pickled dictionaries
    effect = effects[e]
    flavor = flavors[f]

    # Generate query vector by adding these vectors
    query = effect + flavor

    # Run knn model using query vector. Needs to be reshaped
    result = saved_model.kneighbors(query.reshape(1,-1))
    DF_FILEPATH = 'web_app/data/cannabis.csv'
    df = pandas.read_csv(DF_FILEPATH)

    ### Get Strain names from model and locate strain information 
    strains = df.iloc[result[1][0]]['Strain'].to_list() 
    recommendation_dictionaries = []
    for i in range(2):
        rec = df[df['Strain']== strains[i]].reset_index()
        rec.columns =  ['id', 'strain', 'type','rating', 'effect', 'flavor', 'description']
        dictionary = rec.to_dict()
        recommendation_dictionaries.append(dictionary)
        
        
    return jsonify(recommendation_dictionaries) 
