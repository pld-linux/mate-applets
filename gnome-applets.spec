Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	Aplety GNOME - ma�e aplikacje osadzaj�ce si� w panelu
Summary(ru):	��������� ���������, �������������� � ������ GNOME
Summary(uk):	������˦ ��������, �� ������������ � ������ GNOME
Name:		gnome-applets
Version:	2.3.5
Release:	1
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	48b5b003ebf2cfb7d352bb40f69f140d
Patch0:		%{name}-xmldocs.patch
Patch1:		%{name}-docs.patch
Patch2:		%{name}-gkb_de_fix.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel >= 1.3.0
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-panel-devel >= 2.3.0
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool >= 0.23
BuildRequires:	libgnome-devel >= 2.3.0
BuildRequires:	libgnomecanvas-devel >= 2.3.0
BuildRequires:	libgnomeui-devel >= 2.3.0
BuildRequires:	libglade2-devel >= 2.0.1-2
BuildRequires:	libgtop-devel >= 2.0.0
BuildRequires:	libwnck-devel >= 2.3.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.1
BuildRequires:	scrollkeeper >= 0.3.11-4
Requires:	gnome-vfs2 >= 2.2.0
Requires(post):	GConf2 >= 2.3.0
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnotes_applet

%define		_localstatedir	/var

%description
The gnome-applets package provides Panel applets which enhance your
GNOME experience.

%description -l pl
Pakiet gnome-applets udost�pnia aplety Panelu, kt�re usprawniaj� prac�
z GNOME.

%description -l uk
����� gnome-applets ͦ����� ������ ����̦ GNOME, �� �¦�������
�������Φ��� ������ � ��������ݦ GNOME.

%description -l ru
����� gnome-applets �������� ������� ������ GNOME, �������������
������������ ������ � ����� GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
intltoolize --copy --force
%{__libtoolize}
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --all-name

find $RPM_BUILD_ROOT/%{_pixmapsdir}/gkb/|grep '/..\.png$'|sed "s=$RPM_BUILD_ROOT\(/%{_pixmapsdir}/gkb/\)\(..\)\(.png\)=%lang(\2) \1\2\3=" >> %{name}.lang
find . 	-name ChangeLog -o \
	-name TODO -o \
	-name NEWS -o \
	-name AUTHORS \
	-o -name README | \
awk '{src=$0; dst=$0;sub("^./","",dst);gsub("/","-",dst); 
	print "cp " src " " dst}  END {print "exit 0"}' | sh


%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" %{_libdir}/%{name}/mc-install-default-macros

