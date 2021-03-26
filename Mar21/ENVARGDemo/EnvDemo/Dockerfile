FROM openjdk:8
# base image is openjdk
LABEL author="khaja ibrahim"
LABEL maintainer="qtdevops@gmail.com"
ENV applicationpath='/springpetclinic.jar'
ENV dummy='dummy'
ARG downloadlocation
# Downloading the image from the url
ADD  ${downloadlocation} ${applicationpath}
# spring pet clinic runs on port 8080
EXPOSE 8080
# command to start the application
CMD ["java",  "-jar",  ${applicationpath} ]