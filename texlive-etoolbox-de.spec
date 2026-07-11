%global tl_name etoolbox-de
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	German translation of documentation of etoolbox
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/etoolbox/de
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox-de.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox-de.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The version translated is 2.1 or 2011-01-03.

