# Assuming your CI platform will install dependencies, run tests and build artifacts.
FROM nginx:1.18-alpine
# overriding nginx default config
COPY nginx.conf /etc/nginx/conf.d/default.conf
# copying build artifact from ci runner workspace
COPY build /usr/share/nginx/html/
