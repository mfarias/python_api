from flask import Flask
# import required to run on windows 10
# https://github.com/flask-restful/flask-restful/pull/913
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource, Api, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

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
    @marshal_with(resource_fields)
    def get(self):
        result = UserModel.query.all()
        return result

api.add_resource(User, '/')

if __name__ == '__main__':
    app.run(debug=True)