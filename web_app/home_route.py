from flask import Blueprint

home_route = Blueprint('home_route',__name__)

@home_route.route('/')

def index():
    print('Visiting About Page')
    return f'/predict?effect=Creative&flavor=Apple -> to the end of the url'

