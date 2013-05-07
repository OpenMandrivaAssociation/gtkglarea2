%define api	2.0
%define	major	1
%define	fname	gtkglarea
%define	libname	%mklibname gtkgl %{api} %{major}
%define	devname	%mklibname gtkgl -d
%define	bogus	%mklibname %{fname} 2.0

Summary:	OpenGL widget for GTK+ GUI toolkit
Name:		gtkglarea2
Version:	2.0.1
Release:	9
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.mono-project.com/GtkGLArea
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{fname}-%{version}.tar.bz2
Patch0:		gtkglarea-2.0.0-wformat.patch
Patch1:		gtkglarea-2.0.1-link-against-libm.patch

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
Obsoletes:	%{_lib}gtkglarea2.0_1 < 2.0.1-9
%rename		bogus

%description -n %{libname}
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

%package -n	%{devname}
Summary:	Includes and static libs
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}gtkglarea2.0_1-devel < 2.0.1-9

%description -n	%{devname}
Libraries and includes files you can use for GtkGLArea development

%prep
%setup -qn %{fname}-%{version}
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall

%files -n %{libname}
%{_libdir}/libgtkgl-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog README
%doc docs/*.txt
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/gtkgl-2.0.pc

