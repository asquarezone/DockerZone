FROM eclipse-temurin:17
LABEL project="learning" 
LABEL author="khaja"
RUN useradd -m -d /apps -s /bin/bash spc
USER spc
ADD --chown=spc:spc https://referenceappslt.s3.ap-south-1.amazonaws.com/spring-petclinic-3.3.0-SNAPSHOT.jar /apps/spring-petclinic-3.3.0-SNAPSHOT.jar
EXPOSE 8080
# CMD Executes when the container is started
CMD [ "java", "-jar", "/apps/spring-petclinic-3.3.0-SNAPSHOT.jar" ]