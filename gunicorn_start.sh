#!/bin/bash

#/home/pi/cadmin-esp/cadmin-esp

NAME="cadmin"                              #Name of the application (*)
DJANGODIR=/home/pi/cadmin-esp/cadmin-esp             # Django project directory (*)
SOCKFILE=/home/pi/cadmin-esp/cadmin-esp/gunicorn.sock        # we will communicate using this unix socket (*)
USER=pi                                        # the user to run as (*)
GROUP=pi                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=cadmin_site.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=cadmin_site.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/pi/cadmin-esp/cadmin-esp/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/pi/cadmin-esp/cadmin-esp/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE

