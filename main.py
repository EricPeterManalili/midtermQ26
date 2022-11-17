from datetime import datetime
from flask import Flask, request, jsonify
from flask_restful import Api
from heart import *
import json
import os 

app = Flask (__name__)
api = Api(app)

api.add_resource(HeartRecord, "/heart")
api.add_resource(HeartRecordSingle, "/heart/<id>")


# with open ("./heart.json", "r") as jsonData:
#     heartData = json.load(jsonData)

# @app.route('/', methods = ["GET"])
# def home():
#     return "Hello World!"

# @app.route('/heart', methods=["POST"])
# def addNewRecord():
#     myJson = request.get_json()

#     print(heartData)

#     id = 1 if len(heartData) <= 0 else heartData[-1]["id"] + 1

#     newRecord = {
#         "id": id,
#         "heart_rate": myJson["heart_rate"],
#         "date": str(datetime.now())
#     }

#     heartData.append(newRecord)

#     print(heartData)

    

#     return jsonify(heartData)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug = True )