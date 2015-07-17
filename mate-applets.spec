# TODO
# - cpufreq applet does not start
#
# Conditional build:
%bcond_with	gtk3		# use GTK+ 3.x instead of 2.x
%bcond_without	gucharmap	# Gucharmap (character map) support in charpicker applet

Summary:	Small applications which embed themselves in the MATE panel
Summary(pl.UTF-8):	Aplety MATE - małe aplikacje osadzające się w panelu
Summary(ru.UTF-8):	Маленькие программы, встраивающиеся в панель MATE
Summary(uk.UTF-8):	Маленькі програми, що вбудовуються в панель MATE
Name:		mate-applets
Version:	1.10.3
Release:	1
License:	GPL v2+ (applets), FDL (help)
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.10/%{name}-%{version}.tar.xz
# Source0-md5:	4f82b95221c98622e75b8a6b00d0d90d
# check paths in Makefile before removing it!
Patch0:		m4_fix.patch
Patch1:		uidir.patch
URL:		https://github.com/mate-desktop/mate-applets
BuildRequires:	NetworkManager-devel >= 0.7
%ifarch %{ix86} arm mips ppc sh
BuildRequires:	apmd-devel
%endif
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	cpufrequtils-devel >= 0.3
BuildRequires:	dbus-devel >= 1.1.2
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-tools >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.26.0
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.24.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
%{!?with_gtk3:BuildRequires:	gtksourceview2-devel >= 2.0}
%{?with_gtk3:BuildRequires:	gtksourceview3-devel >= 3.0}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgtop-devel >= 1:2.11.92
BuildRequires:	libmateweather-devel >= 1.6.1
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool >= 1:1.4.3
%{?with_gtk3:BuildRequires:	libwnck-devel >= 3.0.0}
%{!?with_gtk3:BuildRequires:	libwnck2-devel >= 2.9.3}
BuildRequires:	libxml2-devel >= 1:2.5.0
%if %{with gucharmap}
%{?with_gtk3:BuildRequires:	gucharmap-devel >= 3.0.0}
%{!?with_gtk3:BuildRequires:	gucharmap2-devel >= 2.32.1}
%endif
BuildRequires:	mate-common >= 1.1.0
BuildRequires:	mate-desktop-devel >= 1.7.3
BuildRequires:	mate-icon-theme-devel >= 1.1.0
BuildRequires:	mate-panel-devel >= 1.7.0
BuildRequires:	mate-settings-daemon-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	polkit-devel >= 0.92
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygobject3-devel >= 3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.9.4
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	mate-icon-theme >= 1.1.0
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

%package -n mate-applet-accessx-status
Summary:	Keyboard Accessibility Status applet for MATE Desktop
Summary(pl.UTF-8):	Aplet stanu dostepności klawiatury dla środowiska MATE
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	mate-icon-theme >= 1.1.0
Requires:	mate-panel >= 1.7.0
Suggests:	mate-control-center >= 1.5

%description -n mate-applet-accessx-status
The Keyboard Accessibility Monitor shows you the status of the
keyboard accessibility features when these are in use. For example,
you can see which modifier keys are currently active, and which mouse
buttons are being pressed via the keyboard.

%description -n mate-applet-accessx-status -l pl.UTF-8
Aplet monitora dostępności klawiatury pokazuje stan funkcji
zwiększających dostępność klawiatury, kiedy są włączone. Pozwala
zobaczyć m.in. które klawisze modyfikatorów są aktywne albo które
przyciski myszy są wciskane z poziomu klawiatury.

%package -n mate-applet-battstat
Summary:	Battery Charge Monitor applet for MATE Desktop
Summary(pl.UTF-8):	Aplet monitora stanu naładowania akumulatora dla środowiska MATE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	libnotify >= 0.7.0
Requires:	mate-panel >= 1.7.0
Requires:	upower >= 0.9.4

%description -n mate-applet-battstat
The Battery Charge Monitor shows the status of any batteries in your
laptop computer. The monitor can tell you the capacity remaining both
visually and as a percentage, as well as offer you an estimate of the
time remaining based off the current usage rate.

