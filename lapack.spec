Summary:	The LAPACK libraries for numerical linear algebra
Summary(pl.UTF-8):	Biblioteki numeryczne LAPACK do algebry liniowej
Name:		lapack
Version:	3.1.1
Release:	6
License:	freely distributable
Group:		Libraries
Source0:	http://www.netlib.org/lapack/%{name}-%{version}.tgz
# Source0-md5:	00b21551a899bcfbaa7b8443e1faeef9
Source1:	http://www.netlib.org/lapack/manpages-%{version}.tgz
# Source1-md5:	e5b46d8915f7cc8a1e50aa3e70c9f86e
Patch0:		%{name}-automake_support.patch
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
Summary:	Static BLAS libraries
Summary(pl.UTF-8):	Biblioteki statyczne BLAS
Group:		Development/Libraries
Requires:	blas-devel = %{version}-%{release}

%description -n blas-static
Static BLAS libraries.

%description -n blas-static -l pl.UTF-8
Biblioteki statyczne BLAS.

%prep
%setup -q -a1
%patch0 -p1
# directory INSTALL conflicts with file INSTALL needed by automake
mv -f INSTALL install
# or maybe it should fail while trying to overwrite a file?
cp -f install/*.f SRC/

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make} \
	LTTAG="--tag=F77"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# present both in blas and lapack
rm -f man/manl/{lsame,xerbla}.l

install -d $RPM_BUILD_ROOT%{_mandir}/man3
for d in manpages/man/manl/*.l manpages/blas/man/manl/*.l ; do
	install $d $RPM_BUILD_ROOT%{_mandir}/man3/`basename $d .l`.3
done

echo "%defattr(644,root,root,755)" > blasmans.list
find manpages/blas/man/manl -name "*.l" -printf "%{_mandir}/man3/%%f\n" | sed 's/\.l/.3*/' >> blasmans.list
echo "%defattr(644,root,root,755)" > mans.list
find manpages/man/manl -name "*.l" -printf "%{_mandir}/man3/%%f\n" | sed 's/\.l/.3*/' >> mans.list

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
%attr(755,root,root) %ghost %{_libdir}/liblapack.so.2

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
%attr(755,root,root) %ghost %{_libdir}/libblas.so.2

%files -n blas-devel -f blasmans.list
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libblas.so
%{_libdir}/libblas.la

%files -n blas-static
%defattr(644,root,root,755)
%{_libdir}/libblas.a
