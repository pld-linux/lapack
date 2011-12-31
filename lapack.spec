# NOTE: when updating automake_support patch, look both on included
#  cmake suite and plain Makefiles - one of them is mostly outdated
#  (as of 3.4.0, cmake misses some files added in 3.4; also it
#   doesn't care about setting soname, so currently isn't worth using)
Summary:	The LAPACK libraries for numerical linear algebra
Summary(pl.UTF-8):	Biblioteki numeryczne LAPACK do algebry liniowej
Name:		lapack
Version:	3.4.0
%define	man_ver	3.4.0
Release:	1
License:	freely distributable
Group:		Libraries
Source0:	http://www.netlib.org/lapack/%{name}-%{version}.tgz
# Source0-md5:	02d5706ec03ba885fc246e5fa10d8c70
Source1:	http://www.netlib.org/lapack/manpages-%{man_ver}.tgz
# Source1-md5:	b9448c036dcfb174215ecbd207168fad
Patch0:		%{name}-automake_support.patch
Patch1:		blas-nan.patch
URL:		http://www.netlib.org/lapack/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-fortran
BuildRequires:	libtool >= 2:1.5
Requires:	blas = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision. LAPACK
is coded in Fortran77.

%description -l pl.UTF-8
LAPACK (Linear Algebra PACKage) jest standardową biblioteką numeryczną
do algebry liniowej. Dostarcza funkcje rozwiązywania: układów równań
liniowych, układów równań metodą najmniejszych kwadratów, problemów
własnych. Zawiera algorytmy faktoryzacji macierzy (LU, Cholesky'ego,
QR, SVD, Schura, uogólnioną Schura) i związanych z tym obliczeń (np.
przenumerowywanie w faktoryzacji Schura i estymację uwarunkowania).
LAPACK może obsługiwać macierze blokowe i pasmowe, ale nie rzadkie w
ogólnym przypadku. Zapewnia funkcjonalność dla macierzy rzeczywistych
i zespolonych, dla liczb pojedynczej i podwójnej precyzji. LAPACK jest
napisany w Fortranie 77.

%package devel
Summary:	LAPACK development files
Summary(pl.UTF-8):	Pliki programistyczne LAPACK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	blas-devel = %{version}-%{release}
Obsoletes:	lapack-man

%description devel
LAPACK development files.

%description devel -l pl.UTF-8
Pliki programistyczne LAPACK.

%package static
Summary:	Static LAPACK libraries
Summary(pl.UTF-8):	Biblioteki statyczne LAPACK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LAPACK libraries.

%description static -l pl.UTF-8
Biblioteki statyczne LAPACK.

%package -n blas
Summary:	The BLAS (Basic Linear Algebra Subprograms) library for Linux
Summary(pl.UTF-8):	Biblioteka BLAS (Basic Linear Algebra Subprograms) dla Linuksa
Group:		Libraries
Obsoletes:	lapack-blas

%description -n blas
BLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra. BLAS provides a number of basic algorithms for
linear algebra. BLAS is fast and well-tested, was written in FORTRAN
77.

Warning: this is a reference implementation from Netlib. If possible,
use version optimized for your architecture instead.

%description -n blas -l pl.UTF-8
BLAS (Basic Linear Algebra Subprograms) jest standardową biblioteką
numeryczną algebry. Dostarcza wiele podstawowych algorytmów dla
algebry liniowej. Jest szybka i dobrze przetestowana, została napisana
w Fortranie 77.

Ostrzeżenie: to jest implementacja przykładowa z repozytorium Netlib.
Jeżeli to możliwe, należy używać zamiast niej wersji zoptymalizowanej
pod daną architekturę.

%package -n blas-devel
Summary:	BLAS development files
Summary(pl.UTF-8):	Pliki programistyczne BLAS
Group:		Development/Libraries
Requires:	blas = %{version}-%{release}
Obsoletes:	blas-man

%description -n blas-devel
BLAS development files.

%description -n blas-devel -l pl.UTF-8
Pliki programistyczne BLAS.

%package -n blas-static
Summary:	Static BLAS library
Summary(pl.UTF-8):	Biblioteka statyczna BLAS
Group:		Development/Libraries
Requires:	blas-devel = %{version}-%{release}

%description -n blas-static
Static BLAS library.

%description -n blas-static -l pl.UTF-8
Biblioteka statyczna BLAS.

%package -n lapacke
Summary:	LAPACKE - native C interface to LAPACK library routines
Summary(pl.UTF-8):	LAPACKE - natywny interfejs C do procedur biblioteki LAPACK
Group:		Libraries
Requires:	lapack = %{version}-%{release}

%description -n lapacke
This library is a part of reference implementation for the C interface
to LAPACK project according to the specifications described at the
forum for the Intel(R) Math Kernel Library (Intel(R) MKL).

This implementation provides a native C interface to LAPACK routines
to facilitate usage of LAPACK functionality for C programmers.

%description -n lapacke -l pl.UTF-8
Ta bilioteka jest częścią implementacji referencyjnej interfejsu C do
projektu LAPACK, zgodnej ze specyfikacją opisaną na forum biblioteki
Intel(R) Math Kernel Library.

Ta implementacja udostępnia natywny interfejs C do procedur biblioteki
LAPACK, ułatwiając jej użycie programistom C.

