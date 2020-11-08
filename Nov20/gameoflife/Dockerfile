FROM tomcat:jdk8-openjdk
LABEL team="qtdevops"
RUN cd webapps/ && wget https://referenceappkhaja.s3-us-west-2.amazonaws.com/gameoflife.war
VOLUME /usr/local/tomcat
EXPOSE 8080