docker run --rm -p 8080:8000 --name dev -v %cd%:/django_app mysite django-admin makemessages -l %*
