Summary:	GNOME - Applets
Summary(pl):	GNOME - Applety
Name:		gnome-applets
Version:	1.1.0
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gnome-applets/%{name}-%{version}.tar.gz
Patch:		%{name}-locale.patch
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	ORBit >= 0.4.3
BuildRequires:	audiofile-devel >= 0.1.5
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	guile-devel >= 1.3
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel >= 5.0
URL:		http://www.gnome.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_applnkdir	%{_datadir}/applnk

%description
GNOME Applets.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Applety pod GNOME.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.gz ChangeLog.gz NEWS.gz README.gz

%dir %{_libdir}/gumma
%dir %{_datadir}/asclock
%dir %{_datadir}/bug-applet
%dir %{_datadir}/clockmail
%dir %{_datadir}/geyes
%dir %{_datadir}/gnome
%dir %{_datadir}/gweather
%dir %{_datadir}/odometer
%dir %{_datadir}/pixmaps/gkb
%dir %{_datadir}/pixmaps/gweather
%dir %{_datadir}/pixmaps/mini-commander
%dir %{_datadir}/sound-monitor
%dir %{_datadir}/tickastat

%{_sysconfdir}/CORBA/servers/*

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gumma/*.so*

%{_libdir}/gumma/*.a
%{_libdir}/gumma/*.la

%{_datadir}/applets/*
%{_datadir}/asclock/*
%{_datadir}/bug-applet/*
%{_datadir}/clockmail/*
%{_datadir}/geyes/*
%{_datadir}/gnome/*
%{_datadir}/gweather/*
%{_datadir}/odometer/*
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/*.xpm
%{_datadir}/pixmaps/gweather/*
%{_datadir}/pixmaps/mini-commander/*

%lang(at) %{_datadir}/pixmaps/gkb/at.xpm
%lang(be) %{_datadir}/pixmaps/gkb/be.xpm
%lang(bg) %{_datadir}/pixmaps/gkb/bg.xpm
%lang(br) %{_datadir}/pixmaps/gkb/br.xpm
%lang(ca) %{_datadir}/pixmaps/gkb/ca.xpm
%lang(ch) %{_datadir}/pixmaps/gkb/ch.xpm
%lang(cz) %{_datadir}/pixmaps/gkb/cz.xpm
%lang(de) %{_datadir}/pixmaps/gkb/de.xpm
%lang(dk) %{_datadir}/pixmaps/gkb/dk.xpm
%lang(ee) %{_datadir}/pixmaps/gkb/ee.xpm
%lang(es) %{_datadir}/pixmaps/gkb/es.xpm
%lang(fi) %{_datadir}/pixmaps/gkb/fi.xpm
%lang(fr) %{_datadir}/pixmaps/gkb/fr.xpm
%lang(gb) %{_datadir}/pixmaps/gkb/gb.xpm
%lang(gr) %{_datadir}/pixmaps/gkb/gr.xpm
%lang(hu) %{_datadir}/pixmaps/gkb/hu.xpm
%lang(il) %{_datadir}/pixmaps/gkb/il.xpm
%lang(is) %{_datadir}/pixmaps/gkb/is.xpm
%lang(it) %{_datadir}/pixmaps/gkb/it.xpm
%lang(jp) %{_datadir}/pixmaps/gkb/jp.xpm
%lang(mx) %{_datadir}/pixmaps/gkb/mx.xpm
%lang(nl) %{_datadir}/pixmaps/gkb/nl.xpm
%lang(no) %{_datadir}/pixmaps/gkb/no.xpm
%lang(pl) %{_datadir}/pixmaps/gkb/pl.xpm
%lang(pt) %{_datadir}/pixmaps/gkb/pt.xpm
%lang(qc) %{_datadir}/pixmaps/gkb/qc.xpm
%lang(ru) %{_datadir}/pixmaps/gkb/ru.xpm
%lang(se) %{_datadir}/pixmaps/gkb/se.xpm
%lang(si) %{_datadir}/pixmaps/gkb/si.xpm
%lang(sk) %{_datadir}/pixmaps/gkb/sk.xpm
%lang(th) %{_datadir}/pixmaps/gkb/th.xpm
%lang(tr) %{_datadir}/pixmaps/gkb/tr.xpm
%lang(un) %{_datadir}/pixmaps/gkb/un.xpm
%lang(us) %{_datadir}/pixmaps/gkb/us.xpm
%lang(uy) %{_datadir}/pixmaps/gkb/uy.xpm
%lang(yu) %{_datadir}/pixmaps/gkb/yu.xpm

%{_datadir}/sound-monitor/*
%{_datadir}/tickastat/*

%{_datadir}/xmodmap/xmodmap.dvorak
%lang(be) %{_datadir}/xmodmap/xmodmap.be
%lang(bg) %{_datadir}/xmodmap/xmodmap.bg
%lang(ch) %{_datadir}/xmodmap/xmodmap.ch
%lang(cz) %{_datadir}/xmodmap/xmodmap.cz
%lang(de) %{_datadir}/xmodmap/xmodmap.de
%lang(dk) %{_datadir}/xmodmap/xmodmap.dk
%lang(ee) %{_datadir}/xmodmap/xmodmap.ee
%lang(es) %{_datadir}/xmodmap/xmodmap.es
%lang(fi) %{_datadir}/xmodmap/xmodmap.fi
%lang(fr) %{_datadir}/xmodmap/xmodmap.fr*
%lang(hu) %{_datadir}/xmodmap/xmodmap.hu*
%lang(gr) %{_datadir}/xmodmap/xmodmap.gr
%lang(il) %{_datadir}/xmodmap/xmodmap.il
%lang(is) %{_datadir}/xmodmap/xmodmap.is
%lang(it) %{_datadir}/xmodmap/xmodmap.it
%lang(la) %{_datadir}/xmodmap/xmodmap.la
%lang(nl) %{_datadir}/xmodmap/xmodmap.nl
%lang(no) %{_datadir}/xmodmap/xmodmap.no
%lang(pl) %{_datadir}/xmodmap/xmodmap.pl
%lang(pt) %{_datadir}/xmodmap/xmodmap.pt*
%lang(qc) %{_datadir}/xmodmap/xmodmap.qc
%lang(ru) %{_datadir}/xmodmap/xmodmap.ru*
%lang(se) %{_datadir}/xmodmap/xmodmap.se
%lang(sf) %{_datadir}/xmodmap/xmodmap.sf
%lang(sg) %{_datadir}/xmodmap/xmodmap.sg
%lang(si) %{_datadir}/xmodmap/xmodmap.si
%lang(sk) %{_datadir}/xmodmap/xmodmap.sk
%lang(th) %{_datadir}/xmodmap/xmodmap.th
%lang(tr) %{_datadir}/xmodmap/xmodmap.tr*
%lang(uk) %{_datadir}/xmodmap/xmodmap.uk
%lang(us) %{_datadir}/xmodmap/xmodmap.us*
%lang(yu) %{_datadir}/xmodmap/xmodmap.yu
