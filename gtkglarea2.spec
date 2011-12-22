%define	major	2.0

%define	fname	gtkglarea
%define	libname	%mklibname %fname %{major}

Summary:	OpenGL widget for GTK+ GUI toolkit
Name:		gtkglarea2
Version:	2.0.1
Release: 	6
License:	LGPLv2+
Group:		System/Libraries

Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{fname}-%{version}.tar.bz2
Patch0:		gtkglarea-2.0.0-wformat.patch
Patch1:		gtkglarea-2.0.1-link-against-libm.patch

URL:		http://www.mono-project.com/GtkGLArea
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

%package -n	%{libname}
Summary:	OpenGL widget for GTK+ GUI toolkit
Group:		System/Libraries

%description -n %{libname}
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

%package -n	%{libname}-devel
Summary:	Includes and static libs
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{libname}-devel
Libraries and includes files you can use for GtkGLArea development

%prep
%setup -q -n %{fname}-%{version}
%patch0 -p1 -b .wformat~
%patch1 -p1 -b .libs~
autoreconf -fi

%build
%configure2_5x 
%make

%install
%makeinstall

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libgtkgl-%{major}.so.1*

%files -n %{libname}-devel
%doc docs/*.txt
%{_libdir}/*.so
%{_libdir}/*.*a
%{_includedir}/*
%{_libdir}/pkgconfig/gtkgl-2.0.pc
