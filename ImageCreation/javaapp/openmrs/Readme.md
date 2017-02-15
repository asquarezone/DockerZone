# OpenMRS

![N|Solid](https://wiki.openmrs.org/download/attachments/131074/global.logo?version=6&modificationDate=1394803688000&api=v2)
The  installation steps can be found at https://wiki.openmrs.org/display/docs/Installing+OpenMRS

# Assumptions
1. lets use ubunt xenial for installation
2. mysql steps will be skipped
3. installation page of openmrs is treated as success for this version
# Steps!
Please follow the steps mentioned as below
  - Choose ubuntu xenial from docker hub
        - FROM ubuntu:xenial         
  - Install Java (Step 2 in open mrs documentation)
        -     Manual command is sudo apt-get install openjdk-6-jdk
        -     Dockerfile will have RUN apt-get -y install openjdk-6-jdk
  - Install tomcat
        -  Manual step (apt-get install tomcat7)
        -  RUN apt-get -y install tomcat7
  - Download openmrs.war 
        - location  https://downloads.sourceforge.net/project/openmrs/releases/OpenMRS_Platform_2.0.1/openmrs.war
        - find location of tomcat7 webapps (/var/lib/tomcat7/webapps/)
        - equivalent dockerfile statement ADD  https://downloads.sourceforge.net/project/openmrs/releases/OpenMRS_Platform_2.0.1/openmrs.war /var/lib/tomcat7/webapps/openmrs.war
        - Restart Service
        - RUN service tomcat7 restart
  - Need to execute the openmrs in detached mode
        - it takes to execute a file which will not return as the docker container will be stopped.




