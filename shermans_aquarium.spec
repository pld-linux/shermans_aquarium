#
# Conditional build:
%bcond_without	sdl	# without Screensaver support
%bcond_without	gai	# without applet support
#
Summary:	Applet with aquarium
Summary(pl.UTF-8):   Aplet z akwarium
Name:		shermans_aquarium
Version:	3.0.1
Release:	1
License:	GPL v2 (except for images - see COPYING)
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/aquariumapplet/%{name}-%{version}.tar.bz2
# Source0-md5:	2be1531e45c535f148e2416c8d0abd5a
Source1:	%{name}.desktop
Patch0:		%{name}-3.0.0-opt.patch
Patch1:		%{name}-libdir.patch
URL:		http://aquariumapplet.sourceforge.net/
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2}
BuildRequires:	autoconf
%{?with_gai:BuildRequires:	gai-devel}
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
%{?with_sdl:Requires:	xscreensaver}
Obsoletes:	gnome-applet-aquarium
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xscreensavdir	/etc/X11/xscreensaver

%description
This applet gives an aquarium with some randomly selected fishes. Some
other features this program gives is that the temperature scale on the
right side shows the current CPU load. It can also be configured to
display the time and show the status of numlock, capslock and
scrollock.

%description -l pl.UTF-8
Aplet akwarium z losowo wybranymi rybami. Innymi funkcjami programu
jakie oferuje jest to, że skala temperatury na prawo pokazuje aktualne
obciążenie procesora. Aplet ten może też być skonfigurowany do
wyświetlania czasu i pokazywania statusu klawiszy numlock, capslock i
scrollock.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure \
	%{!?with_gai:--disable-gai}
	%{!?with_sdl:--disable-sdl}

%{__make} \
	OPT="%{rpmcflags}"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir}/docklets,%{_xscreensavdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets
mv -f $RPM_BUILD_ROOT%{_datadir}/control-center/screensavers/* \
	$RPM_BUILD_ROOT%{_xscreensavdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README README.gai TODO XSCREENSAVER
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/*
%{_libdir}/bonobo/servers/*.server
%{_pixmapsdir}/*
%{_xscreensavdir}/*
