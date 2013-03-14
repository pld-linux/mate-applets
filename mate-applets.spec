# TODO
# - rename applets (to match applet name vs package name):
#        - charpick
#        - mateweather
#        - invest-applet
#        - trashapplet
# - build:
#        - timer-applet
# - cpufreq applet does not startup
Summary:	Small applications which embed themselves in the MATE panel
Summary(pl.UTF-8):	Aplety MATE - małe aplikacje osadzające się w panelu
Summary(ru.UTF-8):	Маленькие программы, встраивающиеся в панель MATE
Summary(uk.UTF-8):	Маленькі програми, що вбудовуються в панель MATE
Name:		mate-applets
Version:	1.5.2
Release:	0.18
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	912af4be09fb78405bd4da437b3b7f05
# check paths in Makefile before removing it!
#Patch0: m4_fix.patch
Patch0:		uidir.patch
Patch1:		use-libwnck.patch
URL:		https://github.com/mate-desktop/mate-applets
BuildRequires:	NetworkManager-devel >= 0.7
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	cpufrequtils-devel >= 0.3
BuildRequires:	dbus-devel >= 1.1.1
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgtop-devel >= 1:2.11.92
BuildRequires:	libwnck2-devel >= 2.9.3
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	mate-desktop-devel >= 1.1.0
BuildRequires:	mate-doc-utils >= 0.3.2
BuildRequires:	mate-icon-theme-devel >= 1.1.0
BuildRequires:	mate-panel-devel >= 1.5.2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	polkit-devel >= 0.92
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygobject-devel >= 2.6
BuildRequires:	python-pygtk-devel >= 2:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.9.4
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
BuildRequires:	gucharmap2-devel >= 2.23.0
Requires(post,postun):	hicolor-icon-theme
Requires:	gnome-icon-theme >= 2.26.0
Requires:	mate-panel >= 1.5
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/mate-panel

%description
The mate-applets package provides Panel applets which enhance your
MATE experience.

%description -l pl.UTF-8
Pakiet mate-applets udostępnia aplety Panelu, które usprawniają pracę
z MATE.

%description -l uk.UTF-8
Пакет mate-applets містить аплети Панелі MATE, що збільшують
комфортність роботи в середовищі MATE.

%description -l ru.UTF-8
Пакет mate-applets содержит апплеты Панели MATE, увеличивающие
комфортность работы в среде MATE.

%package accessx-status
Summary:	Keyboard Accessibility Status applet
Summary(pl.UTF-8):	Aplet stanu dostepności klawiatury
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}
Suggests:	mate-control-center >= 1.5

%description accessx-status
The Keyboard Accessibility Monitor shows you the status of the
keyboard accessibility features when these are in use. For example,
you can see which modifier keys are currently active, and which mouse
buttons are being pressed via the keyboard.

%description accessx-status -l pl.UTF-8
Aplet monitora dostępności klawiatury pokazuje stan funkcji
zwiększających dostępność klawiatury, kiedy są włączone. Pozwala
zobaczyć m.in. które klawisze modyfikatorów są aktywne albo które
przyciski myszy są wciskane z poziomu klawiatury.

%package battstat
Summary:	Battery Charge Monitor applet
Summary(pl.UTF-8):	Aplet monitora stanu naładowania akumulatora
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0

%description battstat
The Battery Charge Monitor shows the status of any batteries in your
laptop computer. The monitor can tell you the capacity remaining both
visually and as a percentage, as well as offer you an estimate of the
time remaining based off the current usage rate.

%description battstat -l pl.UTF-8
Aplet monitora stanu naładowania akumulatora pokazuje stan wszelkich
baterii w laptopie. Monitor informuje o pozostałej pojemności zarówno
w postaci graficznej, jak i procentowej, a także podaje przybliżony
pozostały czas pracy przy założeniu bieżącego użycia prądu.

%package charpicker
Summary:	Character Palette applet
Summary(pl.UTF-8):	Aplet palety znaków
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0

