from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from mongoengine import *

app = Flask(__name__)
api = Api(app)

db = connect('planets')
db.drop_database('planets') # CLEARS DATABASE FOR TESTING

class Planet(Document):
    name = StringField(required=True)
    terrain = StringField(max_length=50, required=True)
    climate = StringField(max_length=50, required=True)
    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'id': str(self.id),
            'name': self.name,
            'terrain': self.terrain,
            'climate': self.climate,
        }

tatooine = Planet(name='tatooine', terrain='desert', climate='arid')
tatooine.save()

hoth = Planet(name='hoth', terrain='tundra', climate='cold')
hoth.save()

class PlanetsList(Resource):
    def get(self):
        planets = Planet.objects
        return jsonify(planets=[i.serialize for i in planets]) # gets list of planets
api.add_resource(PlanetsList, '/planets')

if __name__ == '__main__':
    app.run(debug=True)
