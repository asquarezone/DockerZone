FROM amazoncorretto:11-alpine3.17
LABEL author="khaja"
LABEL organization="learningthoughts"
RUN adduser -h /petclinic -s /bin/sh -D petclinic
USER petclinic
WORKDIR /petclinic
ADD --chown=petclinic:petclinic https://referenceapplicationskhaja.s3.us-west-2.amazonaws.com/spring-petclinic-2.4.2.jar /petclinic/spring-petclinic-2.4.2.jar
EXPOSE 8080
CMD ["java", "-jar", "spring-petclinic-2.4.2.jar"]