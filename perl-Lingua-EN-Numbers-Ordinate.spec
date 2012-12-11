%define upstream_name	 Lingua-EN-Numbers-Ordinate
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Go from cardinal number (3) to ordinal ("3rd")
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.bz2

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
%doc README ChangeLog
%{perl_vendorlib}/Lingua
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 402569
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.02-8mdv2009.0
+ Revision: 257533
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.02-7mdv2009.0
+ Revision: 245617
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-5mdv2008.1
+ Revision: 137206
- spec cleanup

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-4mdv2008.1
+ Revision: 136999
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 04 2006 Stefan van der Eijk <stefan@mandriva.org> 1.02-3mdv2007.0
+ Revision: 76574
- rebuild
- Import perl-Lingua-EN-Numbers-Ordinate

* Sun Feb 05 2006 Stefan van der Eijk <stefan@eijk.nu> 1.02-2mdk
- Rebuild
- %%mkrel

* Mon Jan 17 2005 Stefan van der Eijk <stefan@mandrakesoft.com> 1.02-1mdk
- New release 1.02

* Fri Nov 28 2003 Stefan van der Eijk <stefan@eijk.nu> 0.01-2mdk
- rpmlint fixes
- revamp .spec file

