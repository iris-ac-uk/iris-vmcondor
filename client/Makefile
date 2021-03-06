#
#  Andrew McNab, University of Manchester.
#  Copyright (c) 2013-9. All rights reserved.
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
#  Contacts: Andrew.McNab@cern.ch  https://www.iris.ac.uk/
#

include ../VERSION

TGZ_FILES=vmcondor_setup example.sub example.sh vmcondor-client.spec ../VERSION

GNUTAR ?= tar
vmcondor-client.tgz: $(TGZ_FILES) rpm-Makefile Makefile
	mkdir -p TEMPDIR/vmcondor-client
	cp $(TGZ_FILES) TEMPDIR/vmcondor-client
	cp rpm-Makefile TEMPDIR/vmcondor-client/Makefile
	cd TEMPDIR ; $(GNUTAR) zcvf ../vmcondor-client.tgz --owner=root --group=root vmcondor-client
	rm -R TEMPDIR

rpm-build: vmcondor-client.tgz
	rm -Rf RPMTMP
	mkdir -p RPMTMP/SOURCES RPMTMP/SPECS RPMTMP/BUILD \
         RPMTMP/SRPMS RPMTMP/RPMS/noarch RPMTMP/BUILDROOT
	cp -f vmcondor-client.tgz RPMTMP/SOURCES
	export VERSION=$(VERSION) ; rpmbuild -ba \
	  --define "_topdir $(shell pwd)/RPMTMP" \
	  --buildroot $(shell pwd)/RPMTMP/BUILDROOT \
	  vmcondor-client.spec

docker-build: Dockerfile ../VERSION
	cp ../VERSION copy.of.VERSION
	docker build -t iris-vmcondor:$(VERSION) .
	rm -f copy.of.*

docker-push: docker-build
	docker tag iris-vmcondor:$(VERSION) irisacuk/iris-vmcondor:$(VERSION)
	docker tag iris-vmcondor:$(VERSION) irisacuk/iris-vmcondor:latest
	docker push irisacuk/iris-vmcondor:$(VERSION)
	docker push irisacuk/iris-vmcondor:latest
