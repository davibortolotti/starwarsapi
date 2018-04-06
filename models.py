from mongoengine import *

### models

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