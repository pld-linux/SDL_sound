Summary:	An abstract soundfile decoder
Summary(pl):	Abstrakcyjny dekoder plików d¼wiêkowych
Name:		SDL_sound
Version:	1.0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.icculus.org/%{name}/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	49e197ef7c8ab623d0640dc74be43160
URL:		http://www.icculus.org/SDL_sound/
BuildRequires:	SDL-devel >= 1.2.6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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

%description -l pl
SDL_sound to biblioteka obs³uguj±ca dekodowanie kilku popularnych
formatów plików d¼wiêkowych, takich jak .WAV lub .MP3. Jej celem
jest uproszczenie pracy programisty przy odtwarzaniu d¼wiêku.
Programista przekazuje SDL_sound nazwê pliku lub dostarcza dane
bezpo¶rednio z jednego z wielu ¼róde³, a nastêpnie odczytuje strumieñ
zdekodowanych danych. Je¶li ograniczenia zasobów s± istotne, SDL_sound
mo¿e obs³ugiwaæ dane d¼wiêkowe w podanych blokach. Alternatywnie,
SDL_sound mo¿e dekodowaæ ca³y plik d¼wiêkowy i przekazywaæ z powrotem
pojedynczy wska¼nik do ca³o¶ci zdekodowanych danych. SDL_sound mo¿e
tak¿e obs³ugiwaæ w locie konwersjê czêstotliwo¶ci próbkowania, formatu
d¼wiêku i liczby kana³ów.

%package devel
Summary:	Header files and more to develop SDL_sound applications
Summary(pl):	Pliki nag³ówkowe do tworzenia aplikacji z u¿yciem SDL_sound
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_sound applications.

%description devel -l pl
Pliki nag³ówkowe do tworzenia aplikacji z u¿yciem SDL_sound.

%package static
Summary:	Static SDL_sound libraries
Summary(pl):	Statyczne biblioteki SDL_sound
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static SDL_sound libraries.

%description static -l pl
Statyczne biblioteki SDL_sound.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/playsound
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
