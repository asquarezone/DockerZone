FROM eclipse-temurin:17
LABEL project="learning" 
LABEL author="khaja"
ADD https://referenceappslt.s3.ap-south-1.amazonaws.com/spring-petclinic-3.3.0-SNAPSHOT.jar /spring-petclinic-3.3.0-SNAPSHOT.jar
EXPOSE 8080
# CMD Executes when the container is started
CMD [ "java", "-jar", "/spring-petclinic-3.3.0-SNAPSHOT.jar" ]