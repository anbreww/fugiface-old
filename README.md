# Fûgiface

Fûgiface is a web interface to display which beers are currently on tap on the Fûgidaire.

quick overview (quickstart for when I need to install dependencies)

* Flask for the web server
* Bootstrap for the css
* Elixir for the database (SQLAlchemy)
* Everything running in a venv
* uwsgi to run the app through nginx
* supervisor to monitor the uswgi app and keep it running
* puppet to setup the server(s)
* fabric to package and deploy the app (pip freeze > requirements.txt also)

Run a full test server in a vm or raspberry pi to act as a VPS

  $ . venv/bin/activate # launch virtual environment

# Quick setup guide

## Create virtual environment

    sudo apt-get install python-virtualenv
    cd /home/andrew/webapps/fugidaire
    virtualenv venv

## Install uwsgi and other packages

From a normal shell 

    sudo apt-get install python-dev libevent-dev

From the virtual environment

    . venv/bin/activate
    pip install uwsgi

    pip install -r requirements.txt

## Configure nginx to forward requests to uwsgi

Add the following lines to /etc/nginx/sites-available/fugidaire

    location / { try_files $uri @fugidaire; }

    location @fugidaire {
      include uwsgi_params;
      uwsgi_pass unix:/tmp/uwsgi.sock;
    }

Restart nginx

    service nginx restart

Then start uwsgi in the venv

    uwsgi -s /tmp/uwsgi.sock -w fugidaire:app -H /path/to/the/fugidaire/venv --chmod-socket=666

The app should be working temporarily (now we'll add supervisor to keep it runing)



## Add supervisor to keep it running

    sudo apt-get install supervisor

Then create a new config file for the app

    sudo vim /etc/supervisor/conf.d/fugidaire.conf

With the following contents

    [program:fugidaire]
    command=/home/andrew/webapps/fugidaire/venv/bin/uwsgi -s /tmp/uwsgi.sock -w fugidaire:app -H /home/andrew/webapps/fugidaire/venv --chmod-socket=666
    directory=/home/andrew/webapps/fugidaire
    autostart=true
    autorestart=true
    stdout_logfile=/home/andrew/webapps/fugidaire/logs/uwsgi.log
    redirect_stderr=true
    stopsignal=QUIT

Make sure to create the folder for the log file before launching supervisord

    mkdir /home/andrew/webapps/fugidaire/logs

Then restart supervisord

    ps -A | grep supervisor
    kill <id>
    sudo supervisord -c /etc/supervisor/supervisord.conf

Source for uwsgi/supervisor/nginx : http://flaviusim.com/blog/Deploying-Flask-with-nginx-uWSGI-and-Supervisor/