%description charpicker
The Character Palette provides a convenient way to access characters
that are not on your keyboard, such as accented characters,
mathematical symbols, special symbols, and punctuation marks.

You can insert characters from the applet into text strings, for
example in text documents or at the command line. You can customize
the contents of the applet to suit your requirements.

Character Palette supports the UTF-8 character encoding so you can use
the palette to display or copy any Unicode character.

%description charpicker -l pl.UTF-8
Aplet palety znaków udostępnia wygodną metodę wprowadzania znaków nie
istniejących na klawiaturze, takich jak znaki akcentowane, symbole
matematyczne, symbole specjalne i znaki przestankowe.

Przy pomocy apletu można wprowadzać znaki do łańcuchów tekstowych, na
przykład w dokumentach tekstowych lub w linii poleceń. Zawartość
apletu można dostosowywać do własnych wymagań.

Paleta znaków obsługuje kodowanie znaków UTF-8, więc można jej używać
do wyświetlania lub kopiowania dowolnych znaków unikodowych.

%package cpufreq
Summary:	CPU Frequency Scaling Monitor applet
Summary(pl.UTF-8):	Aplet monitora częstotliwości procesora
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}
Requires:	mate-polkit

%description cpufreq
The CPU Frequency Scaling Monitor provides a convenient way to monitor
the CPU Frequency Scaling for each CPU.

%description cpufreq -l pl.UTF-8
Aplet monitora częstotliwości procesora umożliwia wygodne
monitorowanie częstotliwości dla każdego procesora.

%package drivemount
Summary:	Disk Mounter applet
Summary(pl.UTF-8):	Aplet do montowania dysków
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0

%description drivemount
The Disk Mounter enables you to quickly mount and unmount various
types of drives and file systems.

%description drivemount -l pl.UTF-8
Aplet do montowania dysków, pozwalający szybko montować i odmontowywać
różne rodzaje dysków i systemów plików.

%package geyes
Summary:	Geyes applet - tracking the mouse pointer
Summary(pl.UTF-8):	Aplet geyes - śledzenie wskaźnika myszy
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0

%description geyes
The Geyes applet provides an entertaining way to track the movement of
the mouse pointer around your screen. The applet is an image of one or
more eyes that follow the mouse pointer around the screen.

%description geyes -l pl.UTF-8
Aplet geyes to zabawny sposób śledzenia ruchu wskaźnika myszy po
ekranie. Aplet jest obrazem jednego lub większej liczby oczu
podążających za wskaźnikiem myszy.

%package gweather
Summary:	Weather Report applet
Summary(pl.UTF-8):	Aplet raportu pogodowego
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}
Requires:	dbus(org.freedesktop.Notifications)

%description gweather
The Weather Report downloads weather information from the U.S.
National Weather Service (NWS) servers, including the Interactive
Weather Information Network (IWIN) and other weather services. You can
use Weather Report to display current weather information and weather
forecasts on your computer.

%description gweather -l pl.UTF-8
Aplet raportu pogodowego ściąga informacje pogodowe z serwerów U.S.
National Weather Service (NWS), wraz z siecią Interactive Weather
Information Network (IWIN) oraz innych serwisów pogodowych. Apletu
można używać do wyświetlania aktualnych informacji pogodowych oraz
prognoz.

%package invest
Summary:	Stock Ticker applet
Summary(pl.UTF-8):	Aplet wskaźnika giełdowego
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}
#Requires:	python-gnome-extras-egg >= 2.14.2

%description invest
The Invest MATE panel applet downloads current stock quotes from
Yahoo! Finance and displays the quotes in a drop-down list.

%description invest -l pl.UTF-8
Aplet wskaźnika giełdowego, ściągający aktualne notowania z serwisu
Yahoo! Finance i wyświetlające je na rozwijanej liście.

%package multiload
Summary:	System Monitor applet
Summary(pl.UTF-8):	Aplet monitora systemu
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
Suggests:	mate-system-monitor >= 1.5

%description multiload
The System Monitor displays system load information in graphical
format in a panel.

