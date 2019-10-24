FROM python:3
WORKDIR /django_app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y gettext

EXPOSE 8000

CMD ./docker_entrypoint.sh
