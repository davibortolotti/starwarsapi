from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from mongoengine import *
import requests
import json

app = Flask(__name__)
api = Api(app)

db = connect('planets')
db.drop_database('planets') # CLEARS DATABASE FOR TESTING

class Planet(Document):
    name = StringField(required=True)
    terrain = StringField(max_length=50, required=True)
    climate = StringField(max_length=50, required=True)
    appearances = ListField(StringField(max_length=50))
    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'id': str(self.id),
            'name': self.name,
            'terrain': self.terrain,
            'climate': self.climate,
            'appearances': self.appearances
        }

tatooine = Planet(name='tatooine', terrain='desert', climate='arid')
tatooine.save()

hoth = Planet(name='hoth', terrain='tundra', climate='cold')
hoth.save()

class PlanetsList(Resource):
    def get(self):
        planets = Planet.objects
        return jsonify(planets=[i.serialize for i in planets]) # gets list of planets
    def post(self):
        name = request.form['name']
        if Planet.objects(name__iexact=name): # check if planet has already been added
            return {'message':'this planet is already in the database'}

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
             return {'message':'error: something went wrong! check your fields.'}
        planets = Planet.objects
        return  {'message':'planet named {} was added successfully'.format(newplanet.name)}
api.add_resource(PlanetsList, '/planets')

if __name__ == '__main__':
    app.run(debug=True)
