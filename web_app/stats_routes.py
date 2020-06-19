
from flask import Flask, jsonify
import os
import pickle
import sklearn
import pandas




#app = Flask(__name__)
#@app.route("/predict", methods=["POST"])



def predict():
    # Load Model
    KNN_FILEPATH = 'web_app/knn.pkl'
    print("LOADING THE MODEL...")
    with open(KNN_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    # Load Effects
    EFFECTS_FILEPATH = 'web_app/effects.pkl'
    print("LOADING EFFECTS..")
    with open(EFFECTS_FILEPATH, "rb") as effect_file:
        effects = pickle.load(effect_file)
    #print(effects)
    # Load Flavors
    FLAVOR_FILEPATH = 'web_app/flavors.pkl'
    print("LOADING FLAVORS...")
    with open(FLAVOR_FILEPATH, "rb") as flavors_file:
        flavors = pickle.load(flavors_file)
    #print(flavors)
    print("PREDICT ROUTE...")
    #print("FORM DATA:", dict(request.form))
    
    #1. Web team sends this user query in some format(probably json)
    from_web = {'effect':'Aroused', 'flavor': 'Sweet'} #json like object 
    
    #2. Use info to get vectors from pickled dictionaries
    effect = effects['Aroused']
    flavor = flavors['Sweet']
    #3. Generate query vector by adding these vectors
    query = effect + flavor


    #4. Run knn model using query vector. Needs to be reshaped
    result = saved_model.kneighbors(query.reshape(1,-1))
    DF_FILEPATH = 'web_app/cannabis.csv'
    df = pandas.read_csv(DF_FILEPATH)

    #5. Result object will have the index location of recomendations to lookup in df
    print(df.iloc[result[1][0]]['Strain'].tolist())

    print(result)   

    return print(df.iloc[result[1][0]]['Strain'].tolist())#jsonify(result)




if __name__ == "__main__":
    predict()

