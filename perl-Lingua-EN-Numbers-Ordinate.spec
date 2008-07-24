%define module	Lingua-EN-Numbers-Ordinate
%define version 1.02
%define release %mkrel 7

Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
Summary:	Go from cardinal number (3) to ordinal ("3rd")
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/modules/by-module/Lingua/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
There are two kinds of numbers in English -- cardinals (1, 2, 3...), and
ordinals (1st, 2nd, 3rd...). This library provides functions for giving the
ordinal form of a number, given its cardinal value.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{perl_vendorlib}/Lingua
%{_mandir}/*/*