%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *AUTHORS *ChangeLog *NEWS *README *TODO
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/sound/events/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/accessx-status-applet
%attr(755,root,root) %{_libdir}/battstat-applet-2
%attr(755,root,root) %{_libdir}/cdplayer_applet2
%attr(755,root,root) %{_libdir}/charpick_applet2
%attr(755,root,root) %{_libdir}/drivemount_applet2
%attr(755,root,root) %{_libdir}/geyes_applet2
%attr(755,root,root) %{_libdir}/gkb-applet-2
%attr(755,root,root) %{_libdir}/gtik2_applet2
%attr(755,root,root) %{_libdir}/gweather-applet-2
%attr(755,root,root) %{_libdir}/mailcheck-applet
%attr(755,root,root) %{_libdir}/mini_commander_applet
%attr(755,root,root) %{_libdir}/mixer_applet2
%attr(755,root,root) %{_libdir}/modemlights_applet2
%attr(755,root,root) %{_libdir}/multiload-applet-2
%attr(755,root,root) %{_libdir}/stickynotes_applet
%attr(755,root,root) %{_libdir}/wireless-applet
%attr(755,root,root) %{_libdir}/%{name}
%{_libdir}/bonobo/servers/*
%{_datadir}/battstat_applet
%{_datadir}/geyes
%{_datadir}/gnome/gkb/presets.xml
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/gen_util/*.glade
%{_datadir}/stickynotes
%{_datadir}/wireless-applet/*.glade
%{_pixmapsdir}/accessx-status-applet
%{_pixmapsdir}/gweather
%{_pixmapsdir}/mailcheck
%{_pixmapsdir}/mini-commander
%{_pixmapsdir}/mixer
%{_pixmapsdir}/stickynotes
%{_pixmapsdir}/wireless-applet
%{_pixmapsdir}/*.png
%{_omf_dest_dir}/%{name}

%dir %{_datadir}/gnome/gkb
%{_datadir}/gnome/gkb/Dvorak.keyprop
%{_datadir}/gnome/gkb/Default.keyprop
%lang(am) %{_datadir}/gnome/gkb/AM_Armenian.keyprop
%lang(ar) %{_datadir}/gnome/gkb/AR_*
%lang(am) %{_datadir}/gnome/gkb/Armenian.keyprop
%lang(az) %{_datadir}/gnome/gkb/AZ_Azerbaidjani_Turkic.keyprop
%lang(eu) %{_datadir}/gnome/gkb/Basque.keyprop
%lang(be) %{_datadir}/gnome/gkb/BE_Dutch.keyprop
%lang(be) %{_datadir}/gnome/gkb/Belgian.keyprop
%lang(bg) %{_datadir}/gnome/gkb/BG_*
%lang(br) %{_datadir}/gnome/gkb/BR_*
%lang(bg) %{_datadir}/gnome/gkb/BulgarianCyril.keyprop
%lang(by) %{_datadir}/gnome/gkb/BY_Belarussian.keyprop
%lang(ca) %{_datadir}/gnome/gkb/CA_English.keyprop
%lang(ch) %{_datadir}/gnome/gkb/CH_German_x.keyprop
%lang(cz) %{_datadir}/gnome/gkb/CZ_Czech.keyprop
%lang(cz) %{_datadir}/gnome/gkb/CZ_Czech_x.keyprop
%lang(cz,sk) %{_datadir}/gnome/gkb/CZ_Czech_Slovak.keyprop
%lang(de) %{_datadir}/gnome/gkb/DE_*
%lang(dk) %{_datadir}/gnome/gkb/DK_*
%lang(ee) %{_datadir}/gnome/gkb/EE_*
%lang(es) %{_datadir}/gnome/gkb/ES_*
%lang(fi) %{_datadir}/gnome/gkb/FI_*
%lang(ch) %{_datadir}/gnome/gkb/FrenchCanadian2.keyprop
%lang(qc) %{_datadir}/gnome/gkb/FrenchCanadian.keyprop
%lang(ch) %{_datadir}/gnome/gkb/FrenchSwiss.keyprop
%lang(fr) %{_datadir}/gnome/gkb/FR_*
%lang(ge) %{_datadir}/gnome/gkb/GE_Georgian_x.keyprop
%lang(ge-la) %{_datadir}/gnome/gkb/GeorgianLatin.keyprop
%lang(de,at,ch) %{_datadir}/gnome/gkb/German.keyprop
%lang(ch) %{_datadir}/gnome/gkb/GermanSwiss.keyprop
%lang(gr) %{_datadir}/gnome/gkb/GR_*
%lang(hr) %{_datadir}/gnome/gkb/HR_*
%lang(hu) %{_datadir}/gnome/gkb/HU_*
%lang(hu) %{_datadir}/gnome/gkb/Hungarian*
%lang(il) %{_datadir}/gnome/gkb/IL_*
%lang(is) %{_datadir}/gnome/gkb/IS_*
%lang(it) %{_datadir}/gnome/gkb/IT_*
%lang(jp) %{_datadir}/gnome/gkb/JP_*
%lang(kr) %{_datadir}/gnome/gkb/KR_Korean.keyprop
%lang(la) %{_datadir}/gnome/gkb/LA_Lao_x.keyprop
%lang(lt) %{_datadir}/gnome/gkb/LT_*
%lang(mk) %{_datadir}/gnome/gkb/M*acedonian.keyprop
%lang(mn) %{_datadir}/gnome/gkb/MN_Mongolian*.keyprop
%lang(nl) %{_datadir}/gnome/gkb/NL_Dutch_x.keyprop
%lang(no) %{_datadir}/gnome/gkb/NO_Norwegian.keyprop
%lang(no) %{_datadir}/gnome/gkb/Norwegian.keyprop
%lang(pl) %{_datadir}/gnome/gkb/*olish*
%lang(pt) %{_datadir}/gnome/gkb/Portug*
%lang(pt) %{_datadir}/gnome/gkb/PT_*
%lang(ro) %{_datadir}/gnome/gkb/RO_Romanian.keyprop
%lang(ru) %{_datadir}/gnome/gkb/*Russian*
%lang(se) %{_datadir}/gnome/gkb/SE_Swedish*.keyprop
%lang(si) %{_datadir}/gnome/gkb/SI_Slovenian*.keyprop
%lang(sk) %{_datadir}/gnome/gkb/Slovak.keyprop
%lang(si) %{_datadir}/gnome/gkb/Sloven*.keyprop
%lang(yu) %{_datadir}/gnome/gkb/SR_Dutch.keyprop
%lang(sv) %{_datadir}/gnome/gkb/Swedish.keyprop
# is (sy) really exist?
%lang(sy) %{_datadir}/gnome/gkb/Syriac*.keyprop
%lang(th) %{_datadir}/gnome/gkb/Thai2.keyprop
%lang(th) %{_datadir}/gnome/gkb/Thai.keyprop
%lang(th) %{_datadir}/gnome/gkb/TH_Thai.keyprop
%lang(th) %{_datadir}/gnome/gkb/TH_Thai_x.keyprop
%lang(tr) %{_datadir}/gnome/gkb/TR*
%lang(ua) %{_datadir}/gnome/gkb/UA_Ukrainian.keyprop
%lang(uk) %{_datadir}/gnome/gkb/UK*
%lang(us) %{_datadir}/gnome/gkb/US*
%lang(vn) %{_datadir}/gnome/gkb/VN_Vietnamese.keyprop
%lang(yu) %{_datadir}/gnome/gkb/Yugoslav.keyprop
%lang(yu) %{_datadir}/gnome/gkb/YU_Serb*.keyprop

%dir %{_pixmapsdir}/gkb
%{_pixmapsdir}/gkb/gkb.png
%{_pixmapsdir}/gkb/lam.png

%dir %{_datadir}/xmodmap
%lang(am) %{_datadir}/xmodmap/xmodmap.am*
%lang(ar) %{_datadir}/xmodmap/xmodmap.ar*
%lang(be) %{_datadir}/xmodmap/xmodmap.be*
%lang(bg) %{_datadir}/xmodmap/xmodmap.bg*
%lang(br) %{_datadir}/xmodmap/xmodmap.br*
%lang(ch) %{_datadir}/xmodmap/xmodmap.ch*
%lang(cz) %{_datadir}/xmodmap/xmodmap.cz*
%lang(de) %{_datadir}/xmodmap/xmodmap.de*
%lang(dk) %{_datadir}/xmodmap/xmodmap.dk*
%{_datadir}/xmodmap/xmodmap.dvorak
%lang(ee) %{_datadir}/xmodmap/xmodmap.ee*
%lang(es) %{_datadir}/xmodmap/xmodmap.es*
%lang(fi) %{_datadir}/xmodmap/xmodmap.fi*
%lang(fr) %{_datadir}/xmodmap/xmodmap.fr*
%lang(gb) %{_datadir}/xmodmap/xmodmap.gb*
%lang(ge) %{_datadir}/xmodmap/xmodmap.ge*
%lang(gr) %{_datadir}/xmodmap/xmodmap.gr*
%lang(hu) %{_datadir}/xmodmap/xmodmap.hu*
%lang(il) %{_datadir}/xmodmap/xmodmap.il*
%lang(is) %{_datadir}/xmodmap/xmodmap.is*
%lang(it) %{_datadir}/xmodmap/xmodmap.it*
%lang(jp) %{_datadir}/xmodmap/xmodmap.jp*
%lang(kr) %{_datadir}/xmodmap/xmodmap.kr*
%lang(la) %{_datadir}/xmodmap/xmodmap.la*
%lang(lt) %{_datadir}/xmodmap/xmodmap.lt*
%lang(mk) %{_datadir}/xmodmap/xmodmap.mk*
%lang(mn) %{_datadir}/xmodmap/xmodmap.mn*
%lang(nl) %{_datadir}/xmodmap/xmodmap.nl*
%lang(no) %{_datadir}/xmodmap/xmodmap.no*
%lang(pl) %{_datadir}/xmodmap/xmodmap.pl*
%lang(pt) %{_datadir}/xmodmap/xmodmap.pt*
%lang(qc) %{_datadir}/xmodmap/xmodmap.qc*
%lang(ro) %{_datadir}/xmodmap/xmodmap.ro*
%lang(ru) %{_datadir}/xmodmap/xmodmap.ru*
%lang(se) %{_datadir}/xmodmap/xmodmap.se*
%lang(sf) %{_datadir}/xmodmap/xmodmap.sf*
%lang(sg) %{_datadir}/xmodmap/xmodmap.sg*
%lang(si) %{_datadir}/xmodmap/xmodmap.si*
%lang(sk) %{_datadir}/xmodmap/xmodmap.sk*
%lang(th) %{_datadir}/xmodmap/xmodmap.th*
%lang(tr) %{_datadir}/xmodmap/xmodmap.tr*
%lang(uk) %{_datadir}/xmodmap/xmodmap.uk*
%lang(us) %{_datadir}/xmodmap/xmodmap.us*
%lang(yu) %{_datadir}/xmodmap/xmodmap.yu*
