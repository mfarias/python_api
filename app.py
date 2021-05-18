from flask import Flask
# import required to run on windows 10
# https://github.com/flask-restful/flask-restful/pull/913
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource, Api, fields, marshal_with, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pojflcgsicdxcm:253c3360ac00e62aa1cf9354984ec9171ea640b6f68462f035bd83f0fd093a49@ec2-184-73-198-174.compute-1.amazonaws.com:5432/d3l6eje04o82ao'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    login = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, login={self.login}, email={self.email})'

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'login': fields.String,
    'email': fields.String,
}

class User(Resource):
    @app.route("/")
    def index():
        return "Users API"

    @marshal_with(resource_fields)
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)
        result = UserModel.query.paginate(page, per_page, False)
        return result.items

api.add_resource(User, '/users')

if __name__ == '__main__':
    app.run()