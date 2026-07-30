%define upstream_name    HTTP-Parser
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Parse HTTP/1.1 request into HTTP::Request/Response object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/HTTP-Parser
Source0:	https://cpan.metacpan.org/authors/id/E/ED/EDECA/HTTP-Parser-0.06.tar.gz

BuildRequires:	make
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

