%define upstream_name    HTTP-Parser
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Parse HTTP/1.1 request into HTTP::Request/Response object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
This is an HTTP request parser. It takes chunks of text as received and
returns a 'hint' as to what is required, or returns the HTTP::Request when
a complete request has been read. HTTP/1.1 chunking is supported. It dies
if it finds an error.

new ( named params... )
    Create a new HTTP::Parser object. Takes named parameters, e.g.:

     my $parser = HTTP::Parser->new(request => 1);

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.60.0-3mdv2011.0
+ Revision: 658281
- rebuild

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2
+ Revision: 657441
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1
+ Revision: 643382
- update to new version 0.06

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 624762
- import perl-HTTP-Parser

