%define	name	dokeos
%define version 1.8.6.1
%define	rel	2
%define release %mkrel %{rel}
%define	webroot	%{_var}/www/html/%{name}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	An elearning and course management web application
Source0:	http://ovh.dl.sourceforge.net/sourceforge/dokeos/%{name}-%{version}.zip
License:	GPLv2
Group:		Education
URL:		http://www.dokeos.com/
Requires:	apache-mod_php php-mysql php-xml
%define _requires_exceptions pear\(.*\)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Dokeos is an elearning and course management web application, translated
in 31 languages, already helping thousands of organisations worldwide to
manage learning and collaboration activities. It has many tools, is light
and flexible, and free software.

%prep
%setup -q -n %name-%{version}

%build
cat << EOF > install.sh
#!/bin/sh
echo "Setting permissions of dokeos' files"
chmod 777 %{webroot}/claroline/inc/conf/
chmod 777 %{webroot}/claroline/garbage/
chmod 777 %{webroot}/claroline/upload/
chmod 777 %{webroot}/archive/
chmod 777 %{webroot}/courses/
chmod 777 %{webroot}/home/
echo ""
echo "Be sure to change the permission of /var/www/html/dokeos/claroline/inc/conf/claro_main.conf.php"
echo "afterwards so other users can't write to it."
echo "Eg. chmod 644 /var/www/html/dokeos/claroline/inc/conf/claro_main.conf.php"
EOF
chmod 700 install.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webroot}
cp -r * $RPM_BUILD_ROOT%{webroot}

%post
echo "Default permissions of configuration files won't allow dokeo to make changes."
echo "To allow dokeos to make changes be sure to run %{_docdir}/%{name}-%{version}/install.sh"
echo "to change the permissions."
echo "Also be sure to restrict permissions of /var/www/html/dokeos/claroline/inc/conf/claro_main.conf.php"
echo "afterwards so other users can't write to it."
echo "Eg. chmod 644 /var/www/html/dokeos/claroline/inc/conf/claro_main.conf.php"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt install.sh
%{webroot}



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.6.1-2mdv2011.0
+ Revision: 610263
- rebuild

* Sat Mar 06 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.8.6.1-1mdv2010.1
+ Revision: 514903
- update to 1.8.6.1
- fix %%prep and license

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.8.4-2mdv2010.0
+ Revision: 428324
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.8.4-1mdv2009.0
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 1.8.4-1mdv2008.1
+ Revision: 109188
- fix doc list
- New version 1.8.4
- import dokeos


* Mon Sep 04 2006 Jerome Soyer <saispo@mandriva.org> 1.6.5-1mdv2007.0
- New release 1.6.5

* Wed Jul 05 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.6.2-3mdv2007.0
- fix group

* Thu Oct 06 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.6.2-2mdk
- fix summary (thx misc)

* Wed Oct 05 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.6.2-1mdk
- initial release (requested by GOLL Aurélien <agoll@mandriva.com>)
