Summary:	Displays a cute cow and message on your desktop
Name:		xcowsay
Version:	1.3
Release:	1
License:	GPL v3+
Group:		Applications/Games
URL:		http://www.doof.me.uk/xcowsay
Source0:	http://www.nickg.me.uk/files/%{name}-%{version}.tar.gz
# Source0-md5:	1df62b31e6bc57fbeb386da4539bb21d
Source1:	xcowfortune.desktop
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
Requires:	fortune-mod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcowsay displays a cute cow and message on your desktop. The message
can be text or images (with xcowdream) xcowsay can run in daemon mode
for sending your cow message with DBus. Inspired by the original
cowsay.

%prep
%setup -q
iconv -f iso-8859-1 -t utf-8 NEWS -o NEWS

%build
%configure \
	--enable-dbus
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

# xcowfortune is the only .desktop file because the other program
#(xcowsay, xcowthink and xcowdream) need an argument
install -d $RPM_BUILD_ROOT%{_desktopdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/xcowdream
%attr(755,root,root) %{_bindir}/xcowfortune
%attr(755,root,root) %{_bindir}/xcowsay
%attr(755,root,root) %{_bindir}/xcowthink
%{_mandir}/man6/xcowsay.6*
%{_datadir}/xcowsay
%{_desktopdir}/xcowfortune.desktop
