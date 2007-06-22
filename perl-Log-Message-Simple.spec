%define	module	Log-Message-Simple
%define name	perl-%{module}
%define	modprefix Log/Message

%define version 0.02

%define	rel	1
%define release %mkrel %{rel}

Summary:	Standardized logging facilities using the "Log::Message" module
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Log::Message)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root


%description
Provides standardized logging facilities using the "Log::Message" module.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/%{modprefix}/*
%{_mandir}/*/*
