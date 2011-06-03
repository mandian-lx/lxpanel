%define int_name lxpanel
Summary:	Lightweight X11 desktop panel based on fbpanel
Name:	  	%int_name
Version:	0.5.6
Release:	%mkrel 7
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	%int_name-%version.tar.gz
Patch0:		lxpanel-0.5.0-customization.patch
#Patch3:		batt_status.patch
Patch4:		configure_desktop_number.patch
Patch7:		lxpanel-0.5.4-drop-cpu-freq.patch
#Patch8:		missing_glades.patch
#Patch9:		redefine-alarm-variable.patch
Patch10:	lxpanel-icons.patch

URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel libalsa-devel intltool
BuildRequires:	menu-cache-devel >= 0.2.1
BuildRequires:	docbook-to-man libwnck-1-devel docbook-dtd412-xml
Requires:	desktop-common-data obconf
Suggests:	pcmanfm
Obsoletes:	%int_name

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
%setup -q -n %int_name-%version
%patch0 -p1
#patch3 -p1
%patch4 -p1
%patch7 -p0
#patch8 -p1
#patch9 -p1
%patch10 -p1

%build
./autogen.sh
%configure \
  --with-plugins="wnckpager monitors volumealsa cpu deskno batt kbled xkb thermal"
  
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{int_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{int_name}.lang
%defattr(-, root, root)
%{_bindir}/%{int_name}
%{_bindir}/lxpanelctl
%dir %{_libdir}/%int_name
%dir %{_libdir}/%{int_name}/plugins
%{_libdir}/%{int_name}/plugins/batt.so
%{_libdir}/%{int_name}/plugins/cpu.so
#{_libdir}/%{name}/plugins/cpufreq.so
%{_libdir}/%{int_name}/plugins/deskno.so
%{_libdir}/%{int_name}/plugins/kbled.so
%{_libdir}/%{int_name}/plugins/volumealsa.so
%{_libdir}/%{int_name}/plugins/xkb.so
%{_libdir}/%{int_name}/plugins/thermal.so
%{_libdir}/%{int_name}/plugins/monitors.so
%{_libdir}/%{int_name}/plugins/wnckpager.so
%{_datadir}/%int_name
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/lxpanel
%{_libdir}/pkgconfig/lxpanel.pc

