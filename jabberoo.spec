
Summary:	Object-oriented, cross-platform C++ library which provides handling logic for the Jabber protocol
Summary(pl):	Obiektowa, miêdzyplatformowa biblioteka C++, która u³atwia manipulacjê protoko³em Jabber
Name:		jabberoo
Version:	1.9.0.1
Release:	0.1
License:	LGPL
Group:		Libraries
# Source0-md5:	d0933d4585b221739ae9eb0cb09baab5
Source0:	%{name}-%{version}.tar.gz
#Source0:	http://www.jabberstudio.org/projects/gabber/releases/download.php?file=%{name}-%{version}.tar.gz
URL:		http://gabber.jabberstudio.org/
BuildRequires:	libsigc++-devel >= 1.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object-oriented, cross-platform C++ library which provides handling logic
for the Jabber protocol.

%description -l pl
Obiektowa, miêdzyplatformowa biblioteka C++, która u³atwia manipulacjê
protoko³em Jabber.

%package devel
Summary:	Jabberoo library development files
Summary(pl):	Pliki programistyczne biblioteki Jabberoo
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Jabberoo library development files.

%description devel -l pl
Pliki programistyczne biblioteki Jabberoo.

%package static
Summary:	Static Jabberoo library
Summary(pl):	Wersja statyczna biblioteki Jabberoo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Requires:	libsigc++-devel >= 1.2.1

%description static
Static Jabberoo library.

%description static -l pl
Wersja statyczna biblioteki Jabberoo.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

# libjudo uses expat, which is distributed with jabberoo, so install expat.h...
install libjudo/src/expat/expat.h $RPM_BUILD_ROOT%{_includedir}/%{name}

# ... and hack fucking judo.hpp, which should include expat.h distributed with
# jabberoo sources
mv $RPM_BUILD_ROOT%{_includedir}/%{name}/judo.hpp $RPM_BUILD_ROOT%{_includedir}/%{name}/judo.hpp.1
cat $RPM_BUILD_ROOT%{_includedir}/%{name}/judo.hpp.1 \
	| sed 's,^#include <expat.h>,#include "expat.h",' \
	> $RPM_BUILD_ROOT%{_includedir}/%{name}/judo.hpp
rm -f $RPM_BUILD_ROOT%{_includedir}/%{name}/judo.hpp.1 

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
