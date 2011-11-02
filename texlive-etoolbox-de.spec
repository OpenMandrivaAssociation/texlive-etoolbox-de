Name:		texlive-etoolbox-de
Version:	1
Release:	1
Summary:	German translation of documentation of etoolbox
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/etoolbox/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The version translated is 2.1 or 2011-01-03.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/etoolbox-de/etoolbox-DE.pdf
%doc %{_texmfdistdir}/doc/latex/etoolbox-de/etoolbox-DE.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
