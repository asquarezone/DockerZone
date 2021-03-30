FROM maven:3-jdk-11 as mvn
RUN git clone https://github.com/spring-projects/spring-petclinic.git 
RUN cd spring-petclinic && mvn package


FROM openjdk:11
LABEL author="khaja"
COPY --from=mvn /spring-petclinic/target/spring-petclinic-2.4.2.jar /spring-petclinic-2.4.2.jar
EXPOSE 8080
CMD ["java", "-jar", "/spring-petclinic-2.4.2.jar"]
