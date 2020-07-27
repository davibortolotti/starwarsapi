import json
import os

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from marshmallow import exceptions as ma_exc
from mongoengine import *

from models import Planet
from schemas import PlanetSchema
from seed import seed
from ApiResponseBuilder import ApiResponseBuilder


app = Flask(__name__)
api = Api(app, catch_all_404s=True)

if os.getenv('env') == "docker":
    db = connect('planets', host="mongo")
else:
    db = connect('planets')

seed()

class Planets(Resource):
    def get(self):
        if 'terrain' in request.args:
            planets = Planet.objects(terrain__iexact=request.args.get('terrain'))
        elif 'climate' in request.args:
            planets = Planet.objects(climate__iexact=request.args.get('climate'))
        else:
            planets = Planet.objects
        # print(planets)
        response = Planet.schema(many=True).dump(planets)
        return response

    def post(self):
        try:
            result = PlanetSchema().load(request.json)
            newplanet = Planet(**result)
            if Planet.objects(name__iexact=newplanet.name):
                return ApiResponseBuilder.error('this planet is already in the database', 404)
            newplanet.get_appearances()
            newplanet.save()

        except ma_exc.ValidationError as err:
            return ApiResponseBuilder.error(err.messages, 400)

        return ApiResponseBuilder.success(f'planet named {newplanet.name} was added successfully', newplanet.serialized, 201)


class SinglePlanet(Resource):
    def get(self, planetid):
        try:
            planet = Planet.objects.get(id=planetid)
            return planet.serialized
        except Exception:
            return ApiResponseBuilder.error('could not find a planet with this id', 404)
        

    def delete(self, planetid):
        try:
            planet = Planet.objects.get(id=planetid)
        except Exception:
            return ApiResponseBuilder.error('could not find a planet with this id', 404)
        planet.delete()
        return ApiResponseBuilder.success(f'planet named {planet.name} removed successfully', None)

api.add_resource(Planets, '/planets')
api.add_resource(SinglePlanet, '/planets/<string:planetid>')

if __name__ == '__main__':
    app.run(debug=False)
