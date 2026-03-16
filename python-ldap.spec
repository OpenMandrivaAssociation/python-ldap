%define module ldap
%define oname python_ldap

Name:		python-ldap
Summary:	Python modules for implementing LDAP clients
Version:	3.4.5
Release:	1
License:	python-ldap AND MIT
Group:		Development/Python
URL:		https://github.com/python-ldap/python-ldap
Source0:	%{URL}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	clang
BuildRequires:	glibc-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libsasl2)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(lber)
BuildRequires:	pkgconfig(ldap)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pyasn1)
BuildRequires:	python%{pyver}dist(pyasn1-modules)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
%{name} provides an object-oriented API to access LDAP directory
servers from Python programs.

Mainly it wraps the OpenLDAP client libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%build -p
export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{pyver} -lm"

%files
%doc README Demo/
%license LICENCE LICENCE.MIT
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{oname}-%{version}.dist-info
%{python3_sitearch}/slapdtest
%{python3_sitearch}/__pycache__
%{python3_sitearch}/_ldap*.so
%{python3_sitearch}/{ldif,ldapurl}.py
