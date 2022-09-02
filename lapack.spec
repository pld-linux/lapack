#
# Conditional build:
%bcond_without	static_libs	# static libraries
%bcond_without	tests		# unit tests
%bcond_with	xblas		# use xblas

Summary:	The LAPACK libraries for numerical linear algebra
Summary(pl.UTF-8):	Biblioteki numeryczne LAPACK do algebry liniowej
Name:		lapack
Version:	3.10.1
Release:	1
License:	BSD-like
Group:		Libraries
#Source0Download: https://github.com/Reference-LAPACK/lapack/releases
Source0:	https://github.com/Reference-LAPACK/lapack/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	722407217a080a0012ae3d6913fb8008
Source1:	https://netlib.org/lapack/manpages.tgz
# Source1-md5:	104899b545cdb6e502afd66aeb5fe0f0
Patch0:		blas-nan.patch
URL:		https://netlib.org/lapack/
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gcc-fortran
%{?with_xblas:BuildRequires:	xblas-devel}
Requires:	blas = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# missing __stack_chk_fail symbol when only Fortran sources used
%undefine	_fortify_cflags
%undefine	_ssp_cflags

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
Obsoletes:	lapack-man < 3.0-3

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
URL:		https://netlib.org/blas/
Obsoletes:	lapack-blas < 3.1

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
URL:		http://www.netlib.org/blas/
Requires:	blas = %{version}-%{release}
Obsoletes:	blas-man < 3.0-3

%description -n blas-devel
BLAS development files.

%description -n blas-devel -l pl.UTF-8
Pliki programistyczne BLAS.

%package -n blas-static
Summary:	Static BLAS library
Summary(pl.UTF-8):	Biblioteka statyczna BLAS
Group:		Development/Libraries
URL:		http://www.netlib.org/blas/
Requires:	blas-devel = %{version}-%{release}

%description -n blas-static
Static BLAS library.

%description -n blas-static -l pl.UTF-8
Biblioteka statyczna BLAS.

%package -n cblas
Summary:	C Standard Interface to BLAS Basic Linear Algebra Subprograms
Summary(pl.UTF-8):	Interfejs C do procedur BLAS (Basic Linear Algebra Subprograms)
Group:		Libraries
URL:		http://www.netlib.org/blas/#_cblas
Requires:	blas = %{version}-%{release}

%description -n cblas
C Standard Interface to BLAS Basic Linear Algebra Subprograms.

%description -n cblas -l pl.UTF-8
Interfejs C do procedur BLAS (Basic Linear Algebra Subprograms -
podstawowych procedur algebry liniowej).

%package -n cblas-devel
Summary:	Header files of C Standard Interface to BLAS
Summary(pl.UTF-8):	Pliki nagłówkowe interfejsu C do BLAS
Group:		Libraries
URL:		http://www.netlib.org/blas/#_cblas
Requires:	blas-devel = %{version}-%{release}
Requires:	cblas = %{version}-%{release}

%description -n cblas-devel
Header files of C Standard Interface to BLAS.

%description -n cblas-devel -l pl.UTF-8
Pliki nagłówkowe interfejsu C do BLAS.

%package -n cblas-static
Summary:	Static CBLAS library
Summary(pl.UTF-8):	Statyczna biblioteka CBLAS
Group:		Libraries
URL:		http://www.netlib.org/blas/#_cblas
Requires:	cblas-devel = %{version}-%{release}

%description -n cblas-static
Static CBLAS library.

%description -n cblas-static -l pl.UTF-8
Statyczna biblioteka CBLAS.

%package -n lapacke
Summary:	LAPACKE - native C interface to LAPACK library routines
Summary(pl.UTF-8):	LAPACKE - natywny interfejs C do procedur biblioteki LAPACK
Group:		Libraries
URL:		http://www.netlib.org/lapack/lapacke.html
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
URL:		http://www.netlib.org/lapack/lapacke.html
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
URL:		http://www.netlib.org/lapack/lapacke.html
Requires:	lapacke-devel = %{version}-%{release}

%description -n lapacke-static
Static LAPACKE library - native C interface to LAPACK.

%description -n lapacke-static -l pl.UTF-8
Statyczna biblioteka LAPACKE - natywny interfejs C do biblioteki
LAPACK.

%prep
%setup -q -a1
%patch0 -p1
# copy selected routines; use INT_ETIME versions of second
# FIXME? CMakeLists doesn't handle second
#cp -f INSTALLSRC/{second_INT_ETIME,dsecnd_INT_ETIME}.f SRC

# bogus
%{__rm} man/man3/_Users_julielangou_Documents_GitHub_lapack_*.3
%{__rm} man/man3/groups-usr.dox.3
# duplicated...
%{__rm} man/man3/{SRC_xerbla,SRC_xerbla_array}.f.3
# ...in BLAS and LAPACK sources; keep versions from BLAS
%{__mv} man/man3/BLAS_SRC_xerbla.f.3 man/man3/xerbla.f.3
%{__mv} man/man3/BLAS_SRC_xerbla_array.f.3 man/man3/xerbla_array.f.3
%{__sed} -i -e 's/BLAS_SRC_//' man/man3/{xerbla,xerbla_array}.3
# in base and variants; adjust .so links to use base
%{__sed} -i -e 's/VARIANTS_qr_LL_//' man/man3/zgeqrf.3
%{__sed} -i -e 's/VARIANTS_lu_CR_//' man/man3/zgetrf.3
%{__sed} -i -e 's/VARIANTS_cholesky_RL_//' man/man3/zpotrf.3
# not used variants of some procedures
%{__rm} man/man3/{VARIANTS_*,sceil,sceil.f}.3
# documentation for examples
%{__rm} man/man3/{LDA,LDB,N,NRHS,example_*,lapacke_example_aux.*,main,print_*}.3
# too common names
%{__mv} man/man3/{testing,lapacktesting}.3
%{__mv} man/man3/{level1,blaslevel1}.3
%{__mv} man/man3/{level2,blaslevel2}.3
%{__mv} man/man3/{level3,blaslevel3}.3