%description -n mate-applet-battstat -l pl.UTF-8
Aplet monitora stanu naładowania akumulatora pokazuje stan wszelkich
baterii w laptopie. Monitor informuje o pozostałej pojemności zarówno
w postaci graficznej, jak i procentowej, a także podaje przybliżony
pozostały czas pracy przy założeniu bieżącego użycia prądu.

%package -n mate-applet-charpicker
Summary:	Character Palette applet for MATE Desktop
Summary(pl.UTF-8):	Aplet palety znaków dla środowiska MATE
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	hicolor-icon-theme
Requires:	mate-panel >= 1.7.0

%description -n mate-applet-charpicker
The Character Palette provides a convenient way to access characters
that are not on your keyboard, such as accented characters,
mathematical symbols, special symbols, and punctuation marks.

You can insert characters from the applet into text strings, for
example in text documents or at the command line. You can customize
the contents of the applet to suit your requirements.

Character Palette supports the UTF-8 character encoding so you can use
the palette to display or copy any Unicode character.

%description -n mate-applet-charpicker -l pl.UTF-8
Aplet palety znaków udostępnia wygodną metodę wprowadzania znaków nie
istniejących na klawiaturze, takich jak znaki akcentowane, symbole
matematyczne, symbole specjalne i znaki przestankowe.

Przy pomocy apletu można wprowadzać znaki do łańcuchów tekstowych, na
przykład w dokumentach tekstowych lub w linii poleceń. Zawartość
apletu można dostosowywać do własnych wymagań.

Paleta znaków obsługuje kodowanie znaków UTF-8, więc można jej używać
do wyświetlania lub kopiowania dowolnych znaków unikodowych.

%package -n mate-applet-command
Summary:	Command applet for MATE Desktop
Summary(pl.UTF-8):	Aplet uruchamiania poleceń dla środowiska MATE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	hicolor-icon-theme
Requires:	mate-panel >= 1.7.0

%description -n mate-applet-command
Command applet for MATE Desktop.

%description -n mate-applet-command -l pl.UTF-8
Aplet uruchamiania poleceń dla środowiska MATE.

%package -n mate-applet-cpufreq
Summary:	CPU Frequency Scaling Monitor applet for MATE Desktop
Summary(pl.UTF-8):	Aplet monitora częstotliwości procesora dla środowiska MATE
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	cpufrequtils-libs >= 0.3
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	hicolor-icon-theme
Requires:	mate-panel >= 1.7.0
Requires:	mate-polkit
Requires:	polkit >= 0.92

%description -n mate-applet-cpufreq
The CPU Frequency Scaling Monitor provides a convenient way to monitor
the CPU Frequency Scaling for each CPU.

%description -n mate-applet-cpufreq -l pl.UTF-8
Aplet monitora częstotliwości procesora umożliwia wygodne
monitorowanie częstotliwości dla każdego procesora.

%package -n mate-applet-drivemount
Summary:	Disk Mounter applet for MATE Desktop
Summary(pl.UTF-8):	Aplet do montowania dysków dla środowiska MATE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	mate-panel >= 1.7.0

%description -n mate-applet-drivemount
The Disk Mounter enables you to quickly mount and unmount various
types of drives and file systems.

%description -n mate-applet-drivemount -l pl.UTF-8
Aplet do montowania dysków, pozwalający szybko montować i odmontowywać
różne rodzaje dysków i systemów plików.

%package -n mate-applet-geyes
Summary:	Geyes applet - tracking the mouse pointer for MATE Desktop
Summary(pl.UTF-8):	Aplet geyes - śledzenie wskaźnika myszy dla środowiska MATE
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	hicolor-icon-theme
Requires:	mate-panel >= 1.7.0

%description -n mate-applet-geyes
The Geyes applet provides an entertaining way to track the movement of
the mouse pointer around your screen. The applet is an image of one or
more eyes that follow the mouse pointer around the screen.

%description -n mate-applet-geyes -l pl.UTF-8
Aplet geyes to zabawny sposób śledzenia ruchu wskaźnika myszy po
ekranie. Aplet jest obrazem jednego lub większej liczby oczu
podążających za wskaźnikiem myszy.

