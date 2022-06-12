FROM ubuntu:focal
LABEL purpose="classroom" author="khaja"
RUN export DEBIAN_FRONTEND=noninteractive && apt update && apt install apache2 -y 
EXPOSE 80
ADD start.sh /start.sh
ADD index.html /var/www/html/index.html
RUN chmod +x /start.sh
CMD ["/bin/bash", "-c", "/start.sh"]

