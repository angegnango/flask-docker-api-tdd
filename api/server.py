from flask import Flask, jsonify, request
from flask_swagger import swagger

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
        return jsonify('you can search a network coverage by providing a query string ?q=xxxxx'), 200


    return app
