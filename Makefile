##
##  Makefile -- Build procedure for sample kms_env Apache module
##  Autogenerated via ``apxs -n kms_env -g''.
##

builddir=.
top_srcdir=/etc/httpd
top_builddir=/usr/lib64/httpd
include /usr/lib64/httpd/build/special.mk

#   the used tools
APACHECTL=apachectl

#   additional defines, includes and libraries
#DEFS=-Dmy_define=my_value
#INCLUDES=-Imy/include/dir
LDFLAGS=-ljson-c -lcrypto -lcurl

#   the default target
all: local-shared-build

#   install the shared object file into Apache 
install: install-modules-yes

#   cleanup
clean:
	-rm -f mod_kms_env.o mod_kms_env.lo mod_kms_env.slo mod_kms_env.la 

#   simple test
test: reload
	lynx -mime_header http://localhost/kms_env

#   install and activate shared object by reloading Apache to
#   force a reload of the shared object file
reload: install restart

#   the general Apache start/restart/stop
#   procedures
start:
	$(APACHECTL) start
restart:
	$(APACHECTL) restart
stop:
	$(APACHECTL) stop

