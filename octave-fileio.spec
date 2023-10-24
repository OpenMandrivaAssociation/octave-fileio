%global octpkg fileio

Summary:	I/O function for files holding structured data, such as JSON and XML files
Name:		octave-fileio
Version:	1.2.2
Release:	1
License:	MIT
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/fileio/
Url:		https://github.com/reprostat/fileio
Source0:	https://github.com/reprostat/fileio/archive/refs/tags/%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 7.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
I/O function for files holding structured data, such as JSON and XML 
files.

%files
%license COPYING LICENSE
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

