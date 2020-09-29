FROM node:14.9-alpine3.11
WORKDIR /app
COPY my-app/package.json my-app/yarn.lock ./
RUN yarn install --production --frozen-lockfile
COPY my-app .
RUN npm run build

FROM nginx:1.18-alpine
# overriding nginx default config
COPY nginx.conf /etc/nginx/conf.d/default.conf
# copying build artifact from multi stage build container
COPY --from=0 /app/build /usr/share/nginx/html/
EXPOSE 8080