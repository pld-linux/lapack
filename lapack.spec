Summary:	The LAPACK libraries for numerical linear algebra.
Name:		lapack
Version:	3.0
Release:	1
Copyright:	Freely distributable
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	http://www.netlib.org/lapack/%{name}.tar.bz2
Source1:	http://www.netlib.org/lapack/manpages.tar.bz2
#Source2:	Makefile.blas
#Source3:	Makefile.lapack
Patch0:		%{name}-automake_support.patch
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

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
%{name} header files.

%description -l pl devel
Pliki nag³ówkowe %{name}.

%package static
Summary:	Static %{name} libraries
Summary(pl):	Biblioteki statyczne %{name}
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static %{name} libraries.

%description -l pl static
Biblioteki statyczne %{name}.


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

%package -n blas-devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	blas = %{version}

%description -n blas-devel
%{name} header files.

%description -l pl -n blas-devel
Pliki nag³ówkowe %{name}.

%package -n blas-static
Summary:	Static %{name} libraries
Summary(pl):	Biblioteki statyczne %{name}
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	blas-devel = %{version}

%description -n blas-static
Static %{name} libraries.

%description -l pl -n blas-static
Biblioteki statyczne %{name}.

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
%setup -q -a1 -n LAPACK
%patch0 -p1
# directory INSTALL conflicts with file INSTALL needed by automake
mv -f INSTALL install
>INSTALL
>AUTHORS
>ChangeLog
>NEWS
>COPYING
>config.h.in

%build
aclocal
autoheader
automake --add-missing
autoconf
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/manl
gzip -9nf blas/man/manl/*.l man/manl/*.l
install blas/man/manl/* man/manl/* $RPM_BUILD_ROOT%{_mandir}/manl

echo "%defattr(644, root, root, 755)" > blasmans.list
find blas/man/manl -name "*.gz" -printf "%{_mandir}/manl/%%f\n" >> blasmans.list
echo "%defattr(644, root, root, 755)" > mans.list
find man/manl -name "*.gz" -printf "%{_mandir}/manl/%%f\n" >> mans.list

gzip -9nf README

%post           -p /sbin/ldconfig
%postun         -p /sbin/ldconfig
%post   -n blas -p /sbin/ldconfig
%postun -n blas -p /sbin/ldconfig

%clean
rm -fr $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_libdir}/liblapack.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/liblapack.so

%files static
%defattr(644,root,root,755)
%{_libdir}/liblapack.a

%files -n blas 
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libblas.so.*.*.*

%files -n blas-devel
%defattr(644,root,root,755)
%{_libdir}/libblas.so

%files -n blas-static
%defattr(644,root,root,755)
%{_libdir}/libblas.a


%files -n blas-man -f blasmans.list
%defattr(644,root,root,755)

%files man -f mans.list
%defattr(644,root,root,755)
