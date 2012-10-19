%define module	pytest
%define name	python-%{module}
%define version 2.3.0
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %rel
%else
%define	release	%rel
%endif

Summary:	Cross-project testing tool for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.zip
License:	MIT
Group:		Development/Python
Url:		http://pytest.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-py >= 1.4.8
BuildRequires:	python-setuptools, python-sphinx, python-py >= 1.4.8

%description
py.test is a simple cross-project testing tool for Python.

%prep
%setup -q -n %{module}-%{version}
%__python setup.py build
pushd doc/en
export PYTHONPATH=../build/lib
make html
popd

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG README.txt doc/en/_build/html
%_bindir/py.test*
%py_sitedir/*pytest*
