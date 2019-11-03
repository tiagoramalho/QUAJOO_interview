from server import app

from flask_restful import Resource, reqparse
from flask import request
from models import CityModel

import requests as req
import json

OpenWeather = "d0cfd84cbad18222482ce87fad30ba96"


class Cities(Resource):
    def get(self):
        cities = CityModel.query.all()
        ids = ""
        r_cities = []
        if (len(cities) > 0):
            for c in cities:
                ids += str(c.open_id) +","

            ids = ids[:-1]
            resp = req.post("http://api.openweathermap.org/data/2.5/group?id="+ids+"&APPID="+OpenWeather)
            json_data = json.loads(resp.content)

            for c in json_data["list"]:
                r_cities.append({"name":c["name"], "temp":c["main"]["temp"]})
            

        return r_cities




class City(Resource):
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('open_id', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()

        if CityModel.find_by_open_id(data['open_id']):
            return {'message': 'City {} already exists'. format(data['open_id'])}

        resp = req.post("http://api.openweathermap.org/data/2.5/weather?id="+data["open_id"] +"&APPID="+OpenWeather)
        json_data = json.loads(resp.content)

        city = CityModel(
                name = json_data["name"],
                open_id = data['open_id']
        )
        try:
            city.save_to_db()
        except Exception as e:
            print(e)
            return {"error" : "Internal Error"}
        return {data["open_id"]:json_data["main"]["temp"]}
