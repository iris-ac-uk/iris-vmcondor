
vmcondor.0001.key: VMCondorCA00.pem
	openssl req -config VMCondorCA.cnf \
                    -newkey rsa:2048 \
                    -keyout key0001.pem \
                    -subj '/CN=VMCondor Request' \
                    -nodes \
                    -out req0001.pem
	echo 01 > ca.serial
	cp /dev/null ca.db
	cp /dev/null ca.db.attr
	openssl ca -config VMCondorCA.cnf \
                   -batch \
                   -in req0001.pem \
                   -subj '/O=vmcondor.iris.ac.uk/CN=user0001' \
                   -days 365 \
                   -noemailDN \
                   -extensions user_ext \
                   -out cert0001.pem
	cat cert0001.pem key0001.pem > vmcondor.0001.key
	openssl x509 -in vmcondor.0001.key -subject -issuer -startdate -enddate
	cat key0001.pem

VMCondorCA00.pem: Makefile VMCondorCA.cnf
	openssl req -config VMCondorCA.cnf \
                    -newkey rsa:2048 \
                    -x509 \
                    -set_serial 0 \
                    -days 3650 \
                    -nodes \
                    -extensions ca_ext \
                    -keyout VMCondorCA00key.pem \
                    -subj '/O=vmcondor.iris.ac.uk/CN=VMCondor CA 00' \
                    -out VMCondorCA00.pem
	openssl x509 -in VMCondorCA00.pem -subject -issuer -startdate -enddate -subject_hash
