#
# Conditional build
%bcond_without	static_libs	# static library
%bcond_without	tests		# example testing
#
Summary:	MyThes thesaurus
Summary(pl.UTF-8):	MyThes - słownik wyrazów bliskoznacznych
Name:		mythes
Version:	1.2.5
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/hunspell/mythes/releases
Source0:	https://github.com/hunspell/mythes/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	35d91f6d9d5e1be3388aaddd63bc4d86
URL:		http://lingucomponent.openoffice.org/thesaurus.html
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	hunspell-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
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
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%if %{with tests}
%{__make} check

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
%doc AUTHORS COPYING README WordNet_{license,readme}.txt data_layout.txt
%attr(755,root,root) %{_libdir}/libmythes-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmythes-1.2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/th_gen_idx.pl
%attr(755,root,root) %{_libdir}/libmythes-1.2.so
%{_includedir}/mythes.hxx
%{_pkgconfigdir}/mythes.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmythes-1.2.a
%endif
