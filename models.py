from mongoengine import *

### models

class Planet(Document):
    name = StringField(max_length=50, required=True)
    terrain = StringField(max_length=50, required=True)
    climate = StringField(max_length=50, required=True)
    appearances = IntField()
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
