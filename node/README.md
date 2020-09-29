# Express app generator

```
npx express-generator
```

# Build & Run docker image for your nodejs express app

```
docker build -t node:0.0.1 -f Dockerfile --force-rm .
docker run -d -p 3000:3000 --name node node:0.0.1
docker rm -f node
```

Visit: `http://localhost:3000`