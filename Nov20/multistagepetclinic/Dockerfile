FROM maven:3-openjdk-8 AS builder
RUN git clone https://github.com/spring-projects/spring-petclinic.git
RUN cd /spring-petclinic/ && mvn package

FROM  openjdk:8
COPY --from=builder /spring-petclinic/target/spring-petclinic-2.3.0.BUILD-SNAPSHOT.jar /spring-petclinic.jar
EXPOSE 8080
CMD ["java", "-jar", "/spring-petclinic.jar"]