%package -n mate-applet-gweather
Summary:	Weather Report applet for MATE Desktop
Summary(pl.UTF-8):	Aplet raportu pogodowego dla środowiska MATE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	dbus >= 1.1.2
Requires:	dbus(org.freedesktop.Notifications)
Requires:	dbus-glib >= 0.74
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	libmateweather >= 1.6.1
Requires:	libnotify >= 0.7.0
Requires:	mate-panel >= 1.7.0

%description -n mate-applet-gweather
The Weather Report downloads weather information from the U.S.
National Weather Service (NWS) servers, including the Interactive
Weather Information Network (IWIN) and other weather services. You can
use Weather Report to display current weather information and weather
forecasts on your computer.

%description -n mate-applet-gweather -l pl.UTF-8
Aplet raportu pogodowego ściąga informacje pogodowe z serwerów U.S.
National Weather Service (NWS), wraz z siecią Interactive Weather
Information Network (IWIN) oraz innych serwisów pogodowych. Apletu
można używać do wyświetlania aktualnych informacji pogodowych oraz
prognoz.

%package -n mate-applet-invest
Summary:	Stock Ticker applet for MATE Desktop
Summary(pl.UTF-8):	Aplet wskaźnika giełdowego dla środowiska MATE
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	hicolor-icon-theme
Requires:	mate-panel >= 1.7.0
Requires:	python-dbus
Requires:	python-pygobject3 >= 3.0

%description -n mate-applet-invest
The Invest MATE panel applet downloads current stock quotes from
Yahoo! Finance and displays the quotes in a drop-down list.

%description -n mate-applet-invest -l pl.UTF-8
Aplet wskaźnika giełdowego, ściągający aktualne notowania z serwisu
Yahoo! Finance i wyświetlające je na rozwijanej liście.

%package -n mate-applet-multiload
Summary:	System Monitor applet for MATE Desktop
Summary(pl.UTF-8):	Aplet monitora systemu dla środowiska MATE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	libgtop >= 1:2.11.92
Requires:	mate-panel >= 1.7.0
Suggests:	mate-system-monitor >= 1.5

%description -n mate-applet-multiload
The System Monitor displays system load information in graphical
format in a panel.

%description -n mate-applet-multiload -l pl.UTF-8
Aplet monitora systemu wyświetla w panelu informacje o obciążeniu
systemu w postaci graficznej.

%package -n mate-applet-stickynotes
Summary:	Sticky Notes applet for MATE Desktop
Summary(pl.UTF-8):	Aplet notatek dla środowiska MATE
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	hicolor-icon-theme
%{?with_gtk3:Requires:	libwnck >= 3.0.0}
%{!?with_gtk3:Requires:	libwnck2 >= 2.9.3}
Requires:	libxml2 >= 1:2.5.0
Requires:	mate-panel >= 1.7.0

%description -n mate-applet-stickynotes
The Sticky Notes panel application enables you to create, view, and
manage sticky notes on your desktop. You can edit the title, contents,
dimensions, and style of sticky notes. When the panel is restarted,
for example when you log out and log in again, all sticky notes are
saved and reopened in the same position with the same dimensions and
style.

%description -n mate-applet-stickynotes -l pl.UTF-8
Aplet notatek pozwala na tworzenie, oglądanie i zarządzanie
przyczepianymi notatkami na pulpicie. Pozwala modyfikować tytuł,
treść, wymiary i styl notatek. Przy restarcie panelu, na przykład przy
wylogowaniu i ponownym zalogowaniu, wszystkie notatki są zapisywane, a
następnie otwierane ponownie w tym samym miejscu, z tymi samymi
wymiarami i stylem.

%package -n mate-applet-timer
Summary:	Timer applet for MATE Desktop
Summary(pl.UTF-8):	Aplet czasomierza dla środowiska MATE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	mate-panel >= 1.7.0

%description -n mate-applet-timer
Timer applet for MATE Desktop.

%description -n mate-applet-timer -l pl.UTF-8
Aplet czasomierza dla środowiska MATE.

%package -n mate-applet-trash
Summary:	Trash applet for MATE Desktop
Summary(pl.UTF-8):	Aplet śmietnika dla środowiska MATE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	mate-panel >= 1.7.0

%description -n mate-applet-trash
The Panel Trash applet lets you manage your Trash from the panel.

