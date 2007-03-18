Summary:	MyThes thesaurus
Name:		mythes
Version:	1.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://lingucomponent.openoffice.org/MyThes-1.zip
# Source0-md5:	79e24a2e9a44d5d370d6685ff233064c
Patch0:		%{name}-optflags.patch
URL:		http://lingucomponent.openoffice.org/thesaurus.html
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MyThes is a simple thesaurus that uses a structured text data file and
an index file with binary search to lookup words and phrases and
return information on part of speech, meanings, and synonyms

MyThes was written to provide a thesaurus for the OpenOffice.org
project

%package devel
Summary:	Header files for MyThes library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for MyThes library.

%package static
Summary:	Static MyThes library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MyThes library.

%prep
%setup -q -n MyThes-%{version}
%patch0 -p1

%build
libtool --tag=CXX --mode=compile %{__cxx} mythes.cxx -c -o mythes.lo
libtool --tag=CXX --mode=link %{__cxx} mythes.lo -rpath %{_libdir} -o libmythes.la

libtool --tag=CXX --mode=compile %{__cxx} example.cxx -c -o example.lo
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
%{_includedir}/mythes.hxx
%{_libdir}/libmythes.la
%{_libdir}/libmythes.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libmythes.a
