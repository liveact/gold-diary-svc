FROM python:3.8.10-slim-buster
ENV PYTHONUNBUFFERED=True
ENV PYTHONIOENCODING=UTF-8
RUN apt-get -y update && apt-get -y install supervisor gcc libmariadb-dev procps vim
RUN pip install --upgrade pip
ADD . /opt/gold-diary-svc
WORKDIR /opt/gold-diary-svc
RUN pip install -r requirements/prod.txt
RUN python manage.py collectstatic --settings=gold_diary_svc.settings.prod
COPY gunicorn /etc/default/gunicorn
COPY supervisor.conf /etc/supervisor/conf.d/app.conf
EXPOSE 8000
CMD  ["/usr/bin/supervisord"]
