#!/bin/bash

source ../env/bin/activate

while getopts ursmM opt; do
  case $opt in
    r)
      python manage.py runserver;
      ;;
    u)
      python manage.py createsuperuser;
      ;;
    s)
      python manage.py collectstatic --clear --noinput --link;
      ;;
    m)
      python manage.py makemigrations $OPTARG;
      ;;
    M)
      python manage.py migrate $OPTARG;
      ;;
  esac
done
