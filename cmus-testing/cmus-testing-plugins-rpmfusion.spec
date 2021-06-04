%global forgeurl https://github.com/pgaskin/cmus
%global commit   45c5a3199740268a60c1cf9dff1a5c752df0e062
%forgemeta

Name:		cmus-testing-plugins-rpmfusion
Version:	2.9.1
Release:	5%{?dist}
Summary:	Plugins for ncurses-based music player with RPMFusion dependencies.

License:	GPLv2+
URL:		%{forgeurl}
Source:		%{forgesource}

BuildRequires:	gcc
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	faad2-devel
BuildRequires:	libmp4v2-devel

Requires:	cmus-testing = %{version}-%{release}
Supplements:	cmus-testing = %{version}-%{release}

%description
This package contains plugins for cmus requiring nonfree or restricted packages
from RPMFusion, including the AAC, FFmpeg, and MP4 input plugins.

%prep
%forgesetup

%build
./configure \
	prefix=%{_prefix} \
	bindir=%{_bindir} \
	datadir=%{_datadir} \
	libdir=%{_libdir} \
	mandir=%{_mandir} \
	exampledir=%{_datadir}/cmus/examples \
	CONFIG_AAC=y \
	CONFIG_ALSA=n \
	CONFIG_AO=n \
	CONFIG_ARTS=n \
	CONFIG_CDDB=n \
	CONFIG_CDIO=n \
	CONFIG_COREAUDIO=n \
	CONFIG_CUE=n \
	CONFIG_DISCID=n \
	CONFIG_FFMPEG=y \
	CONFIG_FLAC=n \
	CONFIG_JACK=n \
	CONFIG_MAD=n \
	CONFIG_MIKMOD=n \
	CONFIG_BASS=n \
	CONFIG_MODPLUG=n \
	CONFIG_MP4=y \
	CONFIG_MPC=n \
	CONFIG_MPRIS=n \
	CONFIG_OPUS=n \
	CONFIG_OSS=n \
	CONFIG_PULSE=n \
	CONFIG_ROAR=n \
	CONFIG_SAMPLERATE=n \
	CONFIG_SNDIO=n \
	CONFIG_SUN=n \
	CONFIG_TREMOR=n \
	CONFIG_VORBIS=n \
	CONFIG_VTX=n \
	CONFIG_WAVEOUT=n \
	CONFIG_WAVPACK=n \
	CONFIG_WAV=n \
	CFLAGS="${RPM_OPT_FLAGS}" \
	LDFLAGS="${RPM_LD_FLAGS}"
%make_build plugins V=2

%install
make install-plugins DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS
%license COPYING
%{_libdir}/cmus/{ip,op}/*

%changelog
* Fri Jun 04 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-5.20210604git45c5a31
- Update for latest cmus-testing release.

* Thu Jun 03 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-4.20210603git71ebcd3
- Update for latest cmus-testing release.

* Wed Jun 02 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-3.20210602gita3e6caa
- Update for latest cmus-testing release.

* Tue Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-2.20210601git48efe76
- Rebuild.

* Tue Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-1.20210601git48efe76
- Initial package.
