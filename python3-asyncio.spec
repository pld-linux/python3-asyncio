#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	asyncio
Summary:	Asynchronous IO Support
Name:		python3-%{module}
Version:	3.4.3
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/a/asyncio/%{module}-%{version}.tar.gz
# Source0-md5:	a189813096a6da1e46c16a41edb5f96d
URL:		https://pypi.python.org/pypi/asyncio
BuildRequires:	python3-2to3
BuildRequires:	python3-modules >= 3.3
BuildRequires:	rpm-pythonprov
Requires:	python3 >= 3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Asynchronous IO Support library - includes a pluggable event loop,
transport and protocol abstractions similar to those in Twisted, and a
higher-level scheduler based on yield from (PEP 380)

%prep
%setup  -q -n asyncio-%{version}

%build
%{__python3} setup.py build
%{?with_tests:%{__make} test PYTHON=%{__python3}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__python3} setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

cp -p examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
