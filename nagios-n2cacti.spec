%include	/usr/lib/rpm/macros.perl
Summary:	Connector to send Nagios performance data to Cacti
Name:		nagios-n2cacti
Version:	0.3.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://nagios2cacti.googlecode.com/files/nagios2cacti.%{version}.tar.gz
# Source0-md5:	cd762d13339d76bed86f763c5f285724
Source1:	http://nagios2cacti.googlecode.com/files/nagios2cacti_pipe.odg
# Source1-md5:	43647040fa0545ed68460e55b84461b1
Source2:	http://nagios2cacti.googlecode.com/files/nagios2cacti_pipe.odg
# Source2-md5:	905a194a8e4925c89e586378855f3676
URL:		http://code.google.com/p/nagios2cacti/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# cames from perl-Error pkg, but dep not provided
%define		_noautoreq	'perl(Error::Simple)'

%description
Nagios 2 Cacti, N2Cacti, is a project derived from N2RRD. N2cacti will
parse Nagios Configuration, read N2RRD configuration (modified version
homemade) and will configure Cacti to create a Graph by Nagios
Services.

%prep
%setup -q -n nagios2cacti

# duplicate
rm etc/n2rrd/dist-n2rrd.conf

# somewhy i think this should be lowercase
mv etc/n2rrd/templates/rra/default.{T,t}
mv etc/n2rrd/templates/rra/PERF_EL.{T,t}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}/n2rrd,%{perl_vendorlib}/N2Cacti}
cp -a lib/N2Cacti/* $RPM_BUILD_ROOT%{perl_vendorlib}/N2Cacti
cp -a etc/n2rrd/* $RPM_BUILD_ROOT%{_sysconfdir}/n2rrd
install perf2rrd.pl send_perf.pl server_perf.pl $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog
%dir %{_sysconfdir}/n2rrd
%dir %{_sysconfdir}/n2rrd/templates
%dir %{_sysconfdir}/n2rrd/templates/code
%dir %{_sysconfdir}/n2rrd/templates/maps
%dir %{_sysconfdir}/n2rrd/templates/rewrite
%dir %{_sysconfdir}/n2rrd/templates/rewrite/service

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/n2rrd/*.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/n2rrd/templates/code/mem.pl
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/n2rrd/templates/maps/*_maps
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/n2rrd/templates/rewrite/*rewrite
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/n2rrd/templates/rewrite/service/*rewrite
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/n2rrd/templates/rra/*.t

%attr(755,root,root) %{_sbindir}/perf2rrd.pl
%attr(755,root,root) %{_sbindir}/send_perf.pl
%attr(755,root,root) %{_sbindir}/server_perf.pl
%{perl_vendorlib}/N2Cacti
