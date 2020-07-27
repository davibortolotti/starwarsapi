import os

from mongoengine import *
from models import Planet

def seed():
    if os.getenv('env') == "docker":
        db = connect('planets', host="mongo")
    else:
        db = connect('planets')

    db.drop_database('planets')  # CLEARS DATABASE FOR TESTING

    # POPULATING DATA WITH EXAMPLES

    tatooine = Planet(name='dagobah', terrain='swamp', climate='murky',
        appearances=3)
    tatooine.save()

    hoth = Planet(name='hoth', terrain='tundra', climate='cold',
        appearances=1)
    hoth.save()

    print('examples added to the database')


if __name__ == '__main__':
    seed()

