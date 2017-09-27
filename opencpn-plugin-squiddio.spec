Name: opencpn-plugin-squiddio
Summary: Squiddio plugin for OpenCPN
Version: 0.7
Release: 1%{?dist}
License: GPLv2+

Source0: https://github.com/mauroc/squiddio_pi/archive/0.7.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Supplements: opencpn%{_isa}

%description
Squiddio is a global user-sourced and maintained repository of sailing
destinations. Plugin enables downloading and viewing destinations as
waypoints from within OpenCPN.

%prep

%setup0 -n squiddio_pi-0.7

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-squiddio_pi

%files -f build/opencpn-squiddio_pi.lang

%{_libdir}/opencpn/libsquiddio_pi.so
