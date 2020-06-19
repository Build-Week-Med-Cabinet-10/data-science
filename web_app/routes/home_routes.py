from flask import Blueprint

home_routes = Blueprint('home_routes',__name__)

@home_routes.route('/')

def index():
    print('Visiting home Page')
    return 'Hello World'

@home_routes.route('/about')

def about():
    print('Visiting About Page')
    return 'About Me'

