%define format	sgml	
%define format2	SGML/nl

%define version 2006
%define release %mkrel 6

Summary:	HOWTO documents (%{format} format) from the Linux Documentation Project
Name:		howto-%{format}-nl
Version: 	%version
Release: 	%release
Group:		Books/Howtos
Source0:	howto-%{format}-nl.tar.bz2
Url:		http://www.linuxdoc.org/docs.html#howto
License:	GPL
BuildRoot:	%{_tmppath}/howto-%{format}-root
BuildArchitectures: noarch
Requires:   locales-nl howto-utils
BuildRequires:  howto-utils

%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

Install this package if you'd like to be able to modify the Linux
HOWTO documentation from your own system.

%prep 
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
cd $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
bzcat %{SOURCE0} | tar xv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/HOWTO/%{format2}




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2006-6mdv2011.0
+ Revision: 619405
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2006-5mdv2010.0
+ Revision: 429407
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2006-4mdv2009.0
+ Revision: 246979
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 2006-3mdv2009.0
+ Revision: 239601
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2006-1mdv2008.1
+ Revision: 126795
- kill re-definition of %%buildroot on Pixel's request
- import howto-sgml-nl


* Fri Dec 09 2005 Lenny Cartier <lenny@mandriva.com> 2006-1mdk
- rebuild

* Wed Oct 08 2003 Lenny Cartier <lenny@mandrakesoft.com> 9.2-1mdk
- updated

* Sun Sep 15 2002 Lenny Cartier <lenny@mandrakesoft.com> 9.0-1mdk
- updated

* Thu Sep 06 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-1mdk
- Updated: Thu Sep 06 2001
- Add Require on locale-nl
- first Mandrake release  
