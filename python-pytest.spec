%define module	pytest

Summary:	Cross-project testing tool for Python

Name:		python-%{module}
Version:	5.3.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/eb/9c/8bf2a5e1a84e6b6d9a255ed1cda5d4b339699e9b1d95ed9f811209d588f8/pytest-5.3.4.tar.gz
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


%description
py.test is a simple cross-project testing tool for Python.

%prep
%setup -q -n %{module}-%{version}
export PYTHONDONTWRITEBYTECODE=1
python -B setup.py build

pushd doc/en
export PYTHONPATH=../../build/lib
#make html
popd

%install
PYTHONDONTWRITEBYTECODE=1  python -B setup.py install --root=%{buildroot}

%clean

%files
%doc CHANGELOG.rst
%{_bindir}/py.test*
%{_bindir}/pytest
%{py_puresitedir}/*
