Summary:	CLCC - The OpenCL kernel compiler
Summary(pl.UTF-8):	CLCC - kompilator jąder OpenCL
Name:		clcc
Version:	0.3.0
Release:	14
License:	Boost v1.0
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/clcc/%{name}-%{version}-25-src.zip
# Source0-md5:	7ec003cc775d1cd06e789fb054c1d695
Patch0:		%{name}-shared.patch
Patch1:		%{name}-no-svn.patch
Patch2:		%{name}-opencl.patch
Patch3:		boost-1.59.patch
URL:		http://clcc.sourceforge.net/
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
Requires:	OpenCL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLCC is a compiler for OpenCL kernel source files. It is intended to
be a tool for application developers who need to incorporate OpenCL
source code into their programs and who want to verify their OpenCL
code actually gets compiled by the driver before their program tries
to compile it on-demand.

%description -l pl.UTF-8
CLCC to kompilator plików źródłowych jąder OpenCL. Jest pomyślany jako
narzędzie dla programistów potrzebujących wykorzystywać we własnych
programach kody źródłowe OpenCL i chcących zweryfikować je przed
skompilowaniem przez sterownik na żądanie w przypadku użycia przez
program.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
install -d build
cd build
%cmake .. \
	-DBOOST_LIBRARIES=%{_libdir}
%{__make} all clcc_doc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# not really useful for non-clcc developers
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt 
%attr(755,root,root) %{_bindir}/clcc
