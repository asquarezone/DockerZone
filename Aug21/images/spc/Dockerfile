FROM openjdk:11-slim
LABEL author="khaja ibrahim"
LABEL organization="quality thought"
ARG DOWNLOAD_URL
ADD ${DOWNLOAD_URL} /spring-petclinic.jar
EXPOSE 8080
CMD [ "java", "-jar", "/spring-petclinic.jar" ]
