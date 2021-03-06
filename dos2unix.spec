#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x38C1F572B12725BE (waterlan@xs4all.nl)
#
Name     : dos2unix
Version  : 7.4.2
Release  : 31
URL      : https://sourceforge.net/projects/dos2unix/files/dos2unix/7.4.2/dos2unix-7.4.2.tar.gz
Source0  : https://sourceforge.net/projects/dos2unix/files/dos2unix/7.4.2/dos2unix-7.4.2.tar.gz
Source1  : https://sourceforge.net/projects/dos2unix/files/dos2unix/7.4.2/dos2unix-7.4.2.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause-FreeBSD
Requires: dos2unix-bin = %{version}-%{release}
Requires: dos2unix-locales = %{version}-%{release}
Requires: dos2unix-man = %{version}-%{release}

%description
dos2unix - DOS/Mac to Unix and vice versa text file format converter.
FILE LIST
INSTALL.txt           : How to build and install.
COPYING.txt           : distribution license.
NEWS.txt              : Basic change log for users.
ChangeLog.txt         : Detailed change log for programmers.
TODO.txt              : Things to do.
BUGS.txt              : Known bugs and instructions on reporting new ones.
DEVEL.txt             : Information about dos2unix' implementation choices.
man/man1/dos2unix.txt : Dos2unix manual, text format.
man/man1/dos2unix.htm : Dos2unix manual, HTML format.

%package bin
Summary: bin components for the dos2unix package.
Group: Binaries

%description bin
bin components for the dos2unix package.


%package doc
Summary: doc components for the dos2unix package.
Group: Documentation
Requires: dos2unix-man = %{version}-%{release}

%description doc
doc components for the dos2unix package.


%package locales
Summary: locales components for the dos2unix package.
Group: Default

%description locales
locales components for the dos2unix package.


%package man
Summary: man components for the dos2unix package.
Group: Default

%description man
man components for the dos2unix package.


%prep
%setup -q -n dos2unix-7.4.2
cd %{_builddir}/dos2unix-7.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602627641
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export SOURCE_DATE_EPOCH=1602627641
rm -rf %{buildroot}
%make_install
%find_lang dos2unix

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dos2unix
/usr/bin/mac2unix
/usr/bin/unix2dos
/usr/bin/unix2mac

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/dos2unix/*

%files man
%defattr(0644,root,root,0755)
/usr/share/man/de/man1/dos2unix.1
/usr/share/man/de/man1/mac2unix.1
/usr/share/man/de/man1/unix2dos.1
/usr/share/man/de/man1/unix2mac.1
/usr/share/man/es/man1/dos2unix.1
/usr/share/man/es/man1/mac2unix.1
/usr/share/man/es/man1/unix2dos.1
/usr/share/man/es/man1/unix2mac.1
/usr/share/man/fr/man1/dos2unix.1
/usr/share/man/fr/man1/mac2unix.1
/usr/share/man/fr/man1/unix2dos.1
/usr/share/man/fr/man1/unix2mac.1
/usr/share/man/man1/dos2unix.1
/usr/share/man/man1/mac2unix.1
/usr/share/man/man1/unix2dos.1
/usr/share/man/man1/unix2mac.1
/usr/share/man/nl/man1/dos2unix.1
/usr/share/man/nl/man1/mac2unix.1
/usr/share/man/nl/man1/unix2dos.1
/usr/share/man/nl/man1/unix2mac.1
/usr/share/man/pl/man1/dos2unix.1
/usr/share/man/pl/man1/mac2unix.1
/usr/share/man/pl/man1/unix2dos.1
/usr/share/man/pl/man1/unix2mac.1
/usr/share/man/pt_BR/man1/dos2unix.1
/usr/share/man/pt_BR/man1/mac2unix.1
/usr/share/man/pt_BR/man1/unix2dos.1
/usr/share/man/pt_BR/man1/unix2mac.1
/usr/share/man/sv/man1/dos2unix.1
/usr/share/man/sv/man1/mac2unix.1
/usr/share/man/sv/man1/unix2dos.1
/usr/share/man/sv/man1/unix2mac.1
/usr/share/man/uk/man1/dos2unix.1
/usr/share/man/uk/man1/mac2unix.1
/usr/share/man/uk/man1/unix2dos.1
/usr/share/man/uk/man1/unix2mac.1
/usr/share/man/zh_CN/man1/dos2unix.1
/usr/share/man/zh_CN/man1/mac2unix.1
/usr/share/man/zh_CN/man1/unix2dos.1
/usr/share/man/zh_CN/man1/unix2mac.1

%files locales -f dos2unix.lang
%defattr(-,root,root,-)

