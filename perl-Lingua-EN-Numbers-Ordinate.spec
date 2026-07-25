%define upstream_name	 Lingua-EN-Numbers-Ordinate
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Go from cardinal number (3) to ordinal ("3rd")

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/neilb/Lingua-EN-Numbers-Ordinate
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Lingua-EN-Numbers-Ordinate-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
There are two kinds of numbers in English -- cardinals (1, 2, 3...), and
ordinals (1st, 2nd, 3rd...). This library provides functions for giving the
ordinal form of a number, given its cardinal value.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README 
%{perl_vendorlib}/Lingua
%{_mandir}/*/*
