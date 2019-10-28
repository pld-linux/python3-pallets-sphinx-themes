#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx themes for Pallets Project documentation
Summary(pl.UTF-8):	Motywy Sphinksa do dokumentacji z projektu Pallets
Name:		python-pallets-sphinx-themes
Version:	1.1.4
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pallets-sphinx-themes/
Source0:	https://files.pythonhosted.org/packages/source/p/pallets-sphinx-themes/Pallets-Sphinx-Themes-%{version}.tar.gz
# Source0-md5:	ed997c379de757b3575a3ac741131880
URL:		https://palletsprojects.com/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Sphinx themes for Pallets related projects.

%description -l pl.UTF-8
Ten pakiet zawiera motywy Sphinksa dla projektów powiązanych z
Pallets.

%package -n python3-pallets-sphinx-themes
Summary:	Sphinx themes for Pallets Project documentation
Summary(pl.UTF-8):	Motywy Sphinksa do dokumentacji z projektu Pallets
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pallets-sphinx-themes
This package contains Sphinx themes for Pallets related projects.

%description -n python3-pallets-sphinx-themes -l pl.UTF-8
Ten pakiet zawiera motywy Sphinksa dla projektów powiązanych z Pallets.

%prep
%setup -q -n Pallets-Sphinx-Themes-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst CHANGES.rst
%{py_sitescriptdir}/pallets_sphinx_themes
%{py_sitescriptdir}/Pallets_Sphinx_Themes-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pallets-sphinx-themes
%defattr(644,root,root,755)
%doc README.rst CHANGES.rst
%{py3_sitescriptdir}/pallets_sphinx_themes
%{py3_sitescriptdir}/Pallets_Sphinx_Themes-%{version}-py*.egg-info
%endif
