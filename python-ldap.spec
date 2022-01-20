Summary:	Various LDAP-related Python modules
Name:		python-ldap
Version:	3.4.0
Release:	1
License:	Modified CNRI Open Source License
Group:		Development/Python
Url:		http://python-ldap.sourceforge.net/
Source0:	https://pypi.python.org/packages/source/p/python-ldap/%{name}-%{version}.tar.gz
BuildRequires:	openldap-devel >= 2.4.11
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libsasl2)
BuildRequires:	pkgconfig(openssl)

%description
python-ldap provides an object-oriented API to access LDAP directory 
servers from Python programs. Mainly it wraps the OpenLDAP 2.x libs 
for that purpose.

Additionally the package contains modules for other LDAP-related stuff 
(e.g. processing LDIF, LDAPURLs, LDAPv3 schema, etc.).

%prep
%setup -q
%autopatch -p1
find -type f|xargs chmod 644

%build
python setup.py build build_ext -llber,sasl2,ssl,crypto,m

%install
python setup.py install --root=%{buildroot}

%files
%doc CHANGES README TODO Demo/
%{py3_platsitedir}/*


