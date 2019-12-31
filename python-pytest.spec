%define module	pytest

Summary:	Cross-project testing tool for Python

Name:		python-%{module}
Version:	5.3.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/c5/71/91ec682e10114f191da1a0ffabf35eccb9ab1c6bf9a535bb4a1b89ea59ca/pytest-5.3.2.tar.gz
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
