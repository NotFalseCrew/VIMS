from flask import Flask, request, jsonify
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

# Init DB
db = SQLAlchemy(app)

# Init marshmellow
ma = Marshmallow(app)


@app.route('/', methods=['GET'])
def all():
    return jsonify({'status': 'OK'})


# Run server
if __name__ == '__main__':
    app.run(debug=True)
