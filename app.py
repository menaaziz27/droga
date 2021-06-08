from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

drug_args = reqparse.RequestParser()
drug_args.add_argument("name", type=str, help="drug name is required", required=True)

class Drug(Resource):
    def get(self):
        return {"drug name": "api is working"}

    def put(self):
        if request.method == "PUT":
            drug_name = drug_args.parse_args()
            try:
                print(request.form['name'])
            except:
                pass
            # # enter drug name into machine learning algorithm
            print(drug_name['name'])
            return {"data": drug_name}

            # return {"data": args}

api.add_resource(Drug, "/drugs")

if __name__ == "__main__":
    app.run(debug=True)
