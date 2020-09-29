#!/bin/bash
echo DB_HOST=$DB_HOST >> /app/.env
echo DB_PORT=$DB_PORT >> /app/.env
echo DB_NAME=$DB_NAME >> /app/.env
echo DB_USER=$DB_USER >> /app/.env
echo DB_PASS=$DB_PASS >> /app/.env

echo SMTP_SERVER=$SMTP_SERVER >> /app/.env
echo SMTP_PORT=$SMTP_PORT >> /app/.env
echo SMTP_USER=$SMTP_USER >> /app/.env
echo SMTP_PASS=$SMTP_PASS >> /app/.env

echo EMAIL_FROM=$EMAIL_FROM >> /app/.env
echo EMAIL_TO=$EMAIL_TO >> /app/.env

echo S3_BUCKET=$S3_BUCKET >> /app/.env
echo S3_PREFIX=$S3_PREFIX >> /app/.env

echo AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID >> /app/.env
echo AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY >> /app/.env

exec "$@"