%package -n lapacke-devel
Summary:	Header files for LAPACKE - native C interface to LAPACK
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LAPACKE - natywnego interfejsu C do biblioteki LAPACK
Group:		Development/Libraries
Requires:	lapack-devel = %{version}-%{release}
Requires:	lapacke = %{version}-%{release}

%description -n lapacke-devel
Header files for LAPACKE - native C interface to LAPACK.

%description -n lapacke-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LAPACKE - natywnego interfejsu C do
biblioteki LAPACK.

%package -n lapacke-static
Summary:	Static LAPACKE library - native C interface to LAPACK
Summary(pl.UTF-8):	Statyczna biblioteka LAPACKE - natywny interfejs C do biblioteki LAPACK
Group:		Development/Libraries
Requires:	lapacke-devel = %{version}-%{release}

%description -n lapacke-static
Static LAPACKE library - native C interface to LAPACK.

%description -n lapacke-static -l pl.UTF-8
Statyczna biblioteka LAPACKE - natywny interfejs C do biblioteki
LAPACK.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
# directory INSTALL conflicts with file INSTALL needed by automake
mv -f INSTALL INSTALLSRC
# copy selected routines; use INT_ETIME versions of second
cp -f INSTALLSRC/{ilaver,slamch,dlamch,second_INT_ETIME,dsecnd_INT_ETIME}.f SRC

# fill in lapacke files, omitting matgen and xblas-dependent files
sed -i -e "s,@LAPACKE_FILES@,$(cd lapacke/src ; ls -1 *.c ../utils/*.c | grep -Ev 'lagge|laghe|lagsy|latms|gbrfsx|gbsvxx|gerfsx|gesvxx|herfsx|hesvxx|porfsx|posvxx|syrfsx|sysvxx' |tr '\n' ' ')," lapacke/src/Makefile.am

# bogus
%{__rm} man/man3/_Users_julie_Desktop_lapack-*.3 \
	man/man3/__*.3
# duplicated...
%{__rm} man/man3/{INSTALL_ilaver,INSTALL_lsame,SRC_xerbla,SRC_xerbla_array}.f.3
# ...in BLAS and LAPACK sources; keep versions from BLAS
mv -f man/man3/BLAS_SRC_lsame.f.3 man/man3/lsame.f.3
mv -f man/man3/BLAS_SRC_xerbla.f.3 man/man3/xerbla.f.3
mv -f man/man3/BLAS_SRC_xerbla_array.f.3 man/man3/xerbla_array.f.3
sed -i -e 's,man3/INSTALL_,man3/,' man/man3/LSAME.3
sed -i -e 's,man3/SRC_,man3/,' man/man3/{ILAVER,XERBLA,XERBLA_ARRAY}.3
# ...in SRC and INSTALL dirs
mv -f man/man3/SRC_ilaver.f.3 man/man3/ilaver.f.3
# [sd]lamchf77.f is not used
%{__rm} man/man3/{DLAMC1,DLAMC2,DLAMC4,DLAMC5,dlamchf77.f}.3
%{__rm} man/man3/{SLAMC1,SLAMC2,SLAMC4,SLAMC5,slamchf77.f}.3

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# install man pages, distributing them among blas-devel and lapack-devel
install -d $RPM_BUILD_ROOT%{_mandir}/man3
echo "%defattr(644,root,root,755)" > blasmans.list
echo "%defattr(644,root,root,755)" > mans.list
for f in man/man3/*.3 ; do
	cp -p "$f" $RPM_BUILD_ROOT%{_mandir}/man3
	bn=$(basename $f)
	if echo "$bn" | grep '\.f\.3$' ; then
		ffn="${bn%.3}"
	elif grep '\.f\.3$' "$f" ; then
		ffn=$(sed -e '1s,^\.so man3/\(.*\.f\)\.3,\1,' $f)
	else
		echo "Unknown manpage: $f"
		exit 1
	fi
	if [ -f "BLAS/SRC/$ffn" ]; then
		echo "%{_mandir}/man3/${bn}*" >> blasmans.list
	elif [ -f "SRC/$ffn" -o -f "INSTALLSRC/$ffn" ]; then
		echo "%{_mandir}/man3/${bn}*" >> mans.list
	else
		echo "Unknown manpage: $f (source file: $ffn)"
		exit 1
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post   -n blas -p /sbin/ldconfig
%postun -n blas -p /sbin/ldconfig

%post   -n lapacke -p /sbin/ldconfig
%postun -n lapacke -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/liblapack.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblapack.so.2

%files devel -f mans.list
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblapack.so
%{_libdir}/liblapack.la
%{_pkgconfigdir}/lapack.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblapack.a

%files -n blas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libblas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libblas.so.2

%files -n blas-devel -f blasmans.list
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libblas.so
%{_libdir}/libblas.la
%{_pkgconfigdir}/blas.pc

%files -n blas-static
%defattr(644,root,root,755)
%{_libdir}/libblas.a

%files -n lapacke
%defattr(644,root,root,755)
%doc lapacke/{LICENSE,README}
%attr(755,root,root) %{_libdir}/liblapacke.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblapacke.so.2

%files -n lapacke-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblapacke.so
%{_libdir}/liblapacke.la
%{_includedir}/lapacke*.h

%files -n lapacke-static
%defattr(644,root,root,755)
%{_libdir}/liblapacke.a
