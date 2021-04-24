from flask import Flask
from flask_restful import Resource, Api, reqparse
from algorithms import leftRightSum
from flask_cors import CORS
# creating  a Flask instance
app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route("/",methods=['POST', 'OPTIONS'])
def index():
    return "Welcome to Left-Right-Sum Algorithm"

class LeftRightSum(Resource):    
    def post(self):
        
        parser = reqparse.RequestParser();
        parser.add_argument('input_array',type=list, location='json', required=True)
        
        args = parser.parse_args()

        # the input arrays should run through the algorithm and returns the value
        # exceptions to be handled
        return(leftRightSum(args['input_array'])), 200



api.add_resource(LeftRightSum, '/left-right-sum')