%description multiload -l pl.UTF-8
Aplet monitora systemu wyświetla w panelu informacje o obciążeniu
systemu w postaci graficznej.

%package stickynotes
Summary:	Sticky Notes applet
Summary(pl.UTF-8):	Aplet notatek
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0

%description stickynotes
The Sticky Notes panel application enables you to create, view, and
manage sticky notes on your desktop. You can edit the title, contents,
dimensions, and style of sticky notes. When the panel is restarted,
for example when you log out and log in again, all sticky notes are
saved and reopened in the same position with the same dimensions and
style.

%description stickynotes -l pl.UTF-8
Aplet notatek pozwala na tworzenie, oglądanie i zarządzanie
przyczepianymi notatkami na pulpicie. Pozwala modyfikować tytuł,
treść, wymiary i styl notatek. Przy restarcie panelu, na przykład przy
wylogowaniu i ponownym zalogowaniu, wszystkie notatki są zapisywane, a
następnie otwierane ponownie w tym samym miejscu, z tymi samymi
wymiarami i stylem.

%package trash
Summary:	Trash applet
Summary(pl.UTF-8):	Aplet śmietnika
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{version}-%{release}

%description trash
The Panel Trash applet lets you manage your Trash from the panel.

The trash on your panel acts identically to the trash on your desktop,
however it is useful because your panels are always visible.

%description trash -l pl.UTF-8
Aplet śmietnika pozwala na zarządzanie śmietnikiem z poziomu panelu.

Śmietnik w panelu zachowuje się tak samo, jak śmietnik na pulpicie,
ale jest przydatny o tyle, że panele są zawsze widoczne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--without-hal \
	--enable-networkmanager \
	--disable-schemas-compile \
	--disable-static
%{__make} \
	DOC_MODULE=

%install
rm -rf $RPM_BUILD_ROOT
%if 1
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DOC_MODULE= \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{py_sitedir}

# mate < 1.5 did not exist in pld, avoid dependency on mate-conf
%{__rm} $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/stickynotes-applet.convert

#%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgweather.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/mate_invest/*.py

