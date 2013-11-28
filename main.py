from fugidaire import app, db, manager

from models import *
from views import *

manager.create_api(Beer, methods=['GET', 'POST', 'DELETE'],
        url_prefix='/api/v1', collection_name='beers')
manager.create_api(Tap, methods=['GET'], url_prefix='/api/v1',
        collection_name='taps')

if __name__ == '__main__':
    app.debug = True
    app.run(host='::', port=9999)

