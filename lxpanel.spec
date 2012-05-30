Summary:	Lightweight X11 desktop panel based on fbpanel
Name:	  	lxpanel
Version:	0.5.9
Release:	%mkrel 7
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	%name-%version.tar.bz2
Source1:	volume_icon.tar.gz
Source3:	lxpanel-userdirs-config.tar
Patch1:		configure_desktop_number.patch
Patch2:		lxpanel-0.5.9-automake1.12.patch

URL:		http://code.google.com/p/mandriva-lxde
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel libalsa-devel intltool
BuildRequires:	menu-cache-devel >= 0.2.1
BuildRequires:	docbook-to-man docbook-dtd412-xml
BuildRequires:	gdk-pixbuf-xlib
Requires:	desktop-common-data obconf
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

%package devel
Summary: Development files for lxpanel
Group: Graphical desktop/Other

%description devel
This package contains development files needed for building lxde plugins.

%prep
%setup -q -n %name-%version -a1 -a3
%apply_patches

%build
./autogen.sh
%configure2_5x \
  --with-plugins="volumealsa cpu deskno batt kbled xkb thermal"
  
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -m 0755 lxpanel-userdirs-config %{buildroot}%{_bindir}

%{find_lang} %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/lxpanelctl
%{_bindir}/lxpanel-userdirs-config
%dir %{_libdir}/%name
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/batt.so
%{_libdir}/%{name}/plugins/cpu.so
#{_libdir}/%{name}/plugins/cpufreq.so
%{_libdir}/%{name}/plugins/deskno.so
%{_libdir}/%{name}/plugins/kbled.so
%{_libdir}/%{name}/plugins/volumealsa.so
%{_libdir}/%{name}/plugins/xkb.so
%{_libdir}/%{name}/plugins/thermal.so
%{_datadir}/%name
%{_mandir}/man1/*
%{_libdir}/%{name}/iface-info

%files devel
%defattr(-, root, root)
%{_includedir}/lxpanel
%{_libdir}/pkgconfig/lxpanel.pc



%changelog
* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.8-2mdv2011.0
+ Revision: 693012
- update to 0.5.8. Drop impliment patches

* Sat Jun 18 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.6-11
+ Revision: 685957
- clean spec and add confilct with lxpanel fork

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.6-10
+ Revision: 684681
- sync customization patch

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.6-9
+ Revision: 684429
+ rebuild (emptylog)

* Fri Jun 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.6-8
+ Revision: 682694
+ rebuild (emptylog)

* Fri Jun 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.6-7
+ Revision: 682591
- revert changes due stability

* Thu Jun 02 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.6-6
+ Revision: 682515
- update language and fix errors from svn

* Fri May 06 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.6-5
+ Revision: 669780
+ rebuild (emptylog)

* Wed May 04 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.6-4
+ Revision: 666979
-add volume icons, clock and wnckplugin patch

* Sun May 01 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.6-3
+ Revision: 661286
-add patch for plugin (desktop, batt), icons_resize and glade errors

  + Funda Wang <fwang@mandriva.org>
    - new version 0.5.6

* Sun Feb 28 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.5-2mdv2010.1
+ Revision: 512522
- rebuild for new menu-cache

* Wed Feb 17 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.5-1mdv2010.1
+ Revision: 507084
- drop patch 5 not needed any more (too)
- new upstream release 0.5.5
- drop patch 10, not needed any more

* Mon Dec 14 2009 Funda Wang <fwang@mandriva.org> 0.5.4.1-1mdv2010.1
+ Revision: 478427
- new version 0.5.4.1

* Fri Dec 11 2009 Funda Wang <fwang@mandriva.org> 0.5.4-1mdv2010.1
+ Revision: 476270
- fix build
- new versino 0.5.4

* Sun Sep 27 2009 Funda Wang <fwang@mandriva.org> 0.5.3-2mdv2010.0
+ Revision: 449693
- use mandriva star

* Sun Aug 09 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.3-1mdv2010.0
+ Revision: 413466
- update to new version 0.5.3

* Sat Aug 08 2009 Funda Wang <fwang@mandriva.org> 0.5.2-1mdv2010.0
+ Revision: 411581
- new version 0.5.2

* Wed Aug 05 2009 Funda Wang <fwang@mandriva.org> 0.5.1-1mdv2010.0
+ Revision: 409927
- new version 0.5.1

* Fri Jul 31 2009 Funda Wang <fwang@mandriva.org> 0.5.0-1mdv2010.0
+ Revision: 405105
- new version 0.5.0

* Tue May 05 2009 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2010.0
+ Revision: 372056
- New version 0.4.1

* Tue Apr 21 2009 Funda Wang <fwang@mandriva.org> 0.4.0-1mdv2009.1
+ Revision: 368477
- New version 0.4.0

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 0.3.999-2.1296.2mdv2009.1
+ Revision: 364427
- use lxterminal as its native terminal

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 0.3.999-2.1296.1mdv2009.1
+ Revision: 364376
- use upstream svn snapshot to fix various small bugs

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 0.3.999-1mdv2009.1
+ Revision: 333764
- New versino 0.3.999

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 0.3.99-1mdv2009.1
+ Revision: 312649
- bump BR of menu-cache
- drop old patches
- rediff customization patch
- use mandirva main menu rather than lxde's own menu
- New version 0.3.99
- drop upstream patches

* Sun Nov 02 2008 Olivier Blin <blino@mandriva.org> 0.3.8.1-4mdv2009.1
+ Revision: 299288
- fix icon for Education section (using Gnome's applications-science icon)
- request 16x16 icons for menu (from upstream SVN)

* Thu Oct 16 2008 Olivier Blin <blino@mandriva.org> 0.3.8.1-3mdv2009.1
+ Revision: 294178
- do not drop icon extension, this breaks ooo-writer3.0
  (and XDG spec already forbids extension for non-absolute paths)
- fix support of Logout command in config file
- fix memory corruption in menu parsing (patch likely from Ander)

* Sun Sep 28 2008 Funda Wang <fwang@mandriva.org> 0.3.8.1-2mdv2009.0
+ Revision: 289022
- raise patch level

  + Olivier Blin <blino@mandriva.org>
    - suggest pcmanfm, since it's used by default in the launchbar
    - use new path for firefox desktop file in launchbar

* Mon Jul 07 2008 Funda Wang <fwang@mandriva.org> 0.3.8.1-1mdv2009.0
+ Revision: 232481
- update to new version 0.3.8.1

* Thu Jul 03 2008 Funda Wang <fwang@mandriva.org> 0.3.8-1mdv2009.0
+ Revision: 230940
- BR intltool
- update to new version 0.3.8

* Mon Jun 09 2008 Funda Wang <fwang@mandriva.org> 0.3.7-1mdv2009.0
+ Revision: 217103
- There is no need disable ldflags
- drop patch3 , merged upstream
- New version 0.3.7

* Thu May 29 2008 Pascal Terjan <pterjan@mandriva.org> 0.3.6-3mdv2009.0
+ Revision: 213123
- Handle resolution changes

* Wed May 28 2008 Pascal Terjan <pterjan@mandriva.org> 0.3.6-2mdv2009.0
+ Revision: 212790
- Add a few categories for the menu

* Thu May 22 2008 Funda Wang <fwang@mandriva.org> 0.3.6-1mdv2009.0
+ Revision: 209961
- Bring back _disable_ld_no_undefined
- disable netstatus plugin, prefer netstat, as the latter is
  lxde native plugin.
- New version 0.3.6
- drop ld paras, it is not needed any more

* Wed May 21 2008 Pascal Terjan <pterjan@mandriva.org> 0.3.5.4-5mdv2009.0
+ Revision: 209825
- Disable no-undefined, it breaks build of plugins
- Fix windows not getting focus when un-minimized

  + Funda Wang <fwang@mandriva.org>
    - list individual files

* Mon May 05 2008 Funda Wang <fwang@mandriva.org> 0.3.5.4-4mdv2009.0
+ Revision: 201266
- enable all plugins

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.3.5.4-3mdv2009.0
+ Revision: 201128
- use customization too

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.3.5.4-2mdv2009.0
+ Revision: 200886
- BR iw-devel
- BR xpm
- add source and spec
- Created package structure for lxpanel.