# es_ES is more complete copy
mv -f $RPM_BUILD_ROOT%{_localedir}/es{_ES,}/LC_MESSAGES/*.mo
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/es_ES

# keyboard applet has been removed
#%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/xmodmap
%endif

rm -f *.lang
%find_lang %{name}
cat <<EOF>>%{name}.lang
%dir %{_datadir}/mate/help/C
%dir %{_datadir}/mate/help/C/figures
%dir %{_datadir}/mate/help/ar
%dir %{_datadir}/mate/help/ar/figures
%dir %{_datadir}/mate/help/ast
%dir %{_datadir}/mate/help/ast/figures
%dir %{_datadir}/mate/help/bg
%dir %{_datadir}/mate/help/bg/figures
%dir %{_datadir}/mate/help/ca
%dir %{_datadir}/mate/help/ca/figures
%dir %{_datadir}/mate/help/cs
%dir %{_datadir}/mate/help/cs/figures
%dir %{_datadir}/mate/help/da
%dir %{_datadir}/mate/help/da/figures
%dir %{_datadir}/mate/help/de
%dir %{_datadir}/mate/help/de/figures
%dir %{_datadir}/mate/help/el
%dir %{_datadir}/mate/help/el/figures
%dir %{_datadir}/mate/help/en_GB
%dir %{_datadir}/mate/help/en_GB/figures
%dir %{_datadir}/mate/help/es
%dir %{_datadir}/mate/help/es/figures
%dir %{_datadir}/mate/help/eu
%dir %{_datadir}/mate/help/eu/figures
%dir %{_datadir}/mate/help/fi
%dir %{_datadir}/mate/help/fi/figures
%dir %{_datadir}/mate/help/fr
%dir %{_datadir}/mate/help/fr/figures
%dir %{_datadir}/mate/help/gl
%dir %{_datadir}/mate/help/gl/figures
%dir %{_datadir}/mate/help/hu
%dir %{_datadir}/mate/help/hu/figures
%dir %{_datadir}/mate/help/it
%dir %{_datadir}/mate/help/it/figures
%dir %{_datadir}/mate/help/ko
%dir %{_datadir}/mate/help/ko/figures
%dir %{_datadir}/mate/help/nl
%dir %{_datadir}/mate/help/nl/figures
%dir %{_datadir}/mate/help/oc
%dir %{_datadir}/mate/help/oc/figures
%dir %{_datadir}/mate/help/pa
%dir %{_datadir}/mate/help/pa/figures
%dir %{_datadir}/mate/help/pt_BR
%dir %{_datadir}/mate/help/pt_BR/figures
%dir %{_datadir}/mate/help/ru
%dir %{_datadir}/mate/help/ru/figures
%dir %{_datadir}/mate/help/sv
%dir %{_datadir}/mate/help/sv/figures
%dir %{_datadir}/mate/help/uk
%dir %{_datadir}/mate/help/uk/figures
%dir %{_datadir}/mate/help/zh_CN
%dir %{_datadir}/mate/help/zh_CN/figures
%dir %{_datadir}/mate/help/zh_HK
%dir %{_datadir}/mate/help/zh_HK/figures
%dir %{_datadir}/mate/help/zh_TW
%dir %{_datadir}/mate/help/zh_TW/figures

EOF
#%find_lang accessx-status --with-mate
cat <<EOF >> accessx-status.lang
%{_datadir}/mate/help/*/figures/accessx*.png
EOF
#%find_lang battstat --with-mate
cat <<EOF >> battstat.lang
%{_datadir}/mate/help/*/figures/battstat*.png
%{_datadir}/mate/help/*/figures/context-menu.png
EOF
#%find_lang char-palette --with-mate
cat <<EOF >> char-palette.lang
%{_datadir}/mate/help/*/figures/charpalette*.png
%{_datadir}/mate/help/*/figures/charpick*.png
EOF
#%find_lang cpufreq --with-mate
cat <<EOF >> cpufreq.lang
%{_datadir}/mate/help/*/figures/cpufreq*.png
EOF
#%find_lang drivemount --with-mate
cat <<EOF >> drivemount.lang
%{_datadir}/mate/help/*/figures/drivemount*.png
EOF
#%find_lang geyes --with-mate
cat <<EOF >> geyes.lang
%{_datadir}/mate/help/*/figures/geyes*.png
EOF
#%find_lang gweather --with-mate
cat <<EOF >> gweather.lang
%{_datadir}/mate/help/*/figures/mateweather*.png
%{_datadir}/mate/help/*/figures/stock_weather-*.png
EOF
#%find_lang invest-applet --with-mate
cat <<EOF >> invest-applet.lang
%{_datadir}/mate/help/*/figures/symbol-search.png
EOF
#%find_lang mixer_applet2 --with-mate
touch mixer_applet2.lang
#%find_lang multiload --with-mate
cat <<EOF >> multiload.lang
%{_datadir}/mate/help/*/figures/multiload*.png
%{_datadir}/mate/help/*/figures/system_monitor.png
%{_datadir}/mate/help/*/figures/system-monitor-*.png
EOF
#%find_lang stickynotes_applet --with-mate
cat <<EOF >> stickynotes_applet.lang
%{_datadir}/mate/help/*/figures/stickynote*.png
EOF
#%find_lang trashapplet --with-mate
cat <<EOF >>trashapplet.lang
%{_datadir}/mate/help/*/figures/trash-applet.png
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post accessx-status
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun accessx-status
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post battstat
%scrollkeeper_update_post
%glib_compile_schemas

%preun battstat
%glib_compile_schemas

%postun battstat
%scrollkeeper_update_postun

%post charpicker
%scrollkeeper_update_post
%glib_compile_schemas
%update_icon_cache hicolor

%preun charpicker
%glib_compile_schemas

%postun charpicker
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post cpufreq
%glib_compile_schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun cpufreq
%glib_compile_schemas

%postun cpufreq
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post drivemount
%scrollkeeper_update_post
%glib_compile_schemas

%preun drivemount
%glib_compile_schemas

%postun drivemount
%scrollkeeper_update_postun

%post geyes
%scrollkeeper_update_post
%glib_compile_schemas
%update_icon_cache hicolor

%preun geyes
%glib_compile_schemas

%postun geyes
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post gweather
/sbin/ldconfig
%scrollkeeper_update_post

%postun gweather
/sbin/ldconfig
%scrollkeeper_update_postun

%post invest
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun invest
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post multiload
%scrollkeeper_update_post
%glib_compile_schemas

%preun multiload
%glib_compile_schemas

%postun multiload
%scrollkeeper_update_postun

%post stickynotes
%scrollkeeper_update_post
%glib_compile_schemas
%update_icon_cache hicolor

%preun stickynotes
%glib_compile_schemas

%postun stickynotes
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post trash
%scrollkeeper_update_post

%postun trash
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/builder
%lang(es_CL) %dir %{_localedir}/es_CL
%lang(es_CL) %dir %{_localedir}/es_CL/LC_MESSAGES
%lang(es_CO) %dir %{_localedir}/es_CO
%lang(es_CO) %dir %{_localedir}/es_CO/LC_MESSAGES
%lang(es_CR) %dir %{_localedir}/es_CR
%lang(es_CR) %dir %{_localedir}/es_CR/LC_MESSAGES
%lang(es_DO) %dir %{_localedir}/es_DO
%lang(es_DO) %dir %{_localedir}/es_DO/LC_MESSAGES
%lang(es_EC) %dir %{_localedir}/es_EC
%lang(es_EC) %dir %{_localedir}/es_EC/LC_MESSAGES
%lang(es_GT) %dir %{_localedir}/es_GT
%lang(es_GT) %dir %{_localedir}/es_GT/LC_MESSAGES
%lang(es_HN) %dir %{_localedir}/es_HN
%lang(es_HN) %dir %{_localedir}/es_HN/LC_MESSAGES
%lang(es_PA) %dir %{_localedir}/es_PA
%lang(es_PA) %dir %{_localedir}/es_PA/LC_MESSAGES
%lang(es_PE) %dir %{_localedir}/es_PE
%lang(es_PE) %dir %{_localedir}/es_PE/LC_MESSAGES
%lang(es_PR) %dir %{_localedir}/es_PR
%lang(es_PR) %dir %{_localedir}/es_PR/LC_MESSAGES
%lang(es_SV) %dir %{_localedir}/es_SV
%lang(es_SV) %dir %{_localedir}/es_SV/LC_MESSAGES
%lang(es_UY) %dir %{_localedir}/es_UY
%lang(es_UY) %dir %{_localedir}/es_UY/LC_MESSAGES
%lang(es_VE) %dir %{_localedir}/es_VE
%lang(es_VE) %dir %{_localedir}/es_VE/LC_MESSAGES

%files accessx-status -f accessx-status.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/accessx-status-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/mate-panel/ui/accessx-status-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.applets.AccessxStatusApplet.mate-panel-applet
%{_pixmapsdir}/mate-accessx-status-applet
%{_iconsdir}/mate/*/apps/ax-applet.png

