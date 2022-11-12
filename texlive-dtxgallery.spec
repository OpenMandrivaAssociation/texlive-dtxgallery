Name:		texlive-dtxgallery
Version:	49504
Release:	1
Summary:	A small collection of minimal DTX examples
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/dtxgallery
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgallery.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgallery.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A collection of files that demonstrate simple things that are
possible with the flexible and under-appreciated docstrip file
format. Each file of the collection is provided as a .dtx file
and as the corresponding .pdf. The set is intended as a
companion to Scott Pakin's excellent and influential dtxtut
example of producing LaTeX packages in this way.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/dtxgallery

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
