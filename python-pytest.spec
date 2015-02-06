%define module	pytest

Summary:	Cross-project testing tool for Python

Name:		python-%{module}
Version:	2.6.4
Release:	2
Source0:	http://pypi.python.org/packages/source/p/pytest/pytest-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pytest.org
BuildArch:	noarch
Requires:	python-py >= 1.4.8
BuildRequires:	python-setuptools, python-sphinx, python-py >= 1.4.8

%description
py.test is a simple cross-project testing tool for Python.

%prep
%setup -q -n %{module}-%{version}
export PYTHONDONTWRITEBYTECODE=1
python -B setup.py build

pushd doc/en
export PYTHONPATH=../../build/lib
make html
popd

%install
PYTHONDONTWRITEBYTECODE=1  python -B setup.py install --root=%{buildroot}

%clean

%files
%doc CHANGELOG  doc/en/_build/html
%{_bindir}/py.test*
%{py_puresitedir}/*pytest*
