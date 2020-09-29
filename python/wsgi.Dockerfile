FROM python:3.8-slim
WORKDIR /app
COPY my-app .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app" ]
