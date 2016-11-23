# This file contains the basic code for creation of user in container
FROM centos:latest
MAINTAINER shaik.khaja.ibrahim@live.in

RUN useradd -ms /bin/bash qt
USER qt
# only adding user without addding respective run commands will fail
# Add run