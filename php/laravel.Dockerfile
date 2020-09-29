FROM php:7.3-apache
RUN apt-get update && apt-get install -y \
  libfreetype6-dev \
  libjpeg62-turbo-dev \
  libpng-dev \
  libxpm-dev \
  libwebp-dev \
  zip \
 && rm -rf /var/lib/apt/lists/* \
 && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/ --with-webp-dir=/usr/include/ --with-xpm-dir=/usr/include/ \
 && docker-php-ext-configure mysqli --with-mysqli=mysqlnd \
 && docker-php-ext-install -j$(nproc) mysqli gd pdo_mysql bcmath \
 && a2enmod rewrite
COPY --from=composer:1.10 /usr/bin/composer /usr/bin/composer
WORKDIR /var/www/html/hello
COPY --chown=www-data:www-data my-app .
RUN php /usr/bin/composer install
