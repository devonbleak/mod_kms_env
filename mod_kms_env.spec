%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo missing-httpd-devel)}}

Name:		mod_kms_env
Version:	1.0
Release:	1%{?dist}
Summary:	Apache module for decrypting environment variables using AWS Key Management Service (KMS)

Group:		System Environment/Daemons
License:	MIT
URL:		https://github.com/devonbleak/mod_kms_env
Source0:	mod_kms_env-%{version}.tar.gz

BuildRequires:	json-c-devel, apr-devel, apr-util-devel, openssl-devel, curl-devel, httpd-devel >= 2.4
Requires:		curl, json-c, openssl, apr, apr-util, httpd-mmn = %{_httpd_mmn}

%description
Apache module for decrypting environment variables using AWS Key Management Service.

Requires an AWS Instance running in an IAM role (or compatible interfaces to instance metadata).

See README.md for more information.


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -D -p -m 644 kms_env.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/kms_env.conf

%files
%defattr(-,root,root,0)
%doc README.md LICENSE
%{_libdir}/httpd/modules/mod_kms_env.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/kms_env.conf



%changelog

