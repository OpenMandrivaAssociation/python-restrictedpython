Name:		python-restrictedpython
Version:	8.5
Release:	2
Summary:	RestrictedPython is a defined subset of the Python language which allows
License:	ZPL-2.1
Group:		Development/Python
URL:		https://pypi.org/project/restrictedpython/
Source0:	restrictedpython-8.5.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
RestrictedPython is a defined subset of the Python language which allows.

%files
%{py_sitedir}/*
