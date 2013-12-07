# revision 21906
# category Package
# catalog-ctan /info/translations/etoolbox/de
# catalog-date 2011-03-30 20:15:49 +0200
# catalog-license lppl
# catalog-version 1
Name:		texlive-etoolbox-de
Version:	1
Release:	5
Summary:	German translation of documentation of etoolbox
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/etoolbox/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox-de.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1-2
+ Revision: 751643
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1-1
+ Revision: 718381
- texlive-etoolbox-de
- texlive-etoolbox-de
- texlive-etoolbox-de
- texlive-etoolbox-de

