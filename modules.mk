mod_kms_env.la: mod_kms_env.slo
	$(SH_LINK) -rpath $(libexecdir) -module -avoid-version  mod_kms_env.lo
DISTCLEAN_TARGETS = modules.mk
shared =  mod_kms_env.la
