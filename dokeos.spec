%define	name	dokeos
%define version 1.8.4
%define	rel	1
%define release %mkrel %{rel}
%define	webroot	%{_var}/www/html/%{name}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	An elearning and course management web application
Source0:	http://ovh.dl.sourceforge.net/sourceforge/dokeos/%{name}-%{version}.zip
License:	GPL
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
%setup -q -n %name

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

