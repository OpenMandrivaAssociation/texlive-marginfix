# revision 24320
# category Package
# catalog-ctan /macros/latex/contrib/marginfix
# catalog-date 2010-09-10 23:39:51 +0200
# catalog-license lppl
# catalog-version 0.9.1
Name:		texlive-marginfix
Version:	0.9.1
Release:	1
Summary:	Patch \marginpar to avoid overfull margins
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/marginfix
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginfix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginfix.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginfix.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Authors using LaTeX to typeset books with significant margin
material often run into the problem of long notes running off
the bottom of the page. A typical workaround is to insert
\vshift commands by hand, but this is a tedious process that is
invalidated when pagination changes. Another workaround is
memoir's \sidebar function, but this can be unsatisfying for
short textual notes, and standard marginpars cannot be mixed
with sidebars. This package implements a solution to make
marginpars "just work" by keeping a list of floating inserts
and arranging them intelligently in the output routine.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/marginfix/marginfix.sty
%doc %{_texmfdistdir}/doc/latex/marginfix/README
%doc %{_texmfdistdir}/doc/latex/marginfix/marginfix.pdf
#- source
%doc %{_texmfdistdir}/source/latex/marginfix/marginfix.dtx
%doc %{_texmfdistdir}/source/latex/marginfix/marginfix.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
