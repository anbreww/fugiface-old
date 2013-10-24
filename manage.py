from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from fugidaire import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from datetime import date, timedelta

@manager.command
def dummy(operation):
    '''Create dummy data to fill taps'''
    if operation == 'create':
        print "Generating dummy data to fill our taps"
        from fugidaire import Beer, Tap
        beers = [
                Beer("Zombie Dust", style="Double IPA", abv=6.0, ibu=120,
                    description="Powerfully hopped double IPA with loads of citrusy Citra hops.", volume=19),
                Beer("Centennial Water", style="American Blonde", abv=4.0,
                    ibu=30, description="A very light and refreshing blonde, with a touch of Centennial hops.", volume=18.5),
                Beer("Bacon Juice", style="Smoked Ale", abv=5.2, ibu=20,
                    description="Slightly hazy ale that smells and tastes like liquid bacon.", volume=19.2),
                Beer("OctoberAle", style="Oktoberfest Ale", abv=6.5, ibu=40,
                    description="An oktoberfest recipe fermented with an ale yeast", volume=19.0),
                Beer("Anbrew ESB", style="Scottish ESB", abv=4.7, ibu=25,
                    description="Clean and dry, this British-style bitter is <i>extra special</i>", volume=17.0)
                ]
        taps = [
                Tap(1, beers[0], "1"),
                Tap(2, beers[1], "2"),
                Tap(3, beers[2], "3"),
                Tap(4, beers[3], "4"),
                Tap(5, beers[4], "5")
                ]

        for beer in beers:
            beer.date_brewed=date.today() - timedelta(1) # yesterday
            beer.date_tapped=date.today()
            db.session.add(beer)

        for tap in taps:
            db.session.add(tap)

        db.session.commit()

    elif operation == 'destroy':
        if prompt_bool("Do you really want to clear the database"):
            db.drop_all()

    else:
        print "Unkown operation (try 'create' or 'destroy')"

if __name__ == '__main__':
    manager.run()
