
Summary:	Object-oriented, cross-platform C++ library handling logic for the Jabber protocol
Summary(pl):	Obiektowa, miêdzyplatformowa biblioteka C++ obs³uguj±ca logikê protoko³u Jabber
Name:		jabberoo
Version:	1.9.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.jabberstudio.org/files/gabber/%{name}-%{version}.tar.gz
# Source0-md5:	8844dc061129c6ffcc5b7968575407ef
URL:		http://gabber.jabberstudio.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsigc++-devel >= 1.2.1
BuildRequires:	libtool >= 2:1.4d
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
