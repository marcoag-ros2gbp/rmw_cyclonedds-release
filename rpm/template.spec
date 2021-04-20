%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-rmw-cyclonedds-cpp
Version:        0.22.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS rmw_cyclonedds_cpp package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-cyclonedds
Requires:       ros-galactic-rcpputils
Requires:       ros-galactic-rcutils
Requires:       ros-galactic-rmw
Requires:       ros-galactic-rmw-dds-common
Requires:       ros-galactic-rosidl-runtime-c
Requires:       ros-galactic-rosidl-typesupport-introspection-c
Requires:       ros-galactic-rosidl-typesupport-introspection-cpp
Requires:       ros-galactic-ros-workspace
BuildRequires:  ros-galactic-ament-cmake-ros
BuildRequires:  ros-galactic-ament-lint-auto
BuildRequires:  ros-galactic-ament-lint-common
BuildRequires:  ros-galactic-cyclonedds
BuildRequires:  ros-galactic-rcpputils
BuildRequires:  ros-galactic-rcutils
BuildRequires:  ros-galactic-rmw
BuildRequires:  ros-galactic-rmw-dds-common
BuildRequires:  ros-galactic-rosidl-runtime-c
BuildRequires:  ros-galactic-rosidl-typesupport-introspection-c
BuildRequires:  ros-galactic-rosidl-typesupport-introspection-cpp
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-galactic-rmw-implementation-packages(member)

%if 0%{?with_weak_deps}
Supplements:    ros-galactic-rmw-implementation-packages(all)
%endif

%description
Implement the ROS middleware interface using Eclipse CycloneDDS in C++.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Tue Apr 20 2021 Erik Boasson <erik.boasson@adlinktech.com> - 0.22.1-2
- Autogenerated by Bloom

* Mon Apr 12 2021 Erik Boasson <erik.boasson@adlinktech.com> - 0.22.1-1
- Autogenerated by Bloom

* Thu Apr 08 2021 Erik Boasson <erik.boasson@adlinktech.com> - 0.22.0-1
- Autogenerated by Bloom

* Tue Apr 06 2021 Erik Boasson <erik.boasson@adlinktech.com> - 0.21.0-1
- Autogenerated by Bloom

* Fri Mar 19 2021 Erik Boasson <erik.boasson@adlinktech.com> - 0.20.0-1
- Autogenerated by Bloom

* Mon Mar 08 2021 Erik Boasson <erik.boasson@adlinktech.com> - 0.19.0-1
- Autogenerated by Bloom

