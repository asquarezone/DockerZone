FROM tomcat:9-jdk8
LABEL author="khaja"
LABEL organization="QualityThought"
COPY gameoflife.war /usr/local/tomcat/webapps/gameoflife.war
EXPOSE 8080
# If the Tomcat starts my application starts, so i'm ok with the 
# CMD of the base image, SO i will not write CMD