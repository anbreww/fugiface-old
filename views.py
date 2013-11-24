#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template
from fugidaire import app

from models import Tap, Beer

@app.route('/')
def index():
    beers = [tap.beer for tap in Tap.query.order_by(Tap.position).all()]
    return render_template('index.html', beers=beers)

@app.route('/admin')
def admin():
    beers = [tap.beer for tap in Tap.query.order_by(Tap.position).all()]
    return render_template('admin.html', beers=beers)

@app.route('/debug')
def debug():
    config_strings = [key + " = " + str(value) for key, value in app.config.items()]
    if app.debug:
        return '<br/>'.join(config_strings)
    else:
        return "Sorry, not in debug mode!"

@app.route('/new')
def new_beer():
    '''Create a new beer from a form'''
    return render_template('new.html')
