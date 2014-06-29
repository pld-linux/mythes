#
# Conditional build
%bcond_without	tests	# example testing
#
Summary:	MyThes thesaurus
Summary(pl.UTF-8):	MyThes - słownik wyrazów bliskoznacznych
Name:		mythes
Version:	1.2.4
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.gz
# Source0-md5:	a8c2c5b8f09e7ede322d5c602ff6a4b6
URL:		http://lingucomponent.openoffice.org/thesaurus.html
BuildRequires:	hunspell-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MyThes is a simple thesaurus that uses a structured text data file and
an index file with binary search to lookup words and phrases and
return information on part of speech, meanings, and synonyms.

MyThes was written to provide a thesaurus for the OpenOffice.org
project.

%description -l pl.UTF-8
MyThes jest prostym słownikiem wyrazów bliskoznacznych, który
wykorzystuje strukturalny plik danych oraz plik indeksu z
przeszukiwaniem binarnym do znajdowania słów oraz zdań i zwracania
informacji o części mowy, znaczeniu i synonimach.

MyThes powstał w celu dostarczenia słownika wyrazów bliskoznacznych
dla projektu OpenOffice.org.

%package devel
Summary:	Header files for MyThes library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki MyThes
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for MyThes library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki MyThes.

%package static
Summary:	Static MyThes library
Summary(pl.UTF-8):	Biblioteka statyczna MyThes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MyThes library.

%description static -l pl.UTF-8
Biblioteka statyczna MyThes.

%prep
%setup -q

%build
%configure
%{__make}

%if %{with tests}
./example th_en_US_new.idx th_en_US_new.dat checkme.lst
./example morph.idx morph.dat morph.lst morph.aff morph.dic
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README WordNet_{license,readme}.txt data_layout.txt
%attr(755,root,root) %{_libdir}/libmythes-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmythes-1.2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/th_gen_idx.pl
%attr(755,root,root) %{_libdir}/libmythes-1.2.so
%{_includedir}/mythes.hxx
%{_pkgconfigdir}/mythes.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmythes-1.2.a
