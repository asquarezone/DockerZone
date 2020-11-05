FROM openjdk:8
LABEL author="shaik khaja ibrahim"
LABEL org="Learning Thoughts"
# Adding an argument with default value
# This value can be changed by passing 
# docker image build --build-arg download_location="<newlocation>" ....
ARG download_location='https://referenceappkhaja.s3-us-west-2.amazonaws.com/spring-petclinic-2.2.0.BUILD-SNAPSHOT.jar'
ENV FILE_LOCATION='spring-petclinic.jar'
ADD  ${download_location} ${FILE_LOCATION}
EXPOSE 8080
CMD java -jar ${FILE_LOCATION}
