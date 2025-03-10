Summary:	Sphinx themes for Pallets Project documentation
Summary(pl.UTF-8):	Motywy Sphinksa do dokumentacji z projektu Pallets
Name:		python3-pallets-sphinx-themes
Version:	2.0.2
Release:	6
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pallets-sphinx-themes/
Source0:	https://files.pythonhosted.org/packages/source/p/pallets-sphinx-themes/Pallets-Sphinx-Themes-%{version}.tar.gz
# Source0-md5:	898246b2cf5ee6f9826f40a31bc3a9ba
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
%setup -q -n Pallets-Sphinx-Themes-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.rst README.rst
%{py3_sitescriptdir}/pallets_sphinx_themes
%{py3_sitescriptdir}/Pallets_Sphinx_Themes-%{version}-py*.egg-info
