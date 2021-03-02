from flask import Flask
from flask_restful import Api

from resources.dollar import Dollar
from resources.bonos_usd_usd import BonosUsdUsd
from resources.bonos_usd_ars import BonosUsdArs
from resources.bonos_ars import BonosArs
from resources.cedears import Cedears
from resources.rofex import Rofex
from resources.rofex20 import Rofex20
from resources.spmerval import Spmerval
from resources.echo import Echo

app = Flask(__name__)
api = Api(app)

# workaround to avoid the Flask-RESTful problems with CORS.
@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

# API endpoints
api.add_resource(Echo, "/echo/<string:echo>")
api.add_resource(Dollar, "/dollar")
api.add_resource(BonosUsdUsd, "/bonosusd")
api.add_resource(BonosUsdArs, "/bonosusdars")
api.add_resource(BonosArs, "/bonosars")
api.add_resource(Cedears, "/cedears")
api.add_resource(Rofex, "/rofex")
api.add_resource(Spmerval, "/spmerval")
api.add_resource(Rofex20, "/rofex20")


if __name__ == "__main__":
  app.run()