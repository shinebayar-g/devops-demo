# Create react app

```
npx create-react-app my-app
```

# Build & Run docker image for your create react app

```
DOCKER_BUILDKIT=1 docker build -t cra:0.0.1 -f multistage.Dockerfile --force-rm .
docker run -d -p 8080:80 --name cra cra:0.0.1
docker rm -f cra
```

`DOCKER_BUILDKIT=1` allows to use multiple dockerignore files.

Visit: `http://localhost:8080`