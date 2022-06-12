FROM ubuntu:focal
LABEL purpose="classroom" author="khaja"
RUN export DEBIAN_FRONTEND=noninteractive && apt update && apt install apache2 -y 
EXPOSE 80
ADD start.sh /start.sh
ADD https://qtkhajavideos2.s3.us-west-2.amazonaws.com/fun.html /var/www/html/index.html
RUN chmod +x /start.sh
CMD ["/bin/bash", "-c", "/start.sh"]

