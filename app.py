from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os  # core Python module

#  Initialize app with flask
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize API
api = Api(app)

# Initialize database ORM
db = SQLAlchemy(app)

# Initialize marshmallow
ma = Marshmallow(app)

# Route classes


class testRoute(Resource):
    def get(self):
        return jsonify({'status': 'test route'})


class defaultRoute(Resource):
    def get(self):
        return jsonify({'status': 'default route'})


# Adding route paths
api.add_resource(testRoute, '/testRoute')
api.add_resource(defaultRoute, '/')

# Run server
if __name__ == '__main__':
    app.run(debug=True)
