Summary:	Lightweight X11 desktop panel based on fbpanel
Name:	  	lxpanel
Version:	0.5.5
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Patch0:		lxpanel-0.5.0-customization.patch
Patch2:		lxpanel-0.5.4-drop-cpu-freq.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel libalsa-devel intltool
BuildRequires:	menu-cache-devel >= 0.2.1
BuildRequires:	docbook-to-man
Requires:	desktop-common-data
Suggests:	pcmanfm

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

%package devel
Summary: Development files for lxpanel
Group: Graphical desktop/Other

%description devel
This package contains development files needed for building lxde plugins.

%prep
%setup -q -n %name-%version
%patch0 -p1

%build
./autogen.sh
%configure2_5x \
  --with-plugins="volumealsa cpu deskno batt kbled xkb thermal cpufreq"
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%{name}
%{_bindir}/lxpanelctl
%dir %{_libdir}/%name
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/batt.so
%{_libdir}/%{name}/plugins/cpu.so
%{_libdir}/%{name}/plugins/cpufreq.so
%{_libdir}/%{name}/plugins/deskno.so
%{_libdir}/%{name}/plugins/kbled.so
%{_libdir}/%{name}/plugins/volumealsa.so
%{_libdir}/%{name}/plugins/xkb.so
%{_libdir}/%{name}/plugins/thermal.so
%{_datadir}/%name
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/lxpanel
%{_libdir}/pkgconfig/lxpanel.pc

