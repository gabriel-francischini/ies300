#!/bin/bash
uwsgi --chdir=/media/superwolf/2230B90F30B8EAC5/dev/projects/py/ies300/webapp_ies300 \
      --module=webapp_ies300.wsgi:application \
      --env DJANGO_SETTINGS_MODULE=webapp_ies300.settings \
      --master --pidfile=/tmp/ies300-master.pid \
      --socket=127.0.0.1:49152        \
      --processes=5                   \
      --uid=1000           \
      --harakiri=20                   \
      --max-requests=5000             \
      --vacuum                        \
      --home=/home/superwolf/miniconda3      \
#      --daemonize=/var/log/uwsgi/ies300.log      \
