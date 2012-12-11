%define	upstream_name	 Log-Message-Simple
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Standardized logging facilities using the "Log::Message" module
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Log::Message)
BuildArch:	noarch

%description
Provides standardized logging facilities using the "Log::Message" module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Log/*
%{_mandir}/*/*


%changelog
* Tue Feb 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 634688
- update to new version 0.08

* Mon Sep 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 439422
- update to 0.06

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 408963
- rebuild using %%perl_convert_version

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.04-1mdv2009.0
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.1
+ Revision: 105467
- new version
- update to new version 0.04

  + Funda Wang <fwang@mandriva.org>
    - fix tarball url

* Fri Jun 22 2007 Buchan Milne <bgmilne@mandriva.org> 0.02-1mdv2008.0
+ Revision: 42915
- Buildrequire Log::Message
- Import perl-Log-Message-Simple



* Thu Jun 21 2007 Buchan Milne <bgmilne@mandriva.org> 0.02-1mdv2007.1
- initial package
