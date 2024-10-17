Name:		texlive-etoolbox-de
Version:	21906
Release:	2
Summary:	German translation of documentation of etoolbox
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/etoolbox/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The version translated is 2.1 or 2011-01-03.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/etoolbox-de/etoolbox-DE.pdf
%doc %{_texmfdistdir}/doc/latex/etoolbox-de/etoolbox-DE.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
