#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	BigRat
Summary:	Math::BigRat - arbitrarily big rationales
Summary(pl):	Math::BigRat - dowolnie du¿e liczby wymierne
Name:		perl-Math-BigRat
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c5c7fb4ded420beb5f8fa38001ef8fe7
BuildRequires:	perl-Math-BigInt >= 1.61
BuildRequires:	perl(Math::BigFloat) >= 1.36
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.61
Requires:	perl(Math::BigFloat) >= 1.36
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigRat complements Math::BigInt and Math::BigFloat by providing
support for arbitrarily big rationales.

%description -l pl
Math::BigRat uzupe³nia Math::BigInt i Math::BigFloat dostarczaj±c
obs³ugê dowolnie du¿ych liczb wymiernych.

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
%doc BUGS CHANGES LICENSE NEW README TODO
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
