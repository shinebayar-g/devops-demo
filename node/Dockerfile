FROM node:14.9-alpine3.11
WORKDIR /app
RUN chown -R node:node /app
USER node
COPY --chown=node:node my-app/package.json my-app/package-lock.json ./
RUN npm ci --only=production
COPY --chown=node:node my-app .
EXPOSE 3000
ENTRYPOINT [ "npm", "start" ]
