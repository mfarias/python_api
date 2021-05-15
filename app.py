from flask import Flask
# import required to run on windows 10
# https://github.com/flask-restful/flask-restful/pull/913
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self):
        return {"user": {
            "id": 1,
            "name":"John Doe", 
            "login": "jdoe", 
            "email": "test@test.com"}
            }

api.add_resource(User, '/')

if __name__ == '__main__':
    app.run(debug=True)