%files battstat -f battstat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/battstat-applet-2
%{_datadir}/dbus-1/services/org.mate.panel.applet.BattstatAppletFactory.service
%{_datadir}/mate-panel/ui/battstat-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.applets.BattstatApplet.mate-panel-applet
%{_datadir}/%{name}/builder/battstat_applet.ui
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.battstat.gschema.xml
# FIXME package not to pull 'balsa'
%dir %{_sysconfdir}/sound
%dir %{_sysconfdir}/sound/events
%{_sysconfdir}/sound/events/mate-battstat_applet.soundlist

%files charpicker -f char-palette.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/charpick_applet2
%{_datadir}/dbus-1/services/org.mate.panel.applet.CharpickerAppletFactory.service
%{_datadir}/mate-panel/ui/charpick-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.applets.CharpickerApplet.mate-panel-applet
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.charpick.gschema.xml

%files cpufreq -f cpufreq.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mate-cpufreq-selector
%attr(755,root,root) %{_libexecdir}/mate-cpufreq-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.cpufreq.gschema.xml
%if 1
/etc/dbus-1/system.d/org.mate.CPUFreqSelector.conf
%{_datadir}/dbus-1/system-services/org.mate.CPUFreqSelector.service
%{_datadir}/polkit-1/actions/org.mate.cpufreqselector.policy
%endif
%{_datadir}/mate-panel/applets/org.mate.applets.CPUFreqApplet.mate-panel-applet
%{_datadir}/%{name}/builder/cpufreq-preferences.ui
%{_datadir}/mate-panel/ui/cpufreq-applet-menu.xml
%{_pixmapsdir}/mate-cpufreq-applet
%{_iconsdir}/hicolor/*/apps/mate-cpu-frequency-applet.png
%{_iconsdir}/hicolor/*/apps/mate-cpu-frequency-applet.svg

