#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BigRat
Summary:	Math::BigRat - arbitrarily big rationales
Summary(pl.UTF-8):	Math::BigRat - dowolnie duże liczby wymierne
Name:		perl-Math-BigRat
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bcebef7d4b0130fad2c91a3a66b005fe
URL:		http://search.cpan.org/dist/Math-BigRat/
%if %{with tests}
BuildRequires:	perl-Math-BigInt >= 1.83
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.83
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigRat complements Math::BigInt and Math::BigFloat by providing
support for arbitrarily big rationales.

%description -l pl.UTF-8
Math::BigRat uzupełnia Math::BigInt i Math::BigFloat dostarczając
obsługę dowolnie dużych liczb wymiernych.

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
%doc BUGS CHANGES LICENSE README TODO
%{perl_vendorlib}/Math/BigRat.pm
%{_mandir}/man3/*
