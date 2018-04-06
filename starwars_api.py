from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from mongoengine import *
import requests
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


class PlanetsList(Resource):
    def get(self):
        planets = Planet.objects
        return jsonify(planets=[i.serialize for i in planets]) # gets list of planets
api.add_resource(PlanetsList, '/planetlist')


class Planets(Resource):
    def get(self):
        if 'id' in request.form: # check if user searched using and id
            planetId = request.form['id']
            try:
                planet = Planet.objects(id=planetId)
                return jsonify(planet.serialize)
            except:
                return make_error(404, 'could not find a planet with this id')

        elif 'name' in request.form: # check if user searched using a name
            planetName = request.form['name']
            try:
                planet = Planet.objects.get(name__iexact=planetName) # this is case insensitive
                return jsonify(planet.serialize)
            except:
                return make_error(404, 'could not find a planet with this name')

        else:
            return make_error(400, 'you need and id or a name to do this search')

    def post(self):
        name = request.form['name']
        if Planet.objects(name__iexact=name): # check if planet has already been added
            return make_error(400, 'this planet is already in the database')

        climate = request.form['climate']
        terrain = request.form['terrain']
        appearances = []

        # SEARCH SWAPI DATABASE FOR THE PLANET ADDED
        r = requests.get('https://swapi.co/api/planets/?search={}'.format(name))
        json_result = r.json()

        if json_result['count'] > 0:
            # GET THE FILMS ATTRIBUTES
            films_urls = json_result['results'][0]['films']
            # GET EACH FILM'S TITLE
            for url in films_urls:
                r = requests.get(url)
                appearances.append(r.json()['title'])

        # CREATE NEW MOVIE
        newplanet = Planet(name=name, terrain=terrain, climate=climate, appearances=appearances)
        try: # check if fields were filled with proper types
            newplanet.save()
        except:
             return make_error(400, 'something went wrong. check your fields.')
        planets = Planet.objects
        return  {'message':'planet named {} was added successfully'.format(newplanet.name)}

    def delete(self):
        if 'id' in request.form: # check if user searched using and id
            planetId = request.form['id']
            try:
                planet = Planet.objects(id=planetId)
            except:
                return make_error(404, 'could not find a planet with this id')
            planet.delete()
            return {'message' : 'planet named {} removed successfully'.format(planet.name)}

        elif 'name' in request.form: # check if user used a name to find the planet
            planetQuery = request.form['name']
            try:
                planet = Planet.objects.get(name__iexact=planetQuery)
            except:
                return make_error(404, 'could not find a planet with this name')
            planet.delete()
            return {'message' : 'planet named {} removed successfully'.format(planet.name)}

        else: # error handling
            return make_error(400, 'you need and id or a name to do this search')

api.add_resource(Planets, '/planets')


if __name__ == '__main__':
    app.run(debug=False)
