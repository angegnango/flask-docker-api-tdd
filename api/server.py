from flask import Flask, jsonify, request
from flask_swagger import swagger
from api import handler
from api import db

def init_server():

    app = Flask(__name__)

    @app.route('/')
    def index():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Network coverage endpoint"
        return jsonify(swag)


    @app.route('/api/v1/search')
    def search():

        query = request.args.get('q')
        
        if not (query is None):
            city = handler.retrieve_city(query)
            return jsonify(db.search(city)), 200
        else:
            return jsonify('you can search a network coverage by providing a query string ?q=xxxxx'), 200


    return app
