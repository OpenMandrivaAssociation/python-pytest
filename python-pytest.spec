%define module	pytest

Summary:	Cross-project testing tool for Python

Name:		python-%{module}
Version:	8.3.5
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pytest/pytest-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pytest.org
BuildArch:	noarch
Requires:	python-py >= 1.4.8
BuildRequires:	python-setuptools
BuildRequires:  python-setuptools_scm
BuildRequires:	python-sphinx
BuildRequires:	python-py >= 1.4.8
BuildRequires:	python-six
BuildRequires:	python-pip
BuildRequires:	python-wheel

%description
py.test is a simple cross-project testing tool for Python.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
export PYTHONDONTWRITEBYTECODE=1

%py3_build

pushd doc/en
export PYTHONPATH=../../build/lib
#make html
popd

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/__pycache__

%files
%doc CHANGELOG.rst
%{python3_sitelib}/%{module}-%{version}.dist-info
%{_bindir}/py.test*
%{_bindir}/pytest
%{python3_sitelib}/_%{module}
%{python3_sitelib}/%{module}
%{python3_sitelib}/py.py
