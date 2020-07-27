from mongoengine import *
import requests

from schemas import PlanetSchema

class Planet(Document):

    schema = PlanetSchema
    name = StringField(max_length=50, required=True)
    terrain = StringField(max_length=50, required=True)
    climate = StringField(smax_length=50, required=True)
    appearances = IntField()

    def get_appearances(self):  
        """Searches SWAPI to check number of appearances of planet in movies"""
        r = requests.get(f'https://swapi.dev/api/planets?search={self.name}')
        json_result = r.json()

        if json_result['count'] > 0:
            films = json_result['results'][0]['films']
            self.appearances = len(films)
        else:
            self.appearances = 0

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return self.schema().dump(self)
