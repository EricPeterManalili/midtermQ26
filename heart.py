from flask_restful import Resource
from flask import *
from datetime import datetime
import json

def getHeartData():
    try:
        with open('./heart.json','r') as jsonData:
            heartData = json.load(jsonData)
        return heartData
    
    except NameError:
        print(NameError)

def writeHeartData(heartData):
    try: 
        with open("./heart.json", "w") as writeJson:
            writeJson.write(json.dumps(heartData))
    
    except NameError:
        print(NameError)

class HeartRecord(Resource):
    def get(self):
        return jsonify(getHeartData())
    
    def post(self):

        data = request.get_json()
        heartData = getHeartData()

        id = 1 if len(heartData) <= 0 else heartData[-1].get('heart_id') + 1

        newRecord = {
            "heart_id": id,
            "heart_rate": data["heart_rate"],
            "date": str(datetime.now())
        }

        heartData.append(newRecord)
        writeHeartData(heartData)

        return jsonify(heartData)

class HeartRecordSingle(Resource):
    def get(self, id):

        heartData = getHeartData()
        selectedRecord = ''

        for data in heartData: 
            if(data.get("heart_id") == int(id)):
                selectedRecord = data
            
            if(selectedRecord == ''):
                res = make_response()
                return make_response(jsonify({"message": "Does not Exist!"}), 404)

        return jsonify(selectedRecord)

    def patch(self, id):
        req = request.get_json()
        heartData = getHeartData()

        selectedRecord = ''

        for data in heartData:
            if(data.get("heart_id") == int(id)):
                selectedRecord = data

        if (selectedRecord == ''): return make_response(jsonify({"message": "Does not exist!"}), 404)

        if (req.get("heart_rate") != None): selectedRecord["heart_rate"] = req.get ("heart_rate")

        writeHeartData(heartData)

        return jsonify(heartData)

    def delete(self, id): 
        req = request.get_json()
        heartData = getHeartData()

        filteredData = []

        for data in heartData:
            if(data.get("heart_id") != int(id)):
                filteredData.append(data)

        heartData = filteredData

        writeHeartData(heartData)

        return jsonify(heartData)