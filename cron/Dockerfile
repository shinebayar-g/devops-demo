FROM python:3.7.7-slim-stretch
WORKDIR /app
RUN apt-get update \
 && apt-get install --no-install-recommends -yq cron mysql-client \
 && rm -rf /var/lib/apt/lists/*
COPY src docker-entrypoint.sh ./
RUN pip install -r requirements.txt \
 && mv crontab /etc/cron.d/backup-crontab \
 && chmod 0644 /etc/cron.d/backup-crontab \
 && /usr/bin/crontab /etc/cron.d/backup-crontab
ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["cron", "-f"]