FROM ubuntu:trusty
MAINTAINER asquarezone
RUN apt-get update 
ADD https://codeload.github.com/asquarezone/DockerZone/zip/master /master
ADD https://pm.puppetlabs.com/puppet-agent/2017.1.1/1.9.3/repos/deb/trusty/PC1/puppet-agent_1.9.3-1trusty_amd64.deb /puppet-agent_1.9.3-1trusty_amd64.deb
CMD ["/bin/bash"]