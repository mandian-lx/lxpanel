Summary:	Lightweight X11 desktop panel based on fbpanel
Name:	  	lxpanel
Version:	0.5.10
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	%{name}-%{version}.tar.gz
Source1:	volume_icon.tar.gz
Source3:	lxpanel-userdirs-config.tar
Patch1:		configure_desktop_number.patch
Patch2:		lxpanel-0.5.10-automake1.12.patch
Patch3:		lxpanel-0.5.10-linkage.patch
Patch4:		lxpanel-0.5.10-string-format-fixes.patch
URL:		http://code.google.com/p/mandriva-lxde
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
# required for netstatus plugin
BuildRequires:  libiw-devel
BuildRequires:  pkgconfig(libwnck-1.0)
BuildRequires:	intltool
BuildRequires:  pkgconfig(libmenu-cache) >= 0.3.0
BuildRequires:	docbook-to-man
BuildRequires:	docbook-dtd412-xml
Requires:	desktop-common-data
Requires:	obconf
Suggests:	pcmanfm
Conflicts:	lxpanelx

%description
LXPanel is a lightweight X11 desktop panel contains:
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

%package	devel
Summary:	Development files for lxpanel
Group:		Graphical desktop/Other

%description	devel
This package contains development files needed for building lxde plugins.

%prep
%setup -q -a1 -a3
%apply_patches
./autogen.sh

%build
%configure2_5x	--with-plugins=all
%make

%install
%makeinstall_std
install -m755 lxpanel-userdirs-config %{buildroot}%{_bindir}

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/lxpanelctl
%{_bindir}/lxpanel-userdirs-config
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
%{_libdir}/%{name}/plugins/thermal.so
%{_libdir}/%{name}/plugins/volumealsa.so
%{_libdir}/%{name}/plugins/xkb.so
%{_libdir}/%{name}/plugins/wnckpager.so
%{_datadir}/%{name}
%{_mandir}/man1/*

%files devel
%{_includedir}/lxpanel
%{_libdir}/pkgconfig/lxpanel.pc
