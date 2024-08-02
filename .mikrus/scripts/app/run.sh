#!/bin/sh

set -e

python ./geo_doc_generator/manage.py makemigrations
python ./geo_doc_generator/manage.py migrate
python ./geo_doc_generator/manage.py initadmin
python ./geo_doc_generator/manage.py collectstatic --noinput
cd ./geo_doc_generator && gunicorn -b 0.0.0.0:8000 geo_doc_generator.wsgi:application --access-logfile /var/log/gunicorn/access.log --error-logfile /var/log/gunicorn/error.log
