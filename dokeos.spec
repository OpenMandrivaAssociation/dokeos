Summary:	An elearning and course management web application
Name:		dokeos
Version:	1.8.6.1
Release:	3
License:	GPLv2+
Group:		Education
Url:		http://www.dokeos.com/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/dokeos/%{name}-%{version}.zip
Requires:	apache-mod_php
Requires:	php-mysql
Requires:	php-xml
BuildArch:	noarch

%description
Dokeos is an elearning and course management web application, translated
in 31 languages, already helping thousands of organisations worldwide to
manage learning and collaboration activities. It has many tools, is light
and flexible, and free software.

%files
%doc README.txt install.sh
%{_var}/www/html/%{name}

%post
echo "Default permissions of configuration files won't allow dokeo to make changes."
echo "To allow dokeos to make changes be sure to run %{_docdir}/%{name}-%{version}/install.sh"
echo "to change the permissions."
echo "Also be sure to restrict permissions of /var/www/html/dokeos/claroline/inc/conf/claro_main.conf.php"
echo "afterwards so other users can't write to it."
echo "Eg. chmod 644 /var/www/html/dokeos/claroline/inc/conf/claro_main.conf.php"

#----------------------------------------------------------------------------

%prep
%setup -q

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
install -d %{buildroot}%{_var}/www/html/%{name}
cp -r * %{buildroot}%{_var}/www/html/%{name}/

