FROM ubuntu:bionic
LABEL author='khaja'
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt update && apt install apache2 -y \
    && apt install php libapache2-mod-php php-mysql -y \
    && apt install php-cli -y
COPY info.php /var/www/html/info.php
WORKDIR /var/www/html
EXPOSE 80
ENTRYPOINT [ "echo" ]
CMD [ "helloworld" ]
