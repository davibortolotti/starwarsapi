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

Afterwards, open the folder where you cloned the repo into and execute the seed.py file:
```
python seed.py
```

This will populate the database with a couple of planets to get you started. This phase is actually optional, but it will enable to see some data from start.

Get the API running by executing:
```
python starwars_api.py
```
## How does it work

The API consists of two endpoints only, and dumps information in JSON format.

---
### Listing planets and creating new ones

`localhost:5000/planets` is accessed through `GET` and `POST` methods.


- `GET`

This method shows a list of the planets currently in your database.

Example GET request:
```
curl -X GET 'localhost:5000/planets'
```

**It also accepts a name argument**, that filter the planets through the name you provided. Like this:
```
curl -X GET 'localhost:5000/planets?name=Dagobah'
```

The info displayed is:

`name` - the planet's name.

`climate` - the planet's climate.

`terrain` - the planet's terrain.

`appearances` - the number of movies this planet has made an appearance before. If this is 0, than probably, this planet has never appeared on screen before. Maybe it's new 😉

e.g.:

```
{
   "appearances": 3,
   "climate": "murky",
   "id": "5aca4ca4860c93225004e901",
   "name": "dagobah",
   "terrain": "swamp"
}
```

- `POST`

This method can be used to add a new planet. The arguments **name** (50 characters limit), **climate**(50 characters limit) and **terrain**(50 characters limit) are required.
E.g.:
```
curl -X POST 'localhost:5000/planets?name=Tatooine&terrain=desert&climate=hot'
```
The id is automatically generated (a unique set of characters created by mongoengine), and the appearances attribute is fetched in the SWAPI, if the planet is found in their database through the name attribute you used. Else, it is set to 0.

---

### Searching or deleting a planet through the id

`localhost:5000/planets/<planetid>` is accessible through `GET` and `DELETE` methods. More about them:


- `GET`

Searches the database for a planet with that specific id. The id should replace the <planetid> tag.

Example GET request:
```
curl -X GET 'localhost:5000/planets/5ac7df83860c93248ca37f54'
```
And following response:
```
{
  "appearances": 3,
  "climate": "murky",
  "id": "5ac7df83860c93248ca37f54",
  "name": "dagobah",
  "terrain": "swamp"
}
```

- `DELETE`

Deletes an entry, relative to the id you put in the <planetid> tag, such as:
```
curl -X DELETE 'localhost:5000/planets/5ac7df83860c93248ca37f54'
```

## The end
Thanks for your time.
