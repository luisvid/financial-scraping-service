from flask import Flask
from flask_restful import Api

from resources.dollar import Dollar
from resources.cedears import Cedears
from resources.echo import Echo

app = Flask(__name__)
api = Api(app)

@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

api.add_resource(Echo, "/echo/<string:echo>")
api.add_resource(Dollar, "/dollar")
api.add_resource(Cedears, "/cedears")


if __name__ == "__main__":
  app.run()