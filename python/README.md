# Python web app

## Build & Run docker image for your python flask app

```
docker build -t flask:0.0.1 -f flask.Dockerfile --force-rm .
docker run -d -p 5000:5000 --name flask python:0.0.1
docker rm -f flask
```

## Build & Run docker image for your python flask app with Gunicorn wsgi server

```
docker build -t wsgi:0.0.1 -f wsgi.Dockerfile --force-rm .
docker run -d -p 5000:5000 --name wsgi wsgi:0.0.1
docker rm -f wsgi
```

Visit: `http://localhost:5000`