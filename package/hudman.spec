%global appname hudman

%global appsum Simple script to create a local HUD mirror
%global appdesc Simple script to create a local HUD mirror by EasyCoding Team

Name: python-%{appname}
Version: 2.2.0
Release: 1%{?dist}
Summary: %{appsum}

License: GPLv3+
URL: https://github.com/xvitaly/%{appname}
Source0: %{url}/archive/v%{version}.tar.gz#/%{appname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: doxygen
BuildRequires: python3-devel
BuildRequires: python3dist(requests)

%description
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
Requires: python3dist(requests)
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{appname}-%{version} -p1

%build
doxygen
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{appname}
%license LICENSE
%doc README.md
%doc docs/html
%{_bindir}/%{appname}
%{python3_sitelib}/%{appname}
%{python3_sitelib}/%{appname}-*.egg-info

%changelog
* Fri Oct 11 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.0-1
- Updated to version 2.2.0.

* Mon Sep 30 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.0-1
- Updated to version 2.1.0.

* Mon Sep 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-1
- Updated to version 2.0.0.

* Sat Nov 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-2
- Rebuilt for modern Fedora releases.

* Fri Jun 22 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Initial SPEC release.
