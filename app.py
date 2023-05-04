# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi flask
app = Flask(__name__)

# inisiasi rest api
api = Api(app=app)

# inisiasi cors
CORS(app=app)

# inisiasi data dengan dictionary
data = {}

# class resource
class DataResource(Resource):
    
    # method get
    def get(self):
        return data
    
    # method post
    def post(self):
        name = request.json["name"]
        address = request.json["address"]
        
        data["name"] = name
        data["address"] = address
        
        response = {"message":"Data added successfully"}
        return response

api.add_resource(DataResource, "/", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=1000)