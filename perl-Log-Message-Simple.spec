%define	upstream_name	 Log-Message-Simple
%define upstream_version 0.10
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.10
Release:	3

Summary:	Standardized logging facilities using the "Log::Message" module
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Log/Log-Message-Simple-0.10.tar.gz

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
