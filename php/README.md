# PHP Laravel web app

Laravel app created by running:

```
docker run -it -v `pwd`:/var/www/html laravel:0.0.1 composer create-project --prefer-dist laravel/laravel my-app
```

# Build & Run docker image for your php laravel app

```
docker build -t laravel:0.0.1 -f laravel.Dockerfile --force-rm .
docker run -d -p 8080:80 --name laravel laravel:0.0.1
docker rm -f laravel
```

Visit: `http://localhost:8080/hello/public/`