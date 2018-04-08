from mongoengine import *
import requests

### models

class Planet(Document):
    name = StringField(max_length=50, required=True)
    terrain = StringField(max_length=50, required=True)
    climate = StringField(smax_length=50, required=True)
    appearances = IntField()

    def getAppearances(self): #  SEARCH SWAPI FOR FILM APPEARANCES
        r = requests.get('https://swapi.co/api/planets/?search={}'.format(self.name))
        json_result = r.json()

        if json_result['count'] > 0:
            films = json_result['results'][0]['films']
            self.appearances = len(films)
        else:
            self.appearances = 0

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
