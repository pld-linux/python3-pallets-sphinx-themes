Summary:	Sphinx themes for Pallets Project documentation
Summary(pl.UTF-8):	Motywy Sphinksa do dokumentacji z projektu Pallets
Name:		python3-pallets-sphinx-themes
Version:	2.3.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pallets-sphinx-themes/
Source0:	https://files.pythonhosted.org/packages/source/p/pallets-sphinx-themes/pallets_sphinx_themes-%{version}.tar.gz
# Source0-md5:	74ae0072d5585c851e108fce5a1b4112
URL:		https://palletsprojects.com/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Sphinx themes for Pallets related projects.

%description -l pl.UTF-8
Ten pakiet zawiera motywy Sphinksa dla projektów powiązanych z
Pallets.

%prep
%setup -q -n pallets_sphinx_themes-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.txt README.md
%{py3_sitescriptdir}/pallets_sphinx_themes
%{py3_sitescriptdir}/pallets_sphinx_themes-%{version}.dist-info
