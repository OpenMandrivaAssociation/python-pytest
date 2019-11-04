%define module	pytest

Summary:	Cross-project testing tool for Python

Name:		python-%{module}
Version:	5.2.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/24/67/051f7622814613980a03c9722233a4d7f8b0e21787a46b41a1057c903992/pytest-5.2.2.tar.gz
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
