# take amazon correto 17 as a base image
FROM amazoncorretto:17
# add metadata
LABEL author="shaikkhajaibrahim"
LABEL project="lt-learning"
# Download_url with a default value
ARG DOWNLOAD_URL="https://www.learningthoughts.io/spring-petclinic-3.2.0-SNAPSHOT.jar"
# download spring petclinic
RUN curl -O ${DOWNLOAD_URL}
# expose 8080 port as spring petclinic needs 8080
EXPOSE 8080
# command to start the application
CMD ["java", "-jar", "spring-petclinic-3.2.0-SNAPSHOT.jar"]
