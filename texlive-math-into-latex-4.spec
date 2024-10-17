Name:		texlive-math-into-latex-4
Version:	44131
Release:	2
Summary:	Samples from Math into LaTeX, 4th Edition
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/math-into-latex-4
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/math-into-latex-4.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/math-into-latex-4.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Samples for the book `(More) Math into LaTeX', 4th edition. In
addition, there are two excerpts from the book: A Short Course
to help you get started quickly with LaTeX, including detailed
instructions on how to install LaTeX on a PC or a Mac; Math and
Text Symbol Tables.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/math-into-latex-4

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
