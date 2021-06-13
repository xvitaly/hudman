%global srcname hudman

%global _description %{expand:
This package provides a HUD Manager implementation.

HUD Manager is a simple tool for creating a local HUD mirror. Can be used
together with the SRC Repair project.

This product can operate in two modes: anonymous and authorized.
Please read manpage for additional information.}

Name: python-%{srcname}
Version: 3.2.0
Release: 1%{?dist}

License: GPLv3+
Summary: HUD Manager
URL: https://github.com/xvitaly/%{srcname}
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: doxygen
BuildRequires: python3-devel
BuildRequires: %{py3_dist requests}
BuildRequires: %{py3_dist setuptools}

BuildArch: noarch

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%package doc
Summary: Documentation for the %{name}

%description doc
This package provides auto-generated by Doxygen documentation for
the %{name} package.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build
doxygen

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%files doc
%doc docs/*

%changelog
* Sat Jun 12 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-1
- Updated to version 3.2.0.
