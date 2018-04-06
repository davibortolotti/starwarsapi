# Star Wars Planet API
Welcome to the Star Wars Planet API!

This API was made using Python, Flask, MongoDB and with the help of [The Star Wars API](https://swapi.co/ "The Star Wars API"), by Paul Hallett.

With this API you will be able to access a MongoDB database installed in your server, add planets, search, delete and list them.

## Dependencies
In order to use this, you must have some things installed in your machine.  Bear with me:

1. Python 3 - Install it from [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. MongoDB - Get it from [https://www.mongodb.com/download-center#community](https://www.mongodb.com/download-center#community)

3. Pip -  If you don't have pip installed (you do if you've got the latest versions of python), you should get it [here](https://pip.pypa.io/en/stable/installing/ "here"). Then, after it is ready, just type into a prompt, inside the folder you cloned:
```
pip install -r requirements.txt
```

All set! Damn, that was easy.

## Up and running

The API is really easy to set up. First you should clone this repo into your machine.

Then, open a terminal and get your MongoDB instance running by typing into it:
```
mongod
```

Afterwards, open the folder where you cloned the repo into and execute the examples.py file:
```
python examples.py
```

This will populate the database with a couple of planets to get you started. This phase is actually optional, but it will enable to see some data from start.

Get the API running by executing:
```
python starwars_api.py
```
## How does it work

The API consists of two endpoints only.

`localhost:5000/planets` accepts no query options, and is accessed through `GET` and `POST` methods. This endpoint show a list of the planets currently in your database, with all the info that is associated with them. What are they?

`name` - the planet's name.

`climate` - the planet's climate.

`terrain` - the planet's terrain.

`appearance` - a list of movies this planet has made an appearance before. If this is an empty list, than probably, this planet has never appeared on screen before. Maybe it's new 😉

You can use a `POST` method to add a new planet. The arguments **name**, **climate** and **terrain** are required. E.g.:
```
curl -X POST 'localhost:5000/planets' -d 'name=Dagobah&terrain=swamp&climate=murky'
```
The id is automatically generated, and the appearance attribute is fetched from the SWAPI, if the planet is found in their database through the name attribute you used.



The other endpoint is:

`localhost:5000/planets/<planetid>` and is accessible through `GET` and `DELETE` methods. More about them:

`GET` searches the database for a planet with that specific id. The id should replace the <planetid> tag.

Example GET request:
```
curl -X GET 'localhost:5000/planets/5ac7df83860c93248ca37f54'
```
And following response:
```
{
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
```

`DELETE` deletes an entry, relative to the id you put in the <planetid> tag, such as:
```
curl -X DELETE localhost:5000/5ac7df83860c93248ca37f54
```

## The end
Thanks for your time.
