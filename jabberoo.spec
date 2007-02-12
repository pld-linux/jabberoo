Summary:	Object-oriented, cross-platform C++ library handling logic for the Jabber protocol
Summary(pl.UTF-8):   Obiektowa, międzyplatformowa biblioteka C++ obsługująca logikę protokołu Jabber
Name:		jabberoo
Version:	1.9.4
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.jabberstudio.org/files/gabber/%{name}-%{version}.tar.gz
# Source0-md5:	453f44a1993f4b2c7f080fc7e0ca7350
URL:		http://gabber.jabberstudio.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsigc++12-devel >= 1.2.1
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object-oriented, cross-platform C++ library which provides handling logic
for the Jabber protocol.

%description -l pl.UTF-8
Obiektowa, międzyplatformowa biblioteka C++, która ułatwia manipulację
protokołem Jabber.

%package devel
Summary:	Jabberoo library development files
Summary(pl.UTF-8):   Pliki programistyczne biblioteki Jabberoo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libsigc++12-devel >= 1.2.1

%description devel
Jabberoo library development files.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki Jabberoo.

%package static
Summary:	Static Jabberoo library
Summary(pl.UTF-8):   Wersja statyczna biblioteki Jabberoo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Jabberoo library.

%description static -l pl.UTF-8
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
