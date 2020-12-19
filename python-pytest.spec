%define module	pytest

Summary:	Cross-project testing tool for Python

Name:		python-%{module}
Version:	6.2.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/20/4c/d7b19b8661be78461fff0392e33943784340424921578fe1bf300ef59831/%{module}-%{version}.tar.gz
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
#{py_puresitedir}/*
%{python_sitelib}/%{module}
#{python_sitelib}/%{module}-%{version}-py?.?.egg-info
%{python_sitelib}/%{module}-*-py*.egg-info
%{python_sitelib}/%{module}-*-py*.egg-info/PKG-INFO
%{python_sitelib}/_pytest/*
%{python_sitelib}/%{module}-*-py*.egg-info/SOURCES.txt
%{python_sitelib}/%{module}-*-py*.egg-info/dependency_links.txt
%{python_sitelib}/%{module}-*-py*.egg-info/entry_points.txt
%{python_sitelib}/%{module}-*-py*.egg-info/not-zip-safe
%{python_sitelib}/%{module}-*-py*.egg-info/requires.txt
%{python_sitelib}/%{module}-*-py*.egg-info/top_level.txt
