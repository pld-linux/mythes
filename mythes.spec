Summary:	MyThes thesaurus
Summary(pl.UTF-8):	MyThes - słownik wyrazów bliskoznacznych
Name:		mythes
Version:	1.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://lingucomponent.openoffice.org/MyThes-1.zip
# Source0-md5:	79e24a2e9a44d5d370d6685ff233064c
Patch0:		%{name}-optflags.patch
URL:		http://lingucomponent.openoffice.org/thesaurus.html
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MyThes is a simple thesaurus that uses a structured text data file and
an index file with binary search to lookup words and phrases and
return information on part of speech, meanings, and synonyms

MyThes was written to provide a thesaurus for the OpenOffice.org
project

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

%description -l pl.UTF-8
Pliki nagłówkowe biblioteki MyThes.

%package static
Summary:	Static MyThes library
Summary(pl.UTF-8):	Biblioteka statyczna MyThes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MyThes library.

%description -l pl.UTF-8
Biblioteka statyczna MyThes.

%prep
%setup -q -n MyThes-%{version}
%patch0 -p1

%build
CXXFLAGS="-Wall -ansi -pedantic %{rpmcxxflags}"
libtool --tag=CXX --mode=compile %{__cxx} mythes.cxx $CXXFLAGS -c -o mythes.lo
libtool --tag=CXX --mode=link %{__cxx} mythes.lo -rpath %{_libdir} -o libmythes.la

libtool --tag=CXX --mode=compile %{__cxx} example.cxx $CXXFLAGS -c -o example.lo
libtool --tag=CXX --mode=link %{__cxx} libmythes.la example.lo -o example

%check
./example th_en_US_new.idx th_en_US_new.dat checkme.lst

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}
install mythes.hxx $RPM_BUILD_ROOT%{_includedir}
libtool --mode=install install libmythes.la $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README data_layout.txt
%attr(755,root,root) %{_libdir}/libmythes.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmythes.so
%{_libdir}/libmythes.la
%{_includedir}/mythes.hxx

%files static
%defattr(644,root,root,755)
%{_libdir}/libmythes.a
