FROM openjdk:8
# base image is openjdk
LABEL author="khaja ibrahim"
LABEL maintainer="qtdevops@gmail.com"
# Downloading the image from the url
ADD https://referenceappkhaja.s3-us-west-2.amazonaws.com/spring-petclinic-2.2.0.BUILD-SNAPSHOT.jar /spring-petclinic.jar
# spring pet clinic runs on port 8080
EXPOSE 8080
# command to start the application
CMD ["java",  "-jar",  "/spring-petclinic.jar"]