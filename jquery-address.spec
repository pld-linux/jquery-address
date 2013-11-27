# TODO
# - package samples
%define		plugin	address
Summary:	jQuery Address - Deep linking for the masses
Name:		jquery-%{plugin}
Version:	1.5
Release:	1
License:	MIT / GPL v2
Group:		Applications/WWW
Source0:	http://www.asual.com/download/jquery.address-%{version}.zip
# Source0-md5:	840abddcb168dc27bc8648e4de6133df
URL:		http://www.asual.com/jquery/address/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
The jQuery Address plugin provides powerful deep linking capabilities
and allows the creation of unique virtual addresses that can point to
a website section or an application state. It enables a number of
important capabilities including:
- Bookmarking in a browser or social website
- Sending links via email or instant messenger
- Finding specific content using the major search engines
- Utilizing browser history and reload buttons

%prep
%setup -qn jquery.address-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.%{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
cp -p jquery.%{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
