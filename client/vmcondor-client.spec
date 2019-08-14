Name: vmcondor-client
Version: %(echo ${VMCONDOR_VERSION:-0.0})
Release: 1
BuildArch: noarch
Summary: vmcondor-client
License: BSD
Group: Tool
Source: vmcondor-client.tgz
URL: https://www.iris.ac.uk/
Vendor: IRIS
Packager: Andrew McNab <Andrew.McNab@cern.ch>
Requires: openssl,curl,condor

%description
VMCondor allows users to submit HTCondor batch jobs to a common pool of 
virtual machines managed by Vcycle/OpenStack or Vac at multiple IRIS sites. 

%prep

%setup -n vmcondor-client

%build

%install
make install

%files
/usr/bin/*
/usr/lib/vmcondor-client
