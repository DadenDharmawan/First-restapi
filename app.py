# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os

#  import flask sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# initialization flask
app = Flask(__name__)

# initialization rest api
api = Api(app=app)

# initialization cors
CORS(app=app)

# database configuration
basedir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_DATABASE_URI"] = database
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

# initialization SQL Alchemy
db = SQLAlchemy(app=app)

# database model
class DatabaseModel(db.Model):
    # make database fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    address = db.Column(db.TEXT)
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False
            

# resource model
class DataResource(Resource):
    
    # get method
    def get(self):
        query = DatabaseModel.query.all()

        output = [
            {"name":data.name, "age":data.age, "address":data.address} for data in query
        ]
        
        response = {
            "message": "Data Successfully Queried!",
            "code": 200,
            "data": output
        }
        
        return response
    
    # post method
    def post(self):
        name = request.json["name"]
        age = request.json["age"]
        address = request.json["address"]
        
        db.create_all()
        modelDatabase = DatabaseModel(name=name, age=age, address=address)
        modelDatabase.save()
        
        
        response = {
            "message":"Data added successfully",
            "code": 200
        }
        return response

api.add_resource(DataResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=1000)