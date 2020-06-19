from flask import Blueprint, jsonify, request, render_template #, flash, redirect
from data_base_models import db,Recommendation,parse_records

strain_routes = Blueprint('strain_routes', __name__)



@strain_routes.route("/recommendation/new")
def new_recommendation():
    return render_template("recommendation_form.html")

@strain_routes.route("/recommendation/create", methods=["POST"])
def create_recommendation():
    print("FORM DATA:", dict(request.form))
    
    new_recommendation = Recommendation(user_id = request.form["Effect"],
                                        name= request.form["Effect"], 
                                        type_strain = request.form["Flavor"],
                                        rating = 4.5,
                                        flavor = request.form["Flavor"],
                                        effect = request.form["Effect"],
                                        description = request.form["Flavor"])
    
    db.session.add(new_recommendation)
    db.session.commit()

    strain = parse_records(new_recommendation)
    jsonify(strain)
    return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "Strain": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")
