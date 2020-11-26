#!/bin/sh

if [ "${WAIT_DB}" = 1 ]; then
  echo "Waiting for mongo..."

  while ! nc -z mongo 27017; do
    sleep 0.1
  done

  sleep 1

  echo "MongoDB started"
fi;

if [ "${FLASK_ENV}" = "development" ]; then
  flask run --host=0.0.0.0 --port=${PORT}
else
  gunicorn --bind=0.0.0.0:${PORT} --workers=4 app:app
fi;