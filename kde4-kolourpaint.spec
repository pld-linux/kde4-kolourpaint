%define		_state		stable
%define		qtver		4.7.4

Summary:	KDE Painter
Summary(pl.UTF-8):	Program graficzny KDE
Name:		kolourpaint
Version:	4.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	a66e3da8f3f85a5c8b2f4de23b106a6b
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdegraphics-kolourpaint < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A (very) simple painting program for KDE.

%description -l pl.UTF-8
(Bardzo) prosty program do rysowania pod KDE.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolourpaint
%attr(755,root,root) %{_libdir}/libkolourpaint_lgpl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkolourpaint_lgpl.so.?
%{_datadir}/apps/kolourpaint
%{_desktopdir}/kde4/kolourpaint.desktop
%{_iconsdir}/*/*/apps/kolourpaint.*
%{_kdedocdir}/en/kolourpaint
