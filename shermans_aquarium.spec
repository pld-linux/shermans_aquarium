Summary:	Applet with aquarium
Summary(pl):	Aplet z akwarium
Name:		shermans_aquarium
Version:	3.0.0
%define _pre 	pre1
Release:	0.%{_pre}.1
License:	GPL v2 (except for images - see COPYING)
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/sourceforge/aquariumapplet/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	e9064bbc8a210c458bb8708dbbdea281
Source1:	%{name}.desktop
Patch0:		%{name}-3.0.0-opt.patch
URL:		http://aquariumapplet.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	gai-devel
BuildRequires:	pkgconfig
Obsoletes:	gnome-applet-aquarium 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This applet gives an aquarium with some randomly selected fishes. Some
other features this program gives is that the temperature scale on the
right side shows the current CPU load. It can also be configured to
display the time and show the status of numlock, capslock and
scrollock.

%description -l pl
Aplet akwarium z losowo wybranymi rybami. Innymi funkcjami programu
jakie oferuje jest to, ¿e skala temperatury na prawo pokazuje aktualne
obci±¿enie procesora. Aplet ten mo¿e te¿ byæ skonfigurowany do
wy¶wietlania czasu i pokazywania statusu klawiszy numlock, capslock i
scrollock.

%prep
%setup -q -n %{name}-%{version}%{_pre}
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo
echo "If you use WindowMaker or the applet looks weird,"
echo "try run: shermans_applet --gai-window-maker"
echo

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/DockApplets/*
%{_libdir}/bonobo/servers/*.server
%{_pixmapsdir}/*
