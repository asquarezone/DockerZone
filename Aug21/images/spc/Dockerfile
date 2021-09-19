FROM openjdk:11-slim
LABEL author="khaja ibrahim"
LABEL organization="quality thought"
ARG DOWNLOAD_URL
ENV APPLICATION_PATH="/spring-petclinic.jar"
ENV TEST_ENV="hello"
ADD ${DOWNLOAD_URL} ${APPLICATION_PATH}
EXPOSE 8080
CMD [ "java", "-jar", ${APPLICATION_PATH} ]
