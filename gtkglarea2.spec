%define major 2.0

%define fname gtkglarea
%define libname_orig lib%{fname}
%define libname %mklibname %fname %{major}

Summary:	OpenGL widget for GTK+ GUI toolkit
Name:		gtkglarea2
Version:	2.0.1
Release: 	%mkrel 3
License:	LGPLv2+
Group:		System/Libraries

Source:		http://ftp.gnome.org/pub/GNOME/sources/%name/%{fname}-%{version}.tar.bz2
Patch0:		gtkglarea-2.0.0-wformat.patch

BuildRoot:	%_tmppath/%name-%version-%release-root
URL:		http://www.student.oulu.fi/~jlof/gtkglarea/
BuildRequires:	mesaglu-devel
BuildRequires:	gtk+2-devel

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

%package -n %{libname}
Summary:        OpenGL widget for GTK+ GUI toolkit
Group:          System/Libraries

%description -n %{libname}
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

%package -n %{libname}-devel
Summary: Includes and static libs
Group: Development/GNOME and GTK+
Requires: %{libname} >= %{version}
Provides: %{libname_orig}-devel = %{version}-%{release} %{name}-devel = %{version}-%{release} 

%description -n %{libname}-devel
Libraries and includes files you can use for GtkGLArea development

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %fname-%version
%patch0 -p1 -b .wformat

%build
%configure2_5x 
%make LIBS=-lX11

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libgtkgl-%major.so.1*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc docs/*.txt
%{_libdir}/*.so
%{_libdir}/*.*a
%{_includedir}/*
%_libdir/pkgconfig/gtkgl-2.0.pc

