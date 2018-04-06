# Star Wars Planet API
Welcome to the Star Wars Planet API!

This API was made using Python, Flask, MongoDB and with the help of [The Star Wars API](https://swapi.co/ "The Star Wars API"), by Paul Hallett.

With this API you will be able to access a MongoDB database installed in your server, add planets, search, delete and list them.

## Dependencies
In order to use this, you must have some things installed in your machine.  Bear with me:

1. Python 3 - Install it from [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. MongoDB - Get it from [https://www.mongodb.com/download-center#community](https://www.mongodb.com/download-center#community)

3. Flask -  If you don't have pip installed (you do if you just got the latest versions of python), you should get it [here](https://pip.pypa.io/en/stable/installing/ "here"). Then, after it is ready, just type into a prompt:
`pip install flask`
4. Flask_restful module - Same goes here:
`pip install flask_restful`
5. mongoengine module - And again:
`pip install mongoengine`
6. requests module - And at last:
`pip install requests`

All set! Damn, that was easy.

## Up and running

The API is really easy to set up. First you should clone this repo into your machine.

Then, open a terminal and get your MongoDB instance running by typing into it:
`mongod`

Afterwards, open the folder where you clone the repo into and execute the examples.py file:
`python examples.py`

This will populate the database with a couple of planets to get you started. This phase is actually optional, but it will enable to see some data from start.

Get the API running by executing:
`python starwars_api.py`
## How does it work

The API consists of two endpoints only.

`localhost:5000/planetlist` accepts no query options, and is accessed only with a `GET` method. This endpoint show a list of the planets currently in your database, with all the info that is associated with them. What are they?

`name` - the planet's name.
`climate` - the planet's climate.
`terrain` - the planet's terrain.
`appearance` - a list of movies this planet has made an appearance before. If this is an empty list, than this probably this planet has never appeared on the screen before. Maybe it's new

The other endpoint is:

`localhost:5000/planets` and is accessible through `GET`, `POST` and `DELETE` methods. More about them:

`GET` searches the database for a planet with that specific name or respective id.  Requires **name** or **id** attributes.

Example GET response:
>     {
      "appearances": [
        "The Empire Strikes Back",
        "Revenge of the Sith",
        "Return of the Jedi"
      ],
      "climate": "murky",
      "id": "5ac7df83860c93248ca37f54",
      "name": "dagobah",
      "terrain": "swamp"
    }

`POST` adds a new entry to the planets database. It requires **name**, **terrain** and **climate** attributes. What it also does is search in the swapi for the appearances this planet has made in the franchise's movies. If it receives none, no sweat, it returns an empty list and adds it to the planet's properties.

`DELETE` deletes an entry, simple as that. Requires **name** or **id** attributes.

## The end
Thanks for your time.
