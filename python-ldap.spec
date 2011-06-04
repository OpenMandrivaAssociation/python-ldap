%define name python-ldap
%define version 2.4.0
%define rel 1
%define release %mkrel %rel

Summary: 	Various LDAP-related Python modules
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://pypi.python.org/packages/source/p/python-ldap/python-ldap-%{version}.tar.gz
Patch0:		python-ldap-2.4.0-fix-link.patch
License:	Modified CNRI Open Source License
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Url: 		http://python-ldap.sourceforge.net/
BuildRequires:	openldap-devel >= 2.4.11
BuildRequires:	python-devel

%description
python-ldap provides an object-oriented API to access LDAP directory 
servers from Python programs. Mainly it wraps the OpenLDAP 2.x libs 
for that purpose.

Additionally the package contains modules for other LDAP-related stuff 
(e.g. processing LDIF, LDAPURLs, LDAPv3 schema, etc.).

%prep
%setup -q
%patch0 -p0

%build
python setup.py build

%install
rm -Rf %{buildroot}
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README INSTALL TODO Demo/
%python_sitearch/*
