FROM openjdk:8u272-slim
LABEL author="khaja"
ADD https://referenceappkhaja.s3-us-west-2.amazonaws.com/spring-petclinic-2.2.0.BUILD-SNAPSHOT.jar ./spring-petclinic.jar
COPY instructions.txt ./instructions.txt
EXPOSE 8080/tcp
CMD ["java","-jar", "spring-petclinic.jar"]
