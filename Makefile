
all: user_data

VMCONDOR_FILES=make_multipart_user_data      \
                  VMCondor_comments          \
                  VMCondor_condor            \
                  VMCondor_cloud-config      \
                  VMCondor_ucernvm           \
                  VMCondor_shellscript

user_data: IRIS.condor $(VMCONDOR_FILES)
	./make_VMCondor_user_data IRIS
	mv IRIS.user_data user_data
