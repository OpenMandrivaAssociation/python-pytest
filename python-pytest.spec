%define module	pytest
%define name	python-%{module}
%define version 2.2.0
%define release %mkrel 1

Summary:	Cross-project testing tool for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.zip
License:	MIT
Group:		Development/Python
Url:		http://pytest.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
py.test is a simple cross-project testing tool for Python.

%prep
%setup -q -n %{module}-%{version}
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc CHANGELOG README.txt
