import json

from operator import mod
from statistics import mode
from flask import Flask
from flask import request
from flask import jsonify

from peewee import *
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase('memes', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Memes(BaseModel):
    bottomText = CharField()
    image = CharField()
    name = CharField()
    rank = IntegerField()
    tags = CharField()
    topText = CharField()


db.connect()
db.drop_tables([Memes])
db.create_tables([Memes])


meme1 = Memes(bottomText='Good!', image='http://imgflip.com/s/meme/Grumpy-Cat.jpg', name='Grumpy Cat',
              rank=10, tags='Tardar Sauce, Tabatha Bundesen, Felis domesticus', topText=' ').save()

meme2 = Memes(bottomText='Winter is Coming', image='https://imgflip.com/s/meme/Brace-Yourselves-X-is-Coming.jpg', name='Brace Yourselves',
              rank=20, tags='Winter is Coming, Ned Stark, Sean Bean, Game of Thrones, GOT, Imminent Ned', topText='Brace Yourselves').save()

meme3 = Memes(bottomText='Or just ___', image='https://imgflip.com/s/meme/Futurama-Fry.jpg', name='Futurama Fry',
              rank=30, tags='Not Sure If', topText='Not sure if ___').save()

meme4 = Memes(bottomText='Walk into mordor', image='https://imgflip.com/s/meme/One-Does-Not-Simply.jpg', name='One Does Not Simply',
              rank=40, tags='One Does Not Simply Walk Into Mordor, Boromir, Sean Bean, Ned Stark, LOTR, Lord of the rings, One Ring', topText='One does not simply').save()

meme5 = Memes(bottomText='Who ___', image='https://imgflip.com/s/meme/Am-I-The-Only-One-Around-Here.jpg', name='Am I The Only One Around Here',
              rank=70, tags='Dude Abides, Big Lebowski, Angry Walter Sobchak', topText='Am I the only one around here').save()

meme6 = Memes(bottomText='Success!', image='https://imgflip.com/s/meme/Success-Kid.jpg',
              name='Success Kid', rank=80, tags='I hate sandcastles, eating sand', topText=' ').save()

meme7 = Memes(bottomText='But when I do ___', image='https://imgflip.com/s/meme/The-Most-Interesting-Man-In-The-World.jpg',
              name='The Most Interesting Man in the World', rank=160, tags='Jonathan Goldsmith', topText="I don't always ___").save()

meme8 = Memes(bottomText='Everywhere', image='https://imgflip.com/s/meme/X-Everywhere.jpg',
              name='X, X Everywhere', rank=170, tags='Toy story, Buzz lightyear, Woody', topText='___, ___').save()

meme9 = Memes(bottomText="That'd be great", image='https://imgflip.com/s/meme/That-Would-Be-Great.jpg',
              name='That would be great', rank=180, tags='Bill Lumbergh, Office Space', topText='Yeah, If you could just ___').save()

meme10 = Memes(bottomText='Show Me What You Got', image='http://i.imgur.com/6Ln3hp8.png',
               name='Show Me What You Got', rank=188, tags='Rick and Morty, Giant Heads, Dan, Justin, Adult Swim', topText=' ').save()

meme11 = Memes(bottomText='Show Me What You Got', image='http://i.imgur.com/6Ln3hp8.png',
               name='Show Me What You Got', rank=188, tags='Rick and Morty, Giant Heads, Dan, Justin, Adult Swim', topText=' ').save()


app = Flask(__name__)


@app.route('/meme', methods=['GET'])
@app.route('/meme/<id>', methods=['GET'])
def meme(id=None):
    if id:
        meme = Memes.get(Memes.id == id)
        meme = model_to_dict(meme)
        return jsonify(meme)
    else:
        memes = []
        for meme in Memes.select():
            memes.append(model_to_dict(meme))
        return jsonify(memes)


@app.route('/meme/bottomText/<bottomText>', methods=['GET'])
def btmText(bottomText=None):
    if bottomText:
        meme = Memes.get(Memes.bottomText == bottomText)
        meme = model_to_dict(meme)
        return jsonify(meme)
    else:
        memes = []
        for meme in Memes.select():
            memes.append(model_to_dict(meme))
        return jsonify(memes)


@app.route('/meme/name/<name>', methods=['GET'])
def name(name=None):
    if name:
        meme = Memes.get(Memes.name == name)
        meme = model_to_dict(meme)
        return jsonify(meme)
    else:
        memes = []
        for meme in Memes.select():
            memes.append(model_to_dict(meme))
        return jsonify(memes)


@app.route('/meme/rank/<rank>', methods=['GET'])
def rank(rank=None):
    if rank:
        meme = Memes.get(Memes.rank == rank)
        meme = model_to_dict(meme)
        return jsonify(meme)
    else:
        memes = []
        for meme in Memes.select():
            memes.append(model_to_dict(meme))
        return jsonify(memes)


@app.route('/meme/tags/<tags>', methods=['GET'])
def tags(tags=None):
    if rank:
        meme = Memes.get(Memes.tags == tags)
        meme = model_to_dict(meme)
        return jsonify(meme)
    else:
        memes = []
        for meme in Memes.select():
            memes.append(model_to_dict(meme))
        return jsonify(memes)


@app.route('/meme/topText/<topText>', methods=['GET'])
def topText(topText=None):
    if rank:
        meme = Memes.get(Memes.topText == topText)
        meme = model_to_dict(meme)
        return jsonify(meme)
    else:
        memes = []
        for meme in Memes.select():
            memes.append(model_to_dict(meme))
        return jsonify(memes)


@app.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return jsonify({"message": "Hello GET"})
    else:
        return jsonify({"message": "Hello, world!"})


app.run(port=9000, debug=True)
