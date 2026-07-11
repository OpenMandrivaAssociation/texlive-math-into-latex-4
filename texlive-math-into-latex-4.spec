%global tl_name math-into-latex-4
%global tl_revision 44131

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Samples from Math into LaTeX, 4th Edition
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/examples/Math_into_LaTeX-4
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/math-into-latex-4.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/math-into-latex-4.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Samples for the book `(More) Math into LaTeX', 4th edition. In addition,
there are two excerpts from the book: A Short Course to help you get
started quickly with LaTeX, including detailed instructions on how to
install LaTeX on a PC or a Mac; Math and Text Symbol Tables.

