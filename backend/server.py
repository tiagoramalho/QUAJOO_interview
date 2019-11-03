from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

#DB
debug = True
if debug == False:
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="admin",pw="quajoo",url="localhost:5432",db="quajoo")
else:
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="admin",pw="quajoo",url="quajoo_db:5432",db="quajoo")

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
app.config['PROPAGATE_EXCEPTIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models, resources

api.add_resource(resources.Cities, '/cities')
api.add_resource(resources.City, '/city')


@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
