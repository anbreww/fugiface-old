#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

from datetime import date, datetime

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('default_settings')
app.config.from_pyfile('application.cfg', silent=True)

db = SQLAlchemy(app)

manager = APIManager(app, flask_sqlalchemy_db=db)
