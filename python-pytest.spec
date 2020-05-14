%define module	pytest

Summary:	Cross-project testing tool for Python

Name:		python-%{module}
Version:	5.4.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/49/10/4a8f2f7828b195fe9c9e2b910e9b0dd3d4a263bffbab54f09bf6c2f488bb/pytest-5.4.2.tar.gz
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
