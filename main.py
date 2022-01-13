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
              rank=10, tags='Tardar Sauce, Tabatha Bundesen, Felis domesticus', topText=' ')

meme2 = Memes(bottomText='Winter is Coming', image='https://imgflip.com/s/meme/Brace-Yourselves-X-is-Coming.jpg', name='Brace Yourselves',
              rank=20, tags='Winter is Coming, Ned Stark, Sean Bean, Game of Thrones, GOT, Imminent Ned', topText='Brace Yourselves')

meme3 = Memes(bottomText='Or just ___', image='https://imgflip.com/s/meme/Futurama-Fry.jpg', name='Futurama Fry',
              rank=30, tags='Not Sure If', topText='Not sure if ___')


meme1.save()
meme2.save()
meme3.save()


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


@app.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return jsonify({"message": "Hello GET"})
    else:
        return jsonify({"message": "Hello, world!"})


app.run(port=9000, debug=True)
