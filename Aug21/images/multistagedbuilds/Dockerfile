FROM maven:3-openjdk-11 AS builder
RUN git clone https://github.com/spring-projects/spring-petclinic.git \
    && cd spring-petclinic \
    && mvn package


FROM openjdk:11
LABEL author="khaja"
EXPOSE 8080
COPY --from=builder /spring-petclinic/target/spring-petclinic-2.5.0-SNAPSHOT.jar /spring-petclinic.jar
CMD ["java", "-jar", "/spring-petclinic.jar"]

