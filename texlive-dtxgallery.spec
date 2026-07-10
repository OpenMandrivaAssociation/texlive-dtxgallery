%global tl_name dtxgallery
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	A small collection of minimal DTX examples
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/dtxgallery
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgallery.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgallery.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of files that demonstrate simple things that are possible
with the flexible and under-appreciated docstrip file format. Each file
of the collection is provided as a .dtx file and as the corresponding
.pdf. The set is intended as a companion to Scott Pakin's excellent and
influential dtxtut example of producing LaTeX packages in this way.

