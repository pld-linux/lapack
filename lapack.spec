Summary:	The LAPACK libraries for numerical linear algebra.
Name:		lapack
Version:	3.0
Release:	4
Copyright:	Freely distributable
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	http://www.netlib.org/lapack/%{name}.tar.bz2
Source1:	http://www.netlib.org/lapack/manpages.tar.bz2
Source2:	Makefile.blas
Source3:	Makefile.lapack
URL:		http://www.netlib.org/lapack/
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
is coded in Fortran77 and is built with egcs.

%package -n blas
Summary:	The BLAS (Basic Linear Algebra Subprograms) library for Linux.
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Obsoletes:	lapack-blas

%description -n blas
BLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra. BLAS provides a number of basic algorithms for
linear algebra. BLAS is fast and well-tested, was written in FORTRAN
77 and build with egcs. BLAS manual pages are available in the
blas-man package.

%package -n blas-man
Summary:	Man pages for BLAS (Basic Linear Algebra Subprograms) routines.
Group:		Documentation
Group(pl):	Dokumentacja
Obsoletes:	lapack-blas-man

%description -n blas-man
The blas-man package contains documentation for BLAS (Basic Linear
Algebra Subprograms) routines, in the form of man pages.

%package man
Summary:	Documentation for the LAPACK numerical linear algebra libraries.
Group:		Documentation
Group(pl):	Dokumentacja

%description man
Documentation, in the form of man pages, for the LAPACK numerical
linear algebra libraries.

%prep
%setup -q -n LAPACK
%setup -q -D -T -a 1 -n LAPACK
install %{SOURCE3} BLAS/SRC/Makefile
install %{SOURCE3} SRC/Makefile

%build
cd BLAS/SRC
FFLAGS="$RPM_OPT_FLAGS" make static
cp libblas.a ../..
%{__make} clean
FFLAGS="$RPM_OPT_FLAGS -fPIC" make shared
cp libblas.so.3.0.3 ../..
cd ../..
ln -s libblas.so.3.0.3 libblas.so
cd SRC
FFLAGS="$RPM_OPT_FLAGS" make static
cp liblapack.a ..
%{__make} clean
FFLAGS="$RPM_OPT_FLAGS -fPIC" make shared
cp liblapack.so.3.0.3 ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_prefix}/man/manl

cp -f liblapack.so.3.0.3 $RPM_BUILD_ROOT%{_libdir}/liblapack.so.3.0.3
cp -f libblas.so.3.0.3 $RPM_BUILD_ROOT%{_libdir}/libblas.so.3.0.3
cp -f libblas.a $RPM_BUILD_ROOT%{_libdir}/libblas.a
cp -f liblapack.a $RPM_BUILD_ROOT%{_libdir}/liblapack.a

cd blas/man/manl
gzip -9nf *
cd ../../..
echo "%defattr(-, root, root)" > blasmans
find blas/man/manl -type f -printf "%{_prefix}/man/manl/%f\n" > blasmans
cd man/manl
gzip -9nf *
cd ../..
echo "%defattr(-, root, root)" > lapackmans
find man/manl -type f -printf "%{_prefix}/man/manl/%f\n" > lapackmans

cp -f blas/man/manl/* $RPM_BUILD_ROOT%{_prefix}/man/manl
cp -f man/manl/* $RPM_BUILD_ROOT%{_prefix}/man/manl
cd $RPM_BUILD_ROOT%{_libdir}
ln -sf liblapack.so.3.0.3 liblapack.so
ln -sf liblapack.so.3.0.3 liblapack.so.3
ln -sf liblapack.so.3.0.3 liblapack.so.3.0
ln -sf libblas.so.3.0.3 libblas.so
ln -sf libblas.so.3.0.3 libblas.so.3
ln -sf libblas.so.3.0.3 libblas.so.3.0

%pre
ldconfig

%post
ldconfig

%pre -n blas
ldconfig

%post -n blas
ldconfig

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/liblapack.*

%files -n blas
%defattr(644,root,root,755)
%{_libdir}/libblas.*

%files -n blas-man -f blasmans
%defattr(644,root,root,755)

%files man -f lapackmans
%defattr(644,root,root,755)
