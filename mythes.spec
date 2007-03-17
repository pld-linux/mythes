Summary:	MyThes thesaurus
Name:		mythes
Version:	1.0
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://lingucomponent.openoffice.org/MyThes-1.zip
# Source0-md5:	79e24a2e9a44d5d370d6685ff233064c
Patch0:		%{name}-optflags.patch
URL:		http://lingucomponent.openoffice.org/thesaurus.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MyThes is a simple thesaurus that uses a structured text data file and
an index file with binary search to lookup words and phrases and
return information on part of speech, meanings, and synonyms

MyThes was written to provide a thesaurus for the OpenOffice.org
project

%prep
%setup -q -n MyThes-%{version}
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcflags}"

%check
./example th_en_US_new.idx th_en_US_new.dat checkme.lst

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README data_layout.txt
