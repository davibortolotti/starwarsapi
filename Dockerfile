FROM python:3.7.8-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
RUN pip install gunicorn
ENV env=docker


CMD ["gunicorn", "--bind=0.0.0.0:8000", "starwars_api:app"]

EXPOSE 8000