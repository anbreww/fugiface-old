#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    beerlist = [
            ("Zombie Dust", "Double IPA", "6.0", "120",
        "Powerfully hopped double IPA with loads of citrusy Citra hops."),
            ("Centennial Water", "American Blonde", "4.0", "30",
        "A very light and refreshing blonde, with a touch of Centennial hops."),
            ("Bacon Juice", "Smoked Ale", "5.2", "20",
        "Slightly hazy ale that smells and tastes like liquid bacon."),
            ("OctoberAle", "Oktoberfest Ale", "6.5", "40",
        "An oktoberfest recipe fermented with an ale yeast"),
            ("Anbrew ESB", "Scottish ESB", "4.7", "25",
        "Clean and dry, this British-style bitter is <i>extra special</i>"),
            ]
    beers = [dict(name=beer[0], type=beer[1], abv=beer[2],
        ibu=beer[3], description=beer[4]) for beer in
        beerlist]
    return render_template('index.html', beers=beers)

@app.route('/about')
def about():
    return '<h2>Fûgidaire interface, by Andrew Watson 2013</h2>'

if __name__ == '__main__':
    app.debug = True
    app.run(host='::')

