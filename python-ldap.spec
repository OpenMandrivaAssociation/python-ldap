%define name python-ldap
%define version 2.3.1
%define rel 1

%define release %mkrel %rel

Summary: 	Various LDAP-related Python modules
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.gz
License:	Modified CNRI Open Source License
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Url: 		http://python-ldap.sourceforge.net/
BuildRequires:	openldap-devel >= 2.3
BuildRequires:	python-devel
Requires: 	python

%description
python-ldap provides an object-oriented API to access LDAP directory 
servers from Python programs. Mainly it wraps the OpenLDAP 2.x libs 
for that purpose.

Additionally the package contains modules for other LDAP-related stuff 
(e.g. processing LDIF, LDAPURLs, LDAPv3 schema, etc.).

%prep
%setup -q
perl -pi -e 's,^(library_dirs.*=).*,$1,g' setup.cfg
chmod a+r -R .

%build
export CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/sasl"
python setup.py build

%install
rm -Rf %{buildroot}
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc CHANGES README INSTALL TODO Demo/

