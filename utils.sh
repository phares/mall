#!/bin/bash

source ../env/bin/activate

# Fork django oscar app
if [ $# -eq 1 ] && [ -d "myapps/" ]
then
  python manage.py oscar_fork_app $1 myapps/
elif [$# -eq 2 ]
then
  python manage.py oscar_fork_app $1 "$2/"
else
  echo "Usage:
               (1)  ./utils.sh <APP_NAME>
               (2)  ./utils.sh <APP_NAME> <APPS_FOLDER>"
fi
