#
#  Andrew McNab, University of Manchester.
#  Copyright (c) 2018-9. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or
#  without modification, are permitted provided that the following
#  conditions are met:
#
#    o Redistributions of source code must retain the above
#      copyright notice, this list of conditions and the following
#      disclaimer. 
#    o Redistributions in binary form must reproduce the above
#      copyright notice, this list of conditions and the following
#      disclaimer in the documentation and/or other materials
#      provided with the distribution. 
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
#  CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
#  INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS
#  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
#  TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#  ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
#  OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#
#  Contacts: Andrew.McNab@cern.ch  https://www.iris.ac.uk
#
FROM centos:7

# Install HTCondor 
RUN curl --output /root/RPM-GPG-KEY-HTCondor \
      https://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor
RUN rpm --import /root/RPM-GPG-KEY-HTCondor
RUN curl --output /etc/yum.repos.d/htcondor-stable-rhel7.repo \
      https://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo
RUN yum -y --setopt=tsflags='' install condor

# Repositories
RUN yum -y --setopt=tsflags='' install epel-release 

# Packages we need or want
RUN yum -y --setopt=tsflags='' install \
                   emacs \
                   joe \
                   less \
                   which \
                   man \
                   man-pages \
                   man-pages-overrides \
                   nano \
                   openssl \
                   wget

COPY copy.of.vmcondor_setup /usr/local/bin/vmcondor_setup

RUN /usr/local/bin/vmcondor_setup --just-symlinks

RUN echo -e 'export PATH=$HOME/bin:$PATH\nexport PS1="vmcondor.\u: "' > /etc/profile.d/vmcondor.sh
RUN echo -e 'setenv PATH $HOME/bin:$PATH\nset prompt "vmcondor.%n: "' > /etc/profile.d/vmcondor.csh

# Add a non-privileged user
RUN useradd --create-home --skel /dev/null user
