%define		_state		stable
%define		orgname		kolourpaint
%define		qtver		4.8.1

Summary:	KDE Painter
Summary(pl.UTF-8):	Program graficzny KDE
Name:		kde4-kolourpaint
Version:	4.12.4
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	2bdeba37745b84e90ee6474893617a5e
URL:		http://www.kde.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qimageblitz-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegraphics-kolourpaint < 4.6.99
Obsoletes:	kolourpaint <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A (very) simple painting program for KDE.

%description -l pl.UTF-8
(Bardzo) prosty program do rysowania pod KDE.

%prep
%setup -q -n %{orgname}-%{version}

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
