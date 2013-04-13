%define	major	1
%define api 2.0
%define	fname	gtkglarea
%define	libname	%mklibname %{fname} %{api} %{major}

Summary:	OpenGL widget for GTK+ GUI toolkit
Name:		gtkglarea2
Version:	2.0.1
Release:	8
License:	LGPLv2+
Group:		System/Libraries

Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{fname}-%{version}.tar.bz2
Patch0:		gtkglarea-2.0.0-wformat.patch
Patch1:		gtkglarea-2.0.1-link-against-libm.patch

URL:		http://www.mono-project.com/GtkGLArea
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
%define	bogus	%{mklibname %{fname} 2.0}
%rename		bogus

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
%{_libdir}/libgtkgl-2.0.so.%{major}*

%files -n %{libname}-devel
%doc docs/*.txt
%{_libdir}/*.so
%{_libdir}/*.*a
%{_includedir}/*
%{_libdir}/pkgconfig/gtkgl-2.0.pc


%changelog
* Thu Dec 22 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.0.1-6
+ Revision: 744631
- fix bogus major version
- fix missing linkage against libraries
- use pkgconfig() dependencies
- use %%{EVRD} macro
- drop bogus lib%%{name}-devel
- update project url
- clean out junk and apply cosmetics

* Mon Sep 19 2011 Götz Waschk <waschk@mandriva.org> 2.0.1-5
+ Revision: 700351
- rebuild

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-4
+ Revision: 664951
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-3mdv2011.0
+ Revision: 605509
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-2mdv2010.1
+ Revision: 522809
- rebuilt for 2010.1

* Sat Jul 18 2009 Götz Waschk <waschk@mandriva.org> 2.0.1-1mdv2010.0
+ Revision: 397058
- new version
- fix source URL

  + Christophe Fergeau <cfergeau@mandriva.com>
    - fix -Wformat warnings

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-3mdv2009.1
+ Revision: 301528
- rebuilt against new libxcb

* Mon Aug 25 2008 Götz Waschk <waschk@mandriva.org> 2.0.0-2mdv2009.0
+ Revision: 275667
- fix linking with libX11 and reenable --no-undefined
- move pkgconfig file to the devel package

* Sun Aug 24 2008 Götz Waschk <waschk@mandriva.org> 2.0.0-1mdv2009.0
+ Revision: 275590
- new version
- drop patch
- fix build
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.99.0-11mdv2008.1
+ Revision: 170877
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix mesaglu-devel BR
- fix description

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.99.0-10mdv2008.1
+ Revision: 126425
- kill re-definition of %%buildroot on Pixel's request
- fix summary


* Fri Nov 03 2006 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2006-11-03 08:37:56 (76078)
- run libtoolize/aclocal/automake/autoconf to fix build on x86-64

* Fri Nov 03 2006 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2006-11-03 08:35:08 (76077)
Import gtkglarea2

* Wed Sep 13 2006 Frederic Crozat <fcrozat@mandriva.com> 1.99.0-9mdv2007.0
- Rebuild with new X11 path
- mkrel

* Mon Nov 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.99.0-8mdk
- rebuild

