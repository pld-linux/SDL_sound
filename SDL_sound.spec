Summary:	An abstract soundfile decoder
Summary(pl.UTF-8):	Abstrakcyjny dekoder plików dźwiękowych
Name:		SDL_sound
# keep 1.x here, for >= 2 see SDL2_sound.spec
Version:	1.0.3
Release:	9
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.icculus.org/SDL_sound/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	aa09cd52df85d29bee87a664424c94b5
Patch0:		%{name}-physfs.patch
URL:		http://www.icculus.org/SDL_sound/
BuildRequires:	SDL-devel >= 1.2.6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	libmikmod-devel >= 3.1.5
BuildRequires:	libmodplug-devel
BuildRequires:	libvorbis-devel >= 1:1.0-6
BuildRequires:	libtool
BuildRequires:	physfs-devel >= 3
BuildRequires:	smpeg-devel >= 0.4.4-12
BuildRequires:	speex-devel
Requires:	SDL >= 1.2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as .WAV and .MP3. It is meant to make the
programmer's sound playback tasks simpler. The programmer gives
SDL_sound a filename, or feeds it data directly from one of many
sources, and then reads the decoded waveform data back at her leisure.
If resource constraints are a concern, SDL_sound can process sound
data in programmer-specified blocks. Alternately, SDL_sound can decode
a whole sound file and hand back a single pointer to the whole
waveform. SDL_sound can also handle sample rate, audio format, and
channel conversion on-the-fly and behind-the-scenes, if the programmer
desires.

%description -l pl.UTF-8
SDL_sound to biblioteka obsługująca dekodowanie kilku popularnych
formatów plików dźwiękowych, takich jak .WAV lub .MP3. Jej celem
jest uproszczenie pracy programisty przy odtwarzaniu dźwięku.
Programista przekazuje SDL_sound nazwę pliku lub dostarcza dane
bezpośrednio z jednego z wielu źródeł, a następnie odczytuje strumień
zdekodowanych danych. Jeśli ograniczenia zasobów są istotne, SDL_sound
może obsługiwać dane dźwiękowe w podanych blokach. Alternatywnie,
SDL_sound może dekodować cały plik dźwiękowy i przekazywać z powrotem
pojedynczy wskaźnik do całości zdekodowanych danych. SDL_sound może
także obsługiwać w locie konwersję częstotliwości próbkowania, formatu
dźwięku i liczby kanałów.

%package play
Summary:	SDL_sound/physfs based music player
Summary(pl.UTF-8):	Odtwarzacz muzyki oparty na SDL_sound/physfs
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	physfs >= 3

%description play
SDL_sound/physfs based music player.

%description play -l pl.UTF-8
Odtwarzacz muzyki oparty na SDL_sound/physfs.

%package devel
Summary:	Header files and more to develop SDL_sound applications
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji z użyciem SDL_sound
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.6
Requires:	flac-devel >= 1.1.3
Requires:	libmikmod-devel >= 3.1.5
Requires:	libmodplug-devel
Requires:	libvorbis-devel >= 1:1.0
Requires:	smpeg-devel >= 0.4.4
Requires:	speex-devel

%description devel
Header files and more to develop SDL_sound applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji z użyciem SDL_sound.

%package static
Summary:	Static SDL_sound libraries
Summary(pl.UTF-8):	Statyczne biblioteki SDL_sound
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL_sound libraries.

%description static -l pl.UTF-8
Statyczne biblioteki SDL_sound.

%prep
%setup -q
%patch -P0 -p1

%{__rm} acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains additional notes
%doc CHANGELOG COPYING CREDITS README TODO
%attr(755,root,root) %{_bindir}/playsound_simple
%attr(755,root,root) %{_libdir}/libSDL_sound-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL_sound-1.0.so.1

%files play
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/playsound

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL_sound.so
%{_libdir}/libSDL_sound.la
%{_includedir}/SDL/SDL_sound.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL_sound.a
