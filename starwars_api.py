from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from mongoengine import *
from ApiResponseBuilder import ApiResponseBuilder
import json
from models import Planet

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

db = connect('planets')

# ENDPOINT CREATION


class Planets(Resource):
    def get(self):
        if 'name' in request.args:
            planets = Planet.objects(name__iexact=request.args.get('name'))
        else:
            planets = Planet.objects
        return jsonify(planets=[i.serialize for i in planets])

    def post(self):
        if ('name' not in request.args) or ('climate' not in request.args) or \
                ('terrain' not in request.args):
            return ApiResponseBuilder.error(400, 'name, climate and terrain fields are required to create a planet entry')

        name = request.args.get('name')
        if Planet.objects(name__iexact=name):
            return ApiResponseBuilder.error(400, 'this planet is already in the database')
        climate = request.args.get('climate')
        terrain = request.args.get('terrain')
        newplanet = Planet(name=name, terrain=terrain, climate=climate)
        newplanet.getAppearances()

        try:  # catch error if fields were incorrectly filled
            newplanet.save()
        except:
            return ApiResponseBuilder.error(400, 'something went wrong. check your fields.')

        return ApiResponseBuilder.success(201, 'planet named {} was added successfully'.format(newplanet.name), newplanet.serialize)

api.add_resource(Planets, '/planets')


class SinglePlanet(Resource):
    def get(self, planetid):
        try:
            planet = Planet.objects.get(id=planetid)
        except:
            return ApiResponseBuilder.error(404, 'could not find a planet with this id')
        return jsonify(planet.serialize)

    def delete(self, planetid):
        try:
            planet = Planet.objects.get(id=planetid)
        except:
            return ApiResponseBuilder.error(404, 'could not find a planet with this id')
        planet.delete()
        return ApiResponseBuilder.success(200, 'planet named {} removed successfully'.format(planet.name), None)

api.add_resource(SinglePlanet, '/planets/<string:planetid>')


if __name__ == '__main__':
    app.run(debug=False)