The trash on your panel acts identically to the trash on your desktop,
however it is useful because your panels are always visible.

%description -n mate-applet-trash -l pl.UTF-8
Aplet śmietnika pozwala na zarządzanie śmietnikiem z poziomu panelu.

Śmietnik w panelu zachowuje się tak samo, jak śmietnik na pulpicie,
ale jest przydatny o tyle, że panele są zawsze widoczne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e '1s,/usr/bin/env python,/usr/bin/python,' \
	invest-applet/invest/{chart.py,invest-applet.py,mate-invest-chart}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-networkmanager \
	--disable-schemas-compile \
	--disable-static \
	--enable-timer-applet \
	%{?with_gtk3:--with-gtk=3.0} \
	--without-hal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{py_sitedir}

# mate < 1.5 did not exist in pld, avoid dependency on mate-conf
%{__rm} $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/stickynotes-applet.convert

%py_postclean

# outdated version of es (as of 1.6.1)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/es_ES

%find_lang %{name}
%find_lang mate-accessx-status --with-mate
%find_lang mate-battstat --with-mate
%find_lang mate-char-palette --with-mate
%find_lang mate-cpufreq-applet --with-mate
%find_lang mate-drivemount --with-mate
%find_lang mate-geyes --with-mate
%find_lang mateweather --with-mate
%find_lang mate-invest-applet --with-mate
%find_lang mate-multiload --with-mate
%find_lang mate-stickynotes-applet --with-mate
%find_lang mate-trashapplet --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%post -n mate-applet-accessx-status
%update_icon_cache mate

%postun -n mate-applet-accessx-status
%update_icon_cache mate

%post -n mate-applet-battstat
%glib_compile_schemas

%preun -n mate-applet-battstat
%glib_compile_schemas

%post -n mate-applet-charpicker
%glib_compile_schemas
%update_icon_cache hicolor

%preun -n mate-applet-charpicker
%glib_compile_schemas

%postun -n mate-applet-charpicker
%update_icon_cache hicolor

%post -n mate-applet-command
%glib_compile_schemas

%preun -n mate-applet-command
%glib_compile_schemas

%post -n mate-applet-cpufreq
%glib_compile_schemas
%update_icon_cache hicolor

%preun -n mate-applet-cpufreq
%glib_compile_schemas

%postun -n mate-applet-cpufreq
%update_icon_cache hicolor

%post -n mate-applet-drivemount
%glib_compile_schemas

%preun -n mate-applet-drivemount
%glib_compile_schemas

%post -n mate-applet-geyes
%glib_compile_schemas
%update_icon_cache hicolor

%preun -n mate-applet-geyes
%glib_compile_schemas

%postun -n mate-applet-geyes
%update_icon_cache hicolor

%post -n mate-applet-invest
%update_icon_cache hicolor

%postun -n mate-applet-invest
%update_icon_cache hicolor

%post -n mate-applet-multiload
%glib_compile_schemas

%preun -n mate-applet-multiload
%glib_compile_schemas

%post -n mate-applet-stickynotes
%glib_compile_schemas
%update_icon_cache hicolor

%preun -n mate-applet-stickynotes
%glib_compile_schemas

%postun -n mate-applet-stickynotes
%update_icon_cache hicolor

%post -n mate-applet-timer
%glib_compile_schemas

%preun -n mate-applet-timer
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/builder

