%define upstream_name	 Lingua-EN-Numbers-Ordinate
%define upstream_version 1.02

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary:	Go from cardinal number (3) to ordinal ("3rd")
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
There are two kinds of numbers in English -- cardinals (1, 2, 3...), and
ordinals (1st, 2nd, 3rd...). This library provides functions for giving the
ordinal form of a number, given its cardinal value.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
