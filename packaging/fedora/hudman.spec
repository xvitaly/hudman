Name: hudman
Version: 3.0.0
Release: 1%{?dist}

Summary: HUD Manager
License: GPLv3+
URL: https://github.com/xvitaly/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: doxygen
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3dist(requests)

%{?python_provide:%python_provide python3-%{name}}

%description
HUD Manager is a simple tool for creating a local HUD mirror.

%prep
%autosetup -p1

%build
doxygen
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license LICENSE
%doc README.md doxyout/html
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*.egg-info

%changelog
* Wed Apr 14 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.0-1
- Updated to version 3.0.0.
