#An API in python

import flask
from flask import request, jsonify

#create a flask object and enable debug messages if something goes wrong
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Create some test data for our catalog in the form of a list of dictionaries
books = [
        {'id': 0,
            'Character': 'Gandalf The Grey',
            'Location': 'Isengard',
            'Quote': 'You Shall Not Pass!',
            'Style': 'Mage'},
        {'id': 1,
            'Character': 'Frodo Baggins',
            'Location': 'The Shire',
            'Quote': 'It is useless to meet revenge with revenge: It will heal nothing.',
            'Style': 'Hobbit'},
        {'id': 2,
            'Character': 'Gollum',
            'Location': 'Dark Deep of the Misty Mountains',
            'Quote': 'MY PRECIOUS!!!!!!',
            'Style': 'Lurker'}
        ]



#Create a homepage with routing and and HTML webpage
@app.route('/', methods=['GET'])
def home():
    return "<h1>Lord of the Rings API</h1><p>This site is a prototype API for distant reading of LOTR characters.</p><button onclick=\"window.location.href='http://127.0.0.1:5000/links';\">One Link to Rule Them All ;)</button>"


#A route to return all the available entries in our catalog in JSON format
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #Check if an ID was provided as part of the URL
    #If ID is provided, assign it to a variable
    #If no ID is provided, display an error in the browser
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    #Create an empty list for our results
    results = []

    #Loop through the data and match results that fit the requested ID
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    #Use jsonify to convert list of dicts to JSON format
    return jsonify(results)

@app.route('/links', methods=['GET'])
def buttons():
    return "<h1>Links</h1><button onclick=\"window.location.href='http://google.com';\">GOOGLE It</button><button onclick=\"window.location.href='http://codecademy.com';\">Learn To Code</button><button onclick=\"window.location.href='http://127.0.0.1:5000/api/v1/resources/books/all';\">LOTD Characters</button>"

app.run()
