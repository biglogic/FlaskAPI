from flask import Flask
from db_connection import get_data
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/veg')
def get_veg():
    return get_data('vegetagles ')
    
@app.route('/fruits')
def get_fruits():
    return get_data("fruits")