from flask_restful import Resource
import json


class Echo(Resource):
  def get(self, echo):
    print(echo)
    data_set = {"Status": "ok", "echo": echo}
    json_dump = json.dumps(data_set)

    print(json_dump)

    return json_dump, 200
