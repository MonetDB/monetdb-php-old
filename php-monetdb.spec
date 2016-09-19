Name:		php-monetdb
Version:	1.0
Release:	1%{?dist}
Summary:	MonetDB php interface
Group: Applications/Databases

License:	MPLv2.0
URL:		http://www.monetdb.org/
Source0:	https://dev.monetdb.org/hg/monetdb-php/archive/v%{version}.tar.bz2

Requires:	php
BuildArch:	noarch

Obsoletes:	MonetDB-client-php
Recommends:	MonetDB-SQL-server5

%description
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the files needed to use MonetDB from a PHP
program.


%prep
%autosetup -n monetdb-php-v%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license license.txt
%defattr(-,root,root)
%dir %{_datadir}/php/monetdb
%{_datadir}/php/monetdb/*



%changelog
* Wed Sep 14 2016 Sjoerd Mullender <sjoerd@acm.org>
- Initial independent version.

