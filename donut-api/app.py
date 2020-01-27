from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)



class Donut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    quantity = db.Column(db.Integer(), unique=False)
    price = db.Column(db.String(), unique=False)
    description = db.Column(db.String(), unique=False)
    image_url = db.Column(db.String(), unique=False)
    

    
    def __init__(self, name, quantity, price, description, image_url):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.description = description
        self.image_url = image_url


class DonutSchema(ma.Schema):
    class Meta:
        fields = ('name', 'quantity', 'price', 'description', 'image_url')


donut_schema = DonutSchema()
donuts_schema = DonutSchema(many=True)

# Endpoint to create a new donut
@app.route('/donut', methods=["POST"])
def add_donut():
    name = request.json['name']
    quantity = request.json['quantity']
    price = request.json['price']
    description = request.json['description']
    image_url = request.json['image_url']

    new_donut = Donut(name, quantity, price, description, image_url)

    db.session.add(new_donut)
    db.session.commit()

    donut = Donut.query.get(new_donut.id)

    return donut_schema.jsonify(donut)


# Endpoint to query all donuts
@app.route("/donuts", methods=["GET"])
def get_donuts():
    all_donuts = Donut.query.all()
    result = donuts_schema.dump(all_donuts)
    return jsonify(result)


# Endpoint for querying a single donut
@app.route("/donut/<id>", methods=["GET"])
def get_donut(id):
    donut = Donut.query.get(id)
    return donut_schema.jsonify(donut)


# Endpoint for updating a donut
@app.route("/donut/<id>", methods=["PUT"])
def donut_update(id):
    donut = Donut.query.get(id)
    name = request.json['name']
    quantity = request.json['quantity']
    price = request.json['price']
    description = request.json['description']
    image_url = request.json['image_url']

    donut.name = name
    donut.quantity = quantity
    donut.price = price
    donut.description = description
    donut.image_url = image_url

    db.session.commit()
    return donut_schema.jsonify(donut)


# Endpoint for deleting a record
@app.route("/donut/<id>", methods=["DELETE"])
def donut_delete(id):
    donut = Donut.query.get(id)
    db.session.delete(donut)
    db.session.commit()

    return "Donut was successfully deleted"


if __name__ == '__main__':
    app.run(debug=True)