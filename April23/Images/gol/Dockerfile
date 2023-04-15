FROM tomcat:9-jdk8
LABEL author="khaja" organization="qt"
ARG GOL_URL=https://referenceapplicationskhaja.s3.us-west-2.amazonaws.com/gameoflife.war
ADD ${GOL_URL} /usr/local/tomcat/webapps/gameoflife.war
VOLUME "/usr/local/tomcat"
EXPOSE 8080
# IGNORING CMD as i want base image's CMD