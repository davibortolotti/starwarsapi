from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from mongoengine import *

import json
from models import Planet

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

db = connect('planets')


def make_error(status_code, message):
    response = jsonify({
     'status': status_code,
     'message': message
    })
    response.status_code = status_code
    return response

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
            return make_error(400, 'name, climate and terrain fields are' +
                                   'required to create a planet entry')

        name = request.args.get('name')
        if Planet.objects(name__iexact=name):
            return make_error(400, 'this planet is already in the database')
        climate = request.args.get('climate')
        terrain = request.args.get('terrain')
        newplanet = Planet(name=name, terrain=terrain, climate=climate)
        newplanet.getAppearances()

        try:  # check if fields were filled with proper types
            newplanet.save()
        except:
            return make_error(400, 'something went wrong. check your fields.')
        response = jsonify(result=newplanet.serialize,
                           message='planet named {} was added successfully'.format(newplanet.name))
        response.status_code = 201
        return response

api.add_resource(Planets, '/planets')


class SinglePlanet(Resource):
    def get(self, planetid):
        try:
            planet = Planet.objects.get(id=planetid)
        except:
            return make_error(404, 'could not find a planet with this id')
        return jsonify(planet.serialize)

    def delete(self, planetid):
        try:
            planet = Planet.objects.get(id=planetid)
        except:
            return make_error(404, 'could not find a planet with this id')
        planet.delete()
        return {'message': 'planet named {} removed successfully'.format(planet.name)}

api.add_resource(SinglePlanet, '/planets/<string:planetid>')


if __name__ == '__main__':
    app.run(debug=False)
