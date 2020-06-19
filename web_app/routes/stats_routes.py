
from flask import Flask, Blueprint, request, jsonify, render_template
import os
import pickle
import sklearn
import pandas








stats_routes = Blueprint("stats_routes", __name__)


@stats_routes.route("/recommendation/new", methods=["POST"])

def predict():
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
    
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))
    from_web = dict(request.form)
    eff = request.form['effect']
    fla = request.form['flavor']
    print(eff)
    print(fla)
    #1. Web team sends this user query in some format(probably json)
    #from_web = {'effect':'Aroused', 'flavor': 'Sweet'} #json like object 
    
    #2. Use info to get vectors from pickled dictionaries
    #
    effect = effects[list(from_web.values())[0]]
    flavor = flavors[list(from_web.values())[1]]
    #3. Generate query vector by adding these vectors
    query = effect + flavor


    #4. Run knn model using query vector. Needs to be reshaped
    result = saved_model.kneighbors(query.reshape(1,-1))
    DF_FILEPATH = 'web_app/data/cannabis.csv'
    df = pandas.read_csv(DF_FILEPATH)

    #5. Result object will have the index location of recomendations to lookup in df

    strains = df.iloc[result[1][0]]['Strain'].tolist()


    #print(jsonify(result))   

    return render_template("results.html",
        effect= eff,
        flavor= fla,
        
        strains= strains[0])