%files -n mate-applet-accessx-status -f mate-accessx-status.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/accessx-status-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.applets.AccessxStatusApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/accessx-status-applet-menu.xml
%{_pixmapsdir}/mate-accessx-status-applet
%{_iconsdir}/mate/*/apps/ax-applet.png

%files -n mate-applet-battstat -f mate-battstat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/battstat-applet
%{_datadir}/%{name}/builder/battstat_applet.ui
%{_datadir}/dbus-1/services/org.mate.panel.applet.BattstatAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.applets.BattstatApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/battstat-applet-menu.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.battstat.gschema.xml
# FIXME package not to pull 'balsa'
%dir %{_sysconfdir}/sound
%dir %{_sysconfdir}/sound/events
%{_sysconfdir}/sound/events/mate-battstat_applet.soundlist

%files -n mate-applet-charpicker -f mate-char-palette.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mate-charpick-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.CharpickerAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.charpick.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.CharpickerApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/charpick-applet-menu.xml
%{_mandir}/man1/mate-charpick-applet.1*

%files -n mate-applet-command
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/command-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.CommandAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.command.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.CommandApplet.mate-panel-applet

%files -n mate-applet-cpufreq -f mate-cpufreq-applet.lang
%defattr(644,root,root,755)
# selector
%attr(755,root,root) %{_bindir}/mate-cpufreq-selector
/etc/dbus-1/system.d/org.mate.CPUFreqSelector.conf
%{_datadir}/dbus-1/system-services/org.mate.CPUFreqSelector.service
%{_datadir}/polkit-1/actions/org.mate.cpufreqselector.policy
# applet itself
%attr(755,root,root) %{_libexecdir}/mate-cpufreq-applet
%{_datadir}/%{name}/builder/cpufreq-preferences.ui
%{_datadir}/dbus-1/services/org.mate.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.cpufreq.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.CPUFreqApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/cpufreq-applet-menu.xml
%{_pixmapsdir}/mate-cpufreq-applet
%{_iconsdir}/hicolor/*/apps/mate-cpu-frequency-applet.png
%{_iconsdir}/hicolor/*/apps/mate-cpu-frequency-applet.svg
%{_mandir}/man1/mate-cpufreq-selector.1*

%files -n mate-applet-drivemount -f mate-drivemount.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mate-drivemount-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.DriveMountAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.applets.DriveMountApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/drivemount-applet-menu.xml
%{_mandir}/man1/mate-drivemount-applet.1*

%files -n mate-applet-geyes -f mate-geyes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mate-geyes-applet
%{_datadir}/%{name}/geyes
%{_datadir}/dbus-1/services/org.mate.panel.applet.GeyesAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.geyes.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.GeyesApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/geyes-applet-menu.xml
%{_iconsdir}/hicolor/*/apps/mate-eyes-applet.*
%{_mandir}/man1/mate-geyes-applet.1*

%files -n mate-applet-gweather -f mateweather.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mateweather-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWeatherAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.applets.MateWeatherApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/mateweather-applet-menu.xml
%{_mandir}/man1/mateweather.1*

%files -n mate-applet-invest -f mate-invest-applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mate-invest-chart
%attr(755,root,root) %{_libexecdir}/invest-applet
%{_datadir}/%{name}/Invest_Applet.xml
%{_datadir}/%{name}/invest-applet
%{_datadir}/%{name}/builder/financialchart.ui
%{_datadir}/%{name}/builder/prefs-dialog.ui
%{_datadir}/dbus-1/services/org.mate.panel.applet.InvestAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.applets.InvestApplet.mate-panel-applet
%{_iconsdir}/hicolor/*/apps/mate-invest-applet.*
%dir %{py_sitedir}/mate_invest
%{py_sitedir}/mate_invest/*.py[co]
%{_mandir}/man1/mate-invest-chart.1*

%files -n mate-applet-multiload -f mate-multiload.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mate-multiload-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.MultiLoadAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.multiload.gschema.xml
%{_datadir}/mate-panel/ui/multiload-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.applets.MultiLoadApplet.mate-panel-applet
%{_mandir}/man1/mate-multiload-applet.1*

%files -n mate-applet-stickynotes -f mate-stickynotes-applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/stickynotes_applet
%{_datadir}/%{name}/builder/stickynotes.ui
%{_datadir}/dbus-1/services/org.mate.panel.applet.StickyNotesAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.stickynotes.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.StickyNotesApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/stickynotes-applet-menu.xml
%{_pixmapsdir}/mate-stickynotes
%{_iconsdir}/hicolor/*/apps/mate-sticky-notes-applet.*

%files -n mate-applet-timer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/timer-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.TimerAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.timer.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.TimerApplet.mate-panel-applet

%files -n mate-applet-trash -f mate-trashapplet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/trashapplet
%{_datadir}/%{name}/builder/trashapplet-empty-progress.ui
%{_datadir}/dbus-1/services/org.mate.panel.applet.TrashAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.applets.TrashApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/trashapplet-menu.xml
