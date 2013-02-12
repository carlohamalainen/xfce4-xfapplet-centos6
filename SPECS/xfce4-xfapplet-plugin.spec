Name:           xfce4-xfapplet-plugin
Version:        0.1.0
Release:        15%{?dist}
Summary:        A plugin to use gnome-panel based applets inside the Xfce4 panel

Group:          User Interface/Desktops
License:        GPL
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  xfce4-panel-devel >= 4.3.20, libxfcegui4-devel >= 4.2.0
BuildRequires:  libxml2-devel, gettext, perl(XML::Parser)
BuildRequires:  gnome-panel-devel >= 2.0.0
BuildRequires:  glib2-devel, gtk2, gtk2-devel, ORBit2, ORBit2-devel,
BuildRequires:  libpanelappletmm, libpanelappletmm-devel,
BuildRequires:  xfce4-panel-devel, libxfcegui4, libxfcegui4-devel
Requires:       xfce4-panel >= 4.3.99.2, gnome-applets

%description
The XfApplet Plugin is a plugin for the Xfce 4 Panel which allows one to use 
applets designed for the Gnome Panel inside the Xfce Panel. You can think of 
XfApplet as a tiny Gnome Panel that lives inside the Xfce Panel and allows 
you to show the same applets that the Gnome Panel is capable of showing.

%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libexecdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/pixmaps/xfapplet*.svg
%{_datadir}/%{name}


%changelog
* Tue Feb 12 2013 Carlo Hamalainen <carlo.hamalainen@gmail.com> - 0.1.0-2
- Patched to build on Centos 6.3.
* Sat Sep 23 2006 Christoph Wickert <fedora christoph-wickert de> - 0.1.0-1
- Initial Fedora Extras version.
