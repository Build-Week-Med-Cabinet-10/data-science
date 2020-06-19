from flask import Blueprint, render_template

home_routes = Blueprint('home_routes',__name__)

@home_routes.route('/')

def index():
    print('Visiting About Page')
    return f'Hello World'

@home_routes.route('/recommendation/new')

def sample_form():
    print('Visiting rec Page')
    return render_template('sample_form.html', methods=['GET'])