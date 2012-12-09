# revision 15878
# category Package
# catalog-ctan /info/dtxgallery
# catalog-date 2008-08-18 13:49:16 +0200
# catalog-license lppl
# catalog-version 1
Name:		texlive-dtxgallery
Version:	1
Release:	2
Summary:	A small collection of minimal DTX examples
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/dtxgallery
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgallery.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgallery.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgallery.source.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/dtxgallery/README
%doc %{_texmfdistdir}/doc/latex/dtxgallery/conditional-code.pdf
%doc %{_texmfdistdir}/doc/latex/dtxgallery/dtxgallery.pdf
%doc %{_texmfdistdir}/doc/latex/dtxgallery/rearrange.pdf
%doc %{_texmfdistdir}/doc/latex/dtxgallery/single-source.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dtxgallery/conditional-code.dtx
%doc %{_texmfdistdir}/source/latex/dtxgallery/dtxgallery.dtx
%doc %{_texmfdistdir}/source/latex/dtxgallery/rearrange.dtx
%doc %{_texmfdistdir}/source/latex/dtxgallery/single-source.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1-2
+ Revision: 751099
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1-1
+ Revision: 718268
- texlive-dtxgallery
- texlive-dtxgallery
- texlive-dtxgallery
- texlive-dtxgallery