%files drivemount -f drivemount.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/drivemount_applet2
%{_datadir}/dbus-1/services/org.mate.panel.applet.DriveMountAppletFactory.service
%{_datadir}/mate-panel/ui/drivemount-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.applets.DriveMountApplet.mate-panel-applet

%files geyes -f geyes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/geyes_applet2
%{_datadir}/dbus-1/services/org.mate.panel.applet.GeyesAppletFactory.service
%{_datadir}/mate-panel/ui/geyes-applet-menu.xml
%{_datadir}/%{name}/geyes
%{_datadir}/mate-panel/applets/org.mate.applets.GeyesApplet.mate-panel-applet
%{_iconsdir}/hicolor/*/apps/mate-eyes-applet.*
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.geyes.gschema.xml

%files gweather -f gweather.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mateweather-applet-2
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWeatherAppletFactory.service
%{_datadir}/mate-panel/ui/mateweather-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.applets.MateWeatherApplet.mate-panel-applet

%files invest -f invest-applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mate-invest-chart
%attr(755,root,root) %{_libexecdir}/invest-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.InvestAppletFactory.service
%{_datadir}/%{name}/Invest_Applet.xml
%{_datadir}/mate-panel/applets/org.mate.applets.InvestApplet.mate-panel-applet
%{_datadir}/%{name}/builder/financialchart.ui
%{_datadir}/%{name}/builder/prefs-dialog.ui
%{_datadir}/%{name}/invest-applet
%{_iconsdir}/hicolor/*/apps/mate-invest-applet.*
%dir %{py_sitedir}/mate_invest
%{py_sitedir}/mate_invest/*.py[co]

%files multiload -f multiload.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/multiload-applet-2
%{_datadir}/dbus-1/services/org.mate.panel.applet.MultiLoadAppletFactory.service
%{_datadir}/mate-panel/ui/multiload-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.applets.MultiLoadApplet.mate-panel-applet
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.multiload.gschema.xml

%files stickynotes -f stickynotes_applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/stickynotes_applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.StickyNotesAppletFactory.service
%{_datadir}/mate-panel/ui/stickynotes-applet-menu.xml
%{_datadir}/%{name}/builder/stickynotes.ui
%{_datadir}/mate-panel/applets/org.mate.applets.StickyNotesApplet.mate-panel-applet
%{_pixmapsdir}/mate-stickynotes
%{_iconsdir}/hicolor/*/apps/mate-sticky-notes-applet.*
%{_datadir}/glib-2.0/schemas/org.mate.stickynotes.gschema.xml

%files trash -f trashapplet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/trashapplet
%{_datadir}/dbus-1/services/org.mate.panel.applet.TrashAppletFactory.service
%{_datadir}/%{name}/builder/trashapplet-empty-progress.ui
%{_datadir}/mate-panel/ui/trashapplet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.applets.TrashApplet.mate-panel-applet
