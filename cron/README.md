# Build & Run docker image for your cron service

This container runs cron script that does mysqldump, archive, upload to s3, send error/success email to administrator depends on the result.

```
docker build -t cron:0.0.1 -f Dockerfile --force-rm .
docker run -d --name cron cron:0.0.1
docker logs -f cron
docker rm -f cron
```

Container expects following environment variables:

MySQL settings:

```
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASS
```

SMTP settings:

```
SMTP_SERVER
SMTP_PORT
SMTP_USER
SMTP_PASS
```

Email settings:

```
EMAIL_FROM
EMAIL_TO
```

AWS S3 settings:

```
S3_BUCKET
S3_PREFIX
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
```

**Note**: `docker-entrypoint.sh` script populates environment variables to file.
Because docker passed environment variables are set for only `PID 1` and crontab shell (new process) doesn't know about it.
To work around this issue, we're saving envs to a file and sourcing it before running actual cron entry.
