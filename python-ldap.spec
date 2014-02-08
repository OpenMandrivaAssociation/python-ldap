Summary:	Various LDAP-related Python modules
Name:		python-ldap
Version:	2.4.12
Release:	2
Source0:	http://pypi.python.org/packages/source/p/python-ldap/%{name}-%{version}.tar.gz
Patch0:		python-ldap-2.4.6-dirs.patch
License:	Modified CNRI Open Source License
Group:		Development/Python
Url:		http://python-ldap.sourceforge.net/
BuildRequires:	openldap-devel >= 2.4.11
BuildRequires:	pkgconfig(python2)

%description
python-ldap provides an object-oriented API to access LDAP directory 
servers from Python programs. Mainly it wraps the OpenLDAP 2.x libs 
for that purpose.

Additionally the package contains modules for other LDAP-related stuff 
(e.g. processing LDIF, LDAPURLs, LDAPv3 schema, etc.).

%prep
%setup -q
%patch0 -p1
find -type f|xargs chmod 644

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc CHANGES README TODO Demo/
%{python_sitearch}/*
