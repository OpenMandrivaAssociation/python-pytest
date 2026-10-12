%define module	pytest

Summary:	Cross-project testing tool for Python

Name:		python-%{module}
Version:	9.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pytest/pytest-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pytest.org
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(iniconfig)
BuildRequires:	python%{pyver}dist(pluggy)
BuildRequires:	python%{pyver}dist(packaging)

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%description
py.test is a simple cross-project testing tool for Python.

%install -a
rm -rf %{buildroot}%{python_sitelib}/__pycache__

%files
%doc CHANGELOG.rst
%{python_sitelib}/%{module}-%{version}.dist-info
%{_bindir}/py.test*
%{_bindir}/pytest
%{python_sitelib}/_%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/py.py
