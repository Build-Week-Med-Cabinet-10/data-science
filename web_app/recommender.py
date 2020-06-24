

import os 
import requests
from flask import Flask, request, jsonify, Blueprint

import pickle
import sklearn
import pandas




recommend_route = Blueprint('recommend_route',__name__)

@recommend_route.route('/', methods=['GET','POST'])


def predict():
    '''
    Returns a JSON object of the recommended strain information 
    calculated from a users flavor and effect. 

    '''
    
    # Load Model
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
    
    # Test Request
    from_web = {'Effect':'Creative','Flavor':'Apple'}
    
    # Load web request
    #from_web = dict(request.get_data())
    
    web_query = list(from_web.values())
    effect = effects[web_query[0]]
    flavor = flavors[web_query[1]]

    
    # Generate Recommendation
    print("RECOMMENDING...")
    

    # Use info to get vectors from pickled dictionaries
    effect = effects[web_query[0]]
    flavor = flavors[web_query[1]]

    # Generate query vector by adding these vectors
    query = effect + flavor

    # Run knn model using query vector. Needs to be reshaped
    result = saved_model.kneighbors(query.reshape(1,-1))
    DF_FILEPATH = 'web_app/data/cannabis.csv'
    df = pandas.read_csv(DF_FILEPATH)

    #5 Result object will have the index location of recomendations to lookup in df
    strains = df.iloc[result[1][0]]['Strain'].to_list() 
    rec_one = df[df['Strain']== strains[0]].reset_index()
    #rec_two = df[df['Strain']== strains[1]].reset_index()
    #rec_three = df[df['Strain']== strains[2]].reset_index()
    rec_one.columns =  ['id', 'strain', 'type','rating', 'effect', 'flavor', 'description']
    dictionary = rec_one.to_dict()


    
   
    return jsonify(dictionary) 
