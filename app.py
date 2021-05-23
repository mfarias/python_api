from flask import Flask
# import required to run on windows 10
# https://github.com/flask-restful/flask-restful/pull/913
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource, Api, fields, marshal_with, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/user_api'
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

def applyFiltersAndPagination(query):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    name_ = request.args.get('name', type=str)
    if name_:
        query = query.filter_by(name=name_)
    login_ = request.args.get('login', type=str)
    if login_:
        query = query.filter_by(login=login_)
    email_ = request.args.get('email', type=str)
    if email_:
        query = query.filter_by(email=email_)
    return query.paginate(page, per_page)


class User(Resource):
    @app.route("/")
    def index():
        return "Users API"

    @marshal_with(resource_fields)
    def get(self, user_id):
        result = UserModel.query.filter_by(id=user_id).first()
        if result:
            return result, 200
        else:
            return abort(404)

api.add_resource(User, '/users/<user_id>')


class Users(Resource):

    @marshal_with(resource_fields)
    def get(self):
        query = UserModel.query
        result = applyFiltersAndPagination(query)
        return result.items

api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run()