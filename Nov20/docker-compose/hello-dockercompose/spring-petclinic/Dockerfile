FROM openjdk:8
LABEL author="shaik khaja ibrahim"
LABEL org="Learning Thoughts"
RUN wget https://referenceappkhaja.s3-us-west-2.amazonaws.com/spring-petclinic-2.2.0.BUILD-SNAPSHOT.jar
EXPOSE 8080
CMD [ "java", "-jar", "spring-petclinic-2.2.0.BUILD-SNAPSHOT.jar" ]
