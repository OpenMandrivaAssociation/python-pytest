%define module	pytest

Summary:	Cross-project testing tool for Python

Name:		python-%{module}
Version:	6.2.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/20/4c/d7b19b8661be78461fff0392e33943784340424921578fe1bf300ef59831/%{module}-%{version}.tar.gz
Patch0:         fix-version-issue.patch
License:	MIT
Group:		Development/Python
Url:		http://pytest.org
BuildArch:	noarch
Requires:	python-py >= 1.4.8
BuildRequires:	python-setuptools
BuildRequires:  python-setuptools_scm
BuildRequires:	python-sphinx
BuildRequires:	python-py >= 1.4.8
BuildRequires:	python-six

#Provides:	python%{py3_ver}dist(pytest) = %{EVRD}

%description
py.test is a simple cross-project testing tool for Python.

%prep
%setup -q -n %{module}-%{version}

%autopatch

%build
export PYTHONDONTWRITEBYTECODE=1

%py3_build

pushd doc/en
export PYTHONPATH=../../build/lib
#make html
popd

%install
%py3_install


%files
%doc CHANGELOG.rst
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info
%{_bindir}/py.test*
%{_bindir}/pytest
%{python3_sitelib}/_%{module}
%{python3_sitelib}/%{module}
