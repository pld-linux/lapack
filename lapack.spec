Summary:	The LAPACK libraries for numerical linear algebra
Summary(pl):	Biblioteki numeryczne LAPACK do algebry liniowej
Name:		lapack
Version:	3.0
Release:	17
License:	freely distributable
Group:		Development/Libraries
Source0:	http://www.netlib.org/lapack/%{name}.tgz
# Source0-md5:	a24f59304f87b78cdc7da2ae59c98664
Source1:	http://www.netlib.org/lapack/manpages.tgz
# Source1-md5:	50efab6cd73a9429584f7f1537f1727f
Patch0:		%{name}-automake_support.patch
Patch1:		%{name}-20010525.patch
URL:		http://www.netlib.org/lapack/
BuildRequires:	gcc-g77
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.2-9
Requires:	blas = %{version}
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

%description -l pl
LAPACK (Linear Algebra PACKage) jest standardow± bibliotek± numeryczn±
do algebry liniowej. Dostarcza funkcje rozwi±zywania: uk³adów równañ
liniowych, uk³adów równañ metod± najmniejszych kwadratów, problemów
w³asnych. Zawiera algorytmy faktoryzacji macierzy (LU, Cholesky'ego,
QR, SVD, Schura, uogólnion± Schura) i zwi±zanych z tym obliczeñ (np.
przenumerowywanie w faktoryzacji Schura i estymacjê uwarunkowania).
LAPACK mo¿e obs³ugiwaæ macierze blokowe i pasmowe, ale nie rzadkie w
ogólnym przypadku. Zapewnia funkcjonalno¶æ dla macierzy rzeczywistych
i zespolonych, dla liczb pojedynczej i podwójnej precyzji. LAPACK jest
napisany w Fortranie 77.

%package devel
Summary:	LAPACK header files
Summary(pl):	Pliki nag³ówkowe LAPACK
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	blas-devel = %{version}
Obsoletes:	lapack-man

%description devel
LAPACK header files.

%description devel -l pl
Pliki nag³ówkowe LAPACK.

%package static
Summary:	Static LAPACK libraries
Summary(pl):	Biblioteki statyczne LAPACK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static LAPACK libraries.

%description static -l pl
Biblioteki statyczne LAPACK.

%package -n blas
Summary:	The BLAS (Basic Linear Algebra Subprograms) library for Linux
Summary(pl):	Biblioteka BLAS (Basic Linear Algebra Subprograms) dla Linuksa
Group:		Development/Libraries
Obsoletes:	lapack-blas

%description -n blas
BLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra. BLAS provides a number of basic algorithms for
linear algebra. BLAS is fast and well-tested, was written in FORTRAN
77.

%description -n blas -l pl
BLAS (Basic Linear Algebra Subprograms) jest standardow± bibliotek±
numeryczn± algebry. Dostarcza wiele podstawowych algorytmów dla
algebry liniowej. Jest szybka i dobrze przetestowana, zosta³a napisana
w Fortranie 77.

%package -n blas-devel
Summary:	BLAS header files
Summary(pl):	Pliki nag³ówkowe BLAS
Group:		Development/Libraries
Requires:	blas = %{version}
Obsoletes:	blas-man

%description -n blas-devel
BLAS header files.

%description -n blas-devel -l pl
Pliki nag³ówkowe BLAS.

%package -n blas-static
Summary:	Static BLAS libraries
Summary(pl):	Biblioteki statyczne BLAS
Group:		Development/Libraries
Requires:	blas-devel = %{version}

%description -n blas-static
Static BLAS libraries.

%description -n blas-static -l pl
Biblioteki statyczne BLAS.

%prep
%setup -q -a1 -n LAPACK
%patch0 -p1
%patch1 -p1
# directory INSTALL conflicts with file INSTALL needed by automake
mv -f INSTALL install

%build
rm -f ltmain.sh missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

# libtool 1.4d requires --tag for g77, libtool 1.4.2 fails when --tag is passed
LTTAG=""
grep -q -e '--tag' `which libtool` && LTTAG="--tag=F77"

%{__make} LTTAG="$LTTAG"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

# present both in blas and lapack
rm -f man/manl/{lsame,xerbla}.l

install -d $RPM_BUILD_ROOT%{_mandir}/man3
for d in man/manl/*.l blas/man/manl/*.l ; do
	install $d $RPM_BUILD_ROOT%{_mandir}/man3/`basename $d .l`.3
done

echo "%defattr(644, root, root, 755)" > blasmans.list
find blas/man/manl -name "*.l" -printf "%{_mandir}/man3/%%f\n" | sed 's/\.l/.3*/' >> blasmans.list
echo "%defattr(644, root, root, 755)" > mans.list
find man/manl -name "*.l" -printf "%{_mandir}/man3/%%f\n" | sed 's/\.l/.3*/' >> mans.list

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post   -n blas -p /sbin/ldconfig
%postun -n blas -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/liblapack.so.*.*.*

%files devel -f mans.list
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblapack.so
%{_libdir}/liblapack.la

%files static
%defattr(644,root,root,755)
%{_libdir}/liblapack.a

%files -n blas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libblas.so.*.*.*

%files -n blas-devel -f blasmans.list
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libblas.so
%{_libdir}/libblas.la

%files -n blas-static
%defattr(644,root,root,755)
%{_libdir}/libblas.a
