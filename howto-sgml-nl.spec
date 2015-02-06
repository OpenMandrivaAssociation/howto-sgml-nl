%define format2 SGML/nl

Summary:	HOWTO documents (sgml format) from the Linux Documentation Project
Name:		howto-sgml-nl
Version:	2006
Release:	8
License:	GPLv2+
Group:		Books/Howtos
Source0:	howto-sgml-nl.tar.bz2
Url:		http://www.linuxdoc.org/docs.html#howto
BuildRequires:	howto-utils
Requires:	howto-utils
Requires:	locales-nl
BuildArch:	noarch

%description
Linux HOWTOs are detailed documents which describe a specific aspect of
configuring or using Linux. Linux HOWTOs are a great source of
practical information about your system. The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

Install this package if you'd like to be able to modify the Linux
HOWTO documentation from your own system.

%files
%{_docdir}/HOWTO/SGML/nl

#----------------------------------------------------------------------------

%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/HOWTO/SGML/nl
cd %{buildroot}%{_docdir}/HOWTO/SGML/nl
bzcat %{SOURCE0} | tar xv


