#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : osprofiler
Version  : 2.5.0
Release  : 39
URL      : https://tarballs.openstack.org/osprofiler/osprofiler-2.5.0.tar.gz
Source0  : https://tarballs.openstack.org/osprofiler/osprofiler-2.5.0.tar.gz
Source99 : https://tarballs.openstack.org/osprofiler/osprofiler-2.5.0.tar.gz.asc
Summary  : OpenStack Profiler Library
Group    : Development/Tools
License  : Apache-2.0
Requires: osprofiler-bin
Requires: osprofiler-python3
Requires: osprofiler-license
Requires: osprofiler-python
Requires: WebOb
Requires: netaddr
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.serialization
Requires: oslo.utils
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the osprofiler package.
Group: Binaries
Requires: osprofiler-license = %{version}-%{release}

%description bin
bin components for the osprofiler package.


%package license
Summary: license components for the osprofiler package.
Group: Default

%description license
license components for the osprofiler package.


%package python
Summary: python components for the osprofiler package.
Group: Default
Requires: osprofiler-python3 = %{version}-%{release}

%description python
python components for the osprofiler package.


%package python3
Summary: python3 components for the osprofiler package.
Group: Default
Requires: python3-core

%description python3
python3 components for the osprofiler package.


%prep
%setup -q -n osprofiler-2.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539116388
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/osprofiler
cp LICENSE %{buildroot}/usr/share/doc/osprofiler/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/osprofiler

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/osprofiler/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
