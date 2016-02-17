#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dos2unix
Version  : 7.3.3
Release  : 17
URL      : http://waterlan.home.xs4all.nl/dos2unix/dos2unix-7.3.3.tar.gz
Source0  : http://waterlan.home.xs4all.nl/dos2unix/dos2unix-7.3.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause-FreeBSD
Requires: dos2unix-bin
Requires: dos2unix-doc
Requires: dos2unix-locales
Requires: dos2unix-data

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
Requires: dos2unix-data

%description bin
bin components for the dos2unix package.


%package data
Summary: data components for the dos2unix package.
Group: Data

%description data
data components for the dos2unix package.


%package doc
Summary: doc components for the dos2unix package.
Group: Documentation

%description doc
doc components for the dos2unix package.


%package locales
Summary: locales components for the dos2unix package.
Group: Default

%description locales
locales components for the dos2unix package.


%prep
%setup -q -n dos2unix-7.3.3

%build
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make test

%install
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

%files data
%defattr(-,root,root,-)
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/dos2unix/*
%doc /usr/share/man/man1/*

%files locales -f dos2unix.lang 
%defattr(-,root,root,-)

