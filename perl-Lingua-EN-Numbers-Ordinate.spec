%define module	Lingua-EN-Numbers-Ordinate
%define version 1.02
%define release %mkrel 3

Summary:	Go from cardinal number (3) to ordinal ("3rd")
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org/
Source:		http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/%{module}-%{version}.tar.bz2
#Requires:	perl
BuildRequires:	perl-devel >= 0:5.600
BuildArch:	noarch

%description
There are two kinds of numbers in English -- cardinals (1, 2, 3...), and
ordinals (1st, 2nd, 3rd...). This library provides functions for giving the
ordinal form of a number, given its cardinal value.

Authors:
--------
        Sean M. Burke <sburke@cpan.org>

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%doc README Changes
%{perl_vendorlib}/Lingua/*
%{_mandir}/*/*