%build
%if %{with static_libs}
install -d build-static
cd build-static
%cmake .. \
	-DBUILD_DEPRECATED=ON \
	-DBUILD_SHARED_LIBS=OFF \
	-DCBLAS=ON \
	-DLAPACKE_WITH_TMG=ON \
	%{?with_xblas:-DUSE_XBLAS=ON}
%{__make}
cd ..
%endif

install -d build
cd build
%cmake .. \
	-DBUILD_DEPRECATED=ON \
	%{?with_tests:-DBUILD_TESTING=ON} \
	-DCBLAS=ON \
	-DLAPACKE_WITH_TMG=ON \
	%{?with_xblas:-DUSE_XBLAS=ON}
%{__make}

%{?with_tests:ctest}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# install man pages, distributing them among blas-devel and lapack-devel
install -d $RPM_BUILD_ROOT%{_mandir}/man3
echo "%defattr(644,root,root,755)" > blasmans.list
echo "%defattr(644,root,root,755)" > mans.list
echo "%defattr(644,root,root,755)" > lapackemans.list
BLAS_ADDITIONAL='blas|blaslevel[123]|blastesting|aux_blas|(complex|complex16|double|single)_blas_(level[123]|testing)'
LAPACK_ADDITIONAL='lapack|lapacktesting|OTHERauxiliary|(aux|auxiliary|complex|complex16|computational|double|eigen|real|sing|solve|variants)?(GB|GE|GT|HE|OTHER|PO|PT|SY)(auxiliary|computational|eigen|sing|solve)?|((aux|complex|complex16|double|real|single)_)?(eig|lin|matgen)|variants(GE|OTHER|PO)computational'
MANS_ADDITIONAL="$BLAS_ADDITIONAL|$LAPACK_ADDITIONAL"
for f in man/man3/*.3 ; do
	cp -p "$f" $RPM_BUILD_ROOT%{_mandir}/man3
	bn=$(basename $f)
	if echo "$bn" | grep '\.[Fcfh]\.3$' ; then
		ffn="${bn%.3}"
	elif echo "$bn" | grep -E "^($MANS_ADDITIONAL)\.3\$" ; then
		ffn="${bn%.3}"
	elif grep '^\.so man3/.*\.[Fcfh]\.3$' "$f" ; then
		ffn=$(sed -e '1s,^\.so man3/\(.*\.[Fcfh]\)\.3,\1,' $f)
	elif grep -E "^\.so man3/($MANS_ADDITIONAL)\.3" "$f"; then
		ffn=$(sed -e '1s,^\.so man3/\([^.]*\)\.3,\1,' $f)
	else
		echo "Unknown manpage: $f"
		exit 1
	fi
	if [ -f "BLAS/SRC/$ffn" ] || echo "$ffn" | grep -E "^($BLAS_ADDITIONAL)\$" ; then
		echo "%{_mandir}/man3/${bn}*" >> blasmans.list
	elif [ -f "SRC/$ffn" -o -f "INSTALLSRC/$ffn" ] || echo "$ffn" | grep -E "^($LAPACK_ADDITIONAL)\$"; then
		echo "%{_mandir}/man3/${bn}*" >> mans.list
	elif [ -f "LAPACKE/include/$ffn" -o -f "LAPACKE/src/$ffn" -o -f "LAPACKE/utils/$ffn" ]; then
		echo "%{_mandir}/man3/${bn}*" >> lapackemans.list
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

%post   -n cblas -p /sbin/ldconfig
%postun -n cblas -p /sbin/ldconfig

%post   -n lapacke -p /sbin/ldconfig
%postun -n lapacke -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/liblapack.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblapack.so.3

%files devel -f mans.list
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblapack.so
%{_includedir}/lapack.h
%{_pkgconfigdir}/lapack.pc
%{_libdir}/cmake/lapack-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liblapack.a
%endif

%files -n blas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libblas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libblas.so.3

%files -n blas-devel -f blasmans.list
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libblas.so
%{_pkgconfigdir}/blas.pc

%if %{with static_libs}
%files -n blas-static
%defattr(644,root,root,755)
%{_libdir}/libblas.a
%endif

%files -n cblas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcblas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcblas.so.3

%files -n cblas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcblas.so
%{_includedir}/cblas*.h
%{_pkgconfigdir}/cblas.pc
%{_libdir}/cmake/cblas-%{version}

%if %{with static_libs}
%files -n cblas-static
%defattr(644,root,root,755)
%{_libdir}/libcblas.a
%endif

%files -n lapacke -f lapackemans.list
%defattr(644,root,root,755)
%doc LAPACKE/{LICENSE,README}
%attr(755,root,root) %{_libdir}/liblapacke.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblapacke.so.3
%attr(755,root,root) %{_libdir}/libtmglib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtmglib.so.3

%files -n lapacke-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblapacke.so
%attr(755,root,root) %{_libdir}/libtmglib.so
%{_includedir}/lapacke*.h
%{_pkgconfigdir}/lapacke.pc
%{_libdir}/cmake/lapacke-%{version}

%if %{with static_libs}
%files -n lapacke-static
%defattr(644,root,root,755)
%{_libdir}/liblapacke.a
%{_libdir}/libtmglib.a
%endif
