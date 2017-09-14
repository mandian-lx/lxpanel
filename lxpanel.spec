%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Lightweight X11 desktop panel based on fbpanel
Name:		lxpanel
Version:	0.9.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://wiki.lxde.org/en/LXPanel
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
#Source1:	volume_icon.tar.gz
#Patch1:	configure_desktop_number.patch
#Patch2:	lxpanel-0.5.12-automake113.patch

BuildRequires:	docbook-to-man
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libfm-gtk)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(keybinder)

Requires:	desktop-common-data
Requires:	obconf

Suggests:	pcmanfm

Conflicts:	lxpanelx

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

LXPanel is the standard panel of LXDE. The desktop panel can generate a menu
for installed applications automatically from *.desktop files. It can be
configured from a GUI preferences dialog, so there is no need to edit config
files.

Soem features:
1. User-friendly application menu automatically generated from *.desktop
   files on the system.
2. Launcher bar (Small icons clicked to launch apps)
3. Task bar supporting urgency hint (Can flash when gaim gets new
   incoming messages)
4. Notification area (System tray)
5. Digital clock
6. Run dialog (A dialog let you type a command and run, can be called in
   external programs)
7. Volume control plug-in (optional, written by jserv)
8. lxpanelctl, an external controller let you control lxpanel in other
   programs.

This version based on lxpanelx 0.6.0 alpha version

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/lxpanelctl
%dir %{_sysconfdir}/xdg/%{name}
%{_sysconfdir}/xdg/%{name}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/batt.so
%{_libdir}/%{name}/plugins/cpu.so
%{_libdir}/%{name}/plugins/cpufreq.so
%{_libdir}/%{name}/plugins/deskno.so
%{_libdir}/%{name}/plugins/kbled.so
%{_libdir}/%{name}/plugins/monitors.so
%{_libdir}/%{name}/plugins/netstat.so
%{_libdir}/%{name}/plugins/netstatus.so
%{_libdir}/%{name}/plugins/volume.so
%{_libdir}/%{name}/plugins/xkb.so
%{_libdir}/%{name}/plugins/thermal.so
%{_libdir}/%{name}/plugins/weather.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Lxpanel shared library
Group:		Graphical desktop/Other
Requires:	%{name} = %{version}

%description -n %{libname}
Shared library for Lxpanel.

%files -n %{libname}
%{_libdir}/%{name}/lib%{name}.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for lxpanel
Group:		Graphical desktop/Other
Requires:	%{libname} = %{version}

%description -n %{devname}
This package contains development files needed for building lxde plugins.

%files -n %{devname}
%{_includedir}/lxpanel
%{_libdir}/pkgconfig/lxpanel.pc
%{_libdir}/%{name}/lib%{name}.so

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
#/autogen.sh
#export CC=gcc
%configure
# \
#	--enable-man \
#	--with-plugins="cpu batt kbled xkb thermal deskno volumealsa"
%make

%install
%makeinstall_std

# locales
%find_lang %{name}

