from mongoengine import *
from models import Planet

db = connect('planets')
db.drop_database('planets') # CLEARS DATABASE FOR TESTING

### POPULATING DATA WITH EXAMPLES

tatooine = Planet(name='dagobah', terrain='swamp', climate='murky',
    appearances=['The Empire Strikes Back', 'Revenge of the Sith', 'Return of the Jedi'])
tatooine.save()

hoth = Planet(name='hoth', terrain='tundra', climate='cold',
    appearances=['The Empire Strikes Back'])
hoth.save()

print('examples added to the database')
