%define module	pytest
%define name	python-%{module}
%define version 2.2.4
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
pushd doc
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
%doc CHANGELOG README.txt doc/_build/html
%_bindir/py.test*
%py_sitedir/*pytest*


%changelog
* Sun Jun 10 2012 Lev Givon <lev@mandriva.org> 2.2.4-1
+ Revision: 804349
- Update to 2.2.4.

* Tue Jan 10 2012 Lev Givon <lev@mandriva.org> 2.2.1-1
+ Revision: 759481
- Update to 2.2.1.

* Thu Dec 01 2011 Lev Givon <lev@mandriva.org> 2.2.0-1
+ Revision: 737086
- Update to 2.2.0.

* Tue Oct 25 2011 Lev Givon <lev@mandriva.org> 2.1.3-1
+ Revision: 707173
- Update to 2.1.3.

* Sun Aug 21 2011 Lev Givon <lev@mandriva.org> 2.1.1-1
+ Revision: 695927
- Update to 2.1.1.

* Wed Jul 20 2011 Lev Givon <lev@mandriva.org> 2.1.0-1
+ Revision: 690786
- import python-pytest


