#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sub
%define	pnam	Override
Summary:	Sub::Override - Perl extension for easily overriding subroutines
Summary(pl.UTF-8):   Sub::Override - rozszerzenie Perla do łatwego przykrywania procedur
Name:		perl-Sub-Override
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8261e3d77145f0b154641597b7983bd6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception >= 0.15
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sometimes subroutines need to be overridden. In fact, your author does
this constantly for tests. Particularly when testing, using a Mock
Object can be overkill when all you want to do is override one tiny,
little function.

Sub::Override allows the programmer to simply name the sub to replace
and to supply a sub to replace it with.

%description -l pl.UTF-8
Czasem procedura musi zostać przykryta. W praktyce autor robi to stale
dla testów. W szczególności przy testowaniu używanie obiektu Mock może
być nadmiarowe, gdy wszystko co chcemy, to przykryć jedną małą,
maleńką funkcję.

Sub::Override umożliwia programiście prosto nazwać funkcję do
zastąpienia i dostarczyć funkcję do zastąpienia jej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sub/*.pm
%{_mandir}/man3/*
