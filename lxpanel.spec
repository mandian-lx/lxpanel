Summary:	Lightweight X11 desktop panel based on fbpanel
Name:	  	lxpanel
Version:	0.3.8.1
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Patch0:		lxpanel-0.3.8.1-customization.patch
Patch1:		lxpanel-0.3.5.4-fix-focus-on-raise.patch
# (pt) X-MandrivaLinux-Network is needed to have skype in the menu on 2008.1
# This patch should rather add all the missing categories (it adds only  2 so far)
# and be sent upstream
Patch2:		lxpanel-0.3.6-additional-categories.patch
# fixes memory corruption in menu parsing 
Patch3:		lxpanel-menu.patch
# (blino) fix support of Logout command in config file
Patch4:		lxpanel-0.3.8.1-logout.patch
# (blino) do not drop icon extension, this breaks ooo-writer3.0
# and XDG spec already forbids extension for non-absolute paths
Patch5:		lxpanel-0.3.8.1-iconext.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel libalsa-devel xpm-devel libiw-devel intltool
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
7. Net status icon plug-in
8. Volume control plug-in (optional, written by jserv)
9. lxpanelctl, an external controller let you control lxpanel in other
   programs.

%prep
%setup -q
%patch0 -p1 -b .customization
%patch1 -p0 -b .raise
%patch2 -p0 -b .cat
%patch3 -p1 -b .menu
%patch4 -p1 -b .logout
%patch5 -p1 -b .iconext

%build
%configure2_5x \
  --with-plugins="netstat volume volumealsa cpu deskno batt kbled xkb"
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
%{_libdir}/%{name}/plugins/deskno.so
%{_libdir}/%{name}/plugins/kbled.so
%{_libdir}/%{name}/plugins/netstat.so
%{_libdir}/%{name}/plugins/volumealsa.so
%{_libdir}/%{name}/plugins/xkb.so
%dir %{_datadir}/%name
%dir %{_datadir}/%name/images
%{_datadir}/%name/images/*.png
%dir %{_datadir}/%name/images/xkb-flags
%{_datadir}/%name/images/xkb-flags/*.png
%dir %{_datadir}/%name/profile
%{_datadir}/%name/profile/default
%dir %{_datadir}/%name/ui
%{_datadir}/%name/ui/panel-pref.glade
%{_mandir}/man1/*
