%define name python-ldap
%define version 2.4.0
%define rel 2
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


%changelog
* Sat Jun 04 2011 Funda Wang <fwang@mandriva.org> 2.4.0-1mdv2011.0
+ Revision: 682727
- new version 2.4.0

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3.12-2
+ Revision: 667941
- mass rebuild

* Thu Nov 25 2010 Funda Wang <fwang@mandriva.org> 2.3.12-1mdv2011.0
+ Revision: 600940
- new version 2.3.12

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 2.3.11-6mdv2011.0
+ Revision: 589996
- rebuild for python 2.7

* Tue May 04 2010 Eugeni Dodonov <eugeni@mandriva.com> 2.3.11-5mdv2010.1
+ Revision: 542084
- Re-enable ssl support, broken by latest patch.

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 2.3.11-4mdv2010.1
+ Revision: 532475
- newer patch

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 2.3.11-3mdv2010.1
+ Revision: 532474
- fix link

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.3.11-2mdv2010.1
+ Revision: 515902
- update to 2.3.11

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.10-2mdv2010.1
+ Revision: 511631
- rebuilt against openssl-0.9.8m

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.10-1mdv2010.1
+ Revision: 496369
- update to new version 2.3.10

* Wed Aug 05 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.9-1mdv2010.0
+ Revision: 410343
- update to new version 2.3.9

* Mon May 11 2009 Buchan Milne <bgmilne@mandriva.org> 2.3.8-1mdv2010.0
+ Revision: 374233
- update to new version 2.3.8
- Fix source URL

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 2.3.5-2mdv2009.1
+ Revision: 318990
- rebuild for new python

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.5-1mdv2009.1
+ Revision: 305840
- update to new version 2.3.5

* Fri May 02 2008 Funda Wang <fwang@mandriva.org> 2.3.4-1mdv2009.0
+ Revision: 199939
- update to new version 2.3.4

* Sun Feb 10 2008 Frederik Himpe <fhimpe@mandriva.org> 2.3.1-2mdv2008.1
+ Revision: 164726
- Rebuild against openldap 2.4 libraries

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Funda Wang <fwang@mandriva.org> 2.3.1-1mdv2008.0
+ Revision: 55848
- Remove patch, merged upstream
- New version

  + Andreas Hasenack <andreas@mandriva.com>
    - added support for modify+increment (RFC4525) extension

* Thu May 03 2007 Andreas Hasenack <andreas@mandriva.com> 2.3-1mdv2008.0
+ Revision: 21512
- updated to version 2.3
- adjusted buildrequires, we now require openldap-devel >= 2.3


* Sun Mar 04 2007 Gustavo De Nardin <gustavodn@mandriva.com> 2.2.1-3mdv2007.0
+ Revision: 132191
- Requires python, not just python-base (fixes bug #27794).

* Wed Nov 29 2006 Andreas Hasenack <andreas@mandriva.com> 2.2.1-2mdv2007.1
+ Revision: 88466
- rebuild with python 2.5

* Thu Nov 16 2006 Andreas Hasenack <andreas@mandriva.com> 2.2.1-1mdv2007.1
+ Revision: 84835
- updated to version 2.2.1
- Import python-ldap

* Fri May 05 2006 Andreas Hasenack <andreas@mandriva.com> 2.2.0-1mdk
- updated to version 2.2.0

* Wed Nov 23 2005 Andreas Hasenack <andreas@mandriva.com> 2.0.11-2mdk
- rebuilt with openssl 0.9.8a

* Mon Nov 07 2005 Buchan Milne <bgmilne@mandriva.org> 2.0.11-1mdk
- New release 2.0.11

* Wed Aug 31 2005 Emmanuel Blindauer <blindauer@mandriva.org> 2.0.9-2mdk
- Add missing Requires

* Fri Jul 29 2005 Buchan Milne <bgmilne@linux-mandrake.com> 2.0.9-1mdk
- New release 2.0.9

* Wed Jun 22 2005 Buchan Milne <bgmilne@linux-mandrake.com> 2.0.8-1mdk
- New release 2.0.8
- rpmbuildupdate-able and %%mkrel-ed
- clean buildroot in %%install
- cleanups

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 2.0.2-2mdk
- Rebuild for new python

* Thu Sep 02 2004 Buchan Milne <bgmilne@linux-mandrake.com> 2.0.2-1mdk
- 2.0.2

* Wed Jul 21 2004 Buchan Milne<bgmilne@linux-mandrake.com> 2.0.1-1mdk
- 2.0.1
- remove redundant buildrequires
- drop patch (no longer required), empty library_dirs in setup.cfg to avoid
  rpath entries

* Tue Apr 20 2004 Pascal Terjan <pterjan@mandrake.org> 2.0.0-0.pre19.3mdk
- BuildRequires openssl-devel

* Tue Apr 20 2004 Pascal Terjan <pterjan@mandrake.org> 2.0.0-0.pre19.2mdk
- BuildRequires libsasl2-devel

