#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

from datetime import date, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    style = db.Column(db.String(80))
    description = db.Column(db.String(250))
    abv = db.Column(db.Float)
    ibu = db.Column(db.Integer)
    volume = db.Column(db.Float)    # keg volume in litres
    date_brewed = db.Column(db.Date)
    date_tapped = db.Column(db.Date)
    date_retired = db.Column(db.Date)


    def __init__(self, name, style="Pale Ale", description="The newest beer",
            abv=5.0, ibu=20, volume=19.5, date_brewed=None, date_tapped=None,
            date_retired=None):
        self.name = name
        self.style = style
        self.description = description
        self.abv = abv
        self.ibu = ibu
        self.volume = volume
        self.date_brewed=date_brewed
        self.date_tapped=date_tapped
        self.date_retired=date_retired

    def __repr__(self):
        return '<Beer %r>' % self.name

class Tap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(80))

    # define a one-to-one relationship between beer and tap
    beer_id = db.Column(db.Integer, db.ForeignKey('beer.id'))
    beer = db.relationship('Beer', backref=db.backref('tap', uselist=False))

    def __init__(self, position, beer, name="1"):
        self.position = position
        self.beer = beer
        self.name = name

    def __repr__(self):
        return '<Tap %r>' % self.position

@app.route('/')
def index():
    beers = Beer.query.all() # TODO : only get beers that are on tap!
    return render_template('index.html', beers=beers)

@app.route('/about')
def about():
    return '<h2>Fûgidaire interface, by Andrew Watson 2013</h2>'

if __name__ == '__main__':
    app.debug = True
    app.run(host='::')

