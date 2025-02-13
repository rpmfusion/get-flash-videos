Name:           get-flash-videos
Version:        1.25.99.03
Release:        14%{?dist}
Summary:        CLI tool to download flash video from websites
Group:          Applications/Communications
                # License breakdown in README.fedora
License:        ASL 2.0 and GPLv3+
URL:            https://github.com/monsieurvideo/get-flash-videos
# rel_tag=20120714git162d964;
# srcdir=get-flash-videos
# git clone git://github.com/monsieurvideo/get-flash-videos.git $srcdir
# cd $srcdir;  git reset --hard ${rel_tag##*git}; cd ..
# tar czf $srcdir-$rel_tag.tar.gz --exclude .git $srcdir
Source0:        https://github.com/monsieurvideo/get-flash-videos/archive/%{version}/get-flash-videos-%{version}.tar.gz
Source1:        README.fedora
BuildArch:      noarch

# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Modules
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::Blowfish_PP)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Data::AMF::Packet)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTML::Tree)
BuildRequires:  perl(integer)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Memoize)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Net::Netrc)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::localtime)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::Find)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(warnings)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(WWW::Mechanize::Link)
BuildRequires:  perl(XML::Simple)
# Scripts
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Text::Wrap)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(utf8)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Compress::Zlib)
Requires:       perl(Crypt::Rijndael)
Requires:       perl(Cwd)
Requires:       perl(Data::AMF::Packet)
Requires:       perl(Digest::MD5)
Requires:       perl(Digest::SHA)
Requires:       perl(File::Copy)
Requires:       perl(File::Path)
Requires:       perl(File::Spec)
Requires:       perl(Net::Netrc)
Requires:       perl(Term::ReadKey)
Requires:       perl(URI::Find)
Requires:       perl(XML::Simple)
Requires:       rtmpdump
Recommends:     perl(DBI)
Recommends:     perl(LWP::Simple)
Recommends:     perl(Memoize)

%{?perl_default_filter}

%description
Download videos from various Flash-based video hosting sites, without
having to use the Flash player. Handy for saving videos for watching
offline, and means you don't have to keep upgrading Flash for sites that
insist on a newer version of the player.


%prep
%setup -q
cp %{SOURCE1} .


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
# Search is  currently broken, see README.fedora
rm t/google_video_search.t


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
cp -a utils/ff-get-flash-video $RPM_BUILD_ROOT%{_bindir}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%license LICENSE README.fedora
%doc README.md
%{perl_vendorlib}/*
%{_bindir}/get_flash_videos
%{_bindir}/ff-get-flash-video
%{_mandir}/man1/*.1*


%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.25.99.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.25.99.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.25.99.03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.25.99.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.25.99.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Tue Jun 21 2022 aul Howarth <paul@city-fan.org> - 1.25.99.03-9
- Perl 5.36 rebuild

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.25.99.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.25.99.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Leigh Scott <leigh123linux@gmail.com> - 1.25.99.03-6
- Rebuild for new perl version

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.25.99.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.25.99.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Paul Howarth <paul@city-fan.org> - 1.25.99.03-3
- Perl 5.32 rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.25.99.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Sérgio Basto <sergio@serjux.com> - 1.25.99.03-1
- Update get-flash-videos to 1.25.99.03

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.25.94-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.25.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.25.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.25.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Sérgio Basto <sergio@serjux.com> - 1.25.94-1
- Update get-flash-videos to 1.25.94

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.25.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Sérgio Basto <sergio@serjux.com> - 1.25.92-1
- Update to get-flash-videos-1.25.92

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Paul Howarth <paul@city-fan.org> - 1.24-12.20131203git2d46d08
- Specify all dependencies
- Don't need to remove empty directories from the buildroot
- Use %%license

* Fri Dec 27 2013 leamas@nowhere.net - 1.24-11.20131203git2d46d08
- Rebuild after F20 branching

* Tue Dec 03 2013 Alec Leamas <alec@nowhere.com> - 1.24-10.20131203git2d46d08
- Updating to latest upstream
- Add new Requires/BR:

* Sat Oct 13 2012 Alec Leamas <alec@nowhere.com> 1.24-9.20120714gitc52cdf6
- Updating to latest upstream
- Handle new utility ff-get-flash-video

* Sat Jul 14 2012 Alec Leamas <alec@nowhere.com> 1.24-7.20120714git162d964
- Fixing build errors

* Fri Jul 13 2012 Alec Leamas <alec@nowhere.com> 1.24-6.20120713git162d964
- Fixing build errors

* Fri Jul 13 2012 Alec Leamas <alec@nowhere.com> 1.24-5.20120713git162d964
- Updating to new git release

* Mon Apr 09 2012 Alec Leamas <alec@nowhere.com> 1.24-4.20120409gita965329
- Updating to git head, resolving the video search problem
- Adding LICENSE to docs.

* Fri Feb 24 2012 Alec Leamas <alec@nowhere.com> 1.24-3.20120224git8abc6c6
- Updating license break-down

* Fri Feb 24 2012 Alec Leamas <alec@nowhere.com> 1.24-3.20120224git8abc6c6
- Re-enabling Require: perl(:MODULE_COMPAT_...)
- Resolving naming mess, illegal name of spec, bad name of source.

* Tue Feb 21 2012 Alec Leamas <alec@nowhere.com> 1.24-3.20120205git8abc6c6
- Rewriting deps using Perl(Module) syntax.
- Removing auto-detected Requires.
- Updating Requires: from upstream website.

* Sun Feb 05 2012 Alec Leamas <alec@nowhere.com> 1.24-2.20120205git8abc6c6
- Moving to latest git

* Tue Jan 31 2012 Alec Leamas <alec@nowhere.com>             1.24-1
- Intial packaging
