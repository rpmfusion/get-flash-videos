%global         rel_tag  20131203git2d46d08
Name:           get-flash-videos
Version:        1.24
Release:        11.%{?rel_tag}%{?dist}
Summary:        CLI tool to download flash video from websites
Group:          Applications/Communications
                # License breakdown in README.fedora
License:        ASL 2.0 and GPLv3+
URL:            http://code.google.com/p/get-flash-videos/
# rel_tag=20120714git162d964;
# srcdir=get-flash-videos
# git clone git://github.com/monsieurvideo/get-flash-videos.git $srcdir
# cd $srcdir;  git reset --hard ${rel_tag##*git}; cd ..
# tar czf $srcdir-$rel_tag.tar.gz --exclude .git $srcdir
Source0:        get-flash-videos-%{rel_tag}.tar.gz
Source1:        README.fedora
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(XML::Parser::PerlSAX)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(LWP::UserAgent::Determined)
BuildRequires:  perl(LWP::Protocol::https)
Buildrequires:  perl(Test::Simple)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(URI)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(XML::Simple)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Compress::Zlib)
Requires:       perl(Crypt::Rijndael)
Requires:       perl(Data::AMF)
Requires:       perl(Module::Find)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent::Determined)
Requires:       perl(Tie::IxHash)
Requires:       perl(XML::Simple)
Requires:       rtmpdump


%{?perl_default_filter}

%description
Download videos from various Flash-based video hosting sites, without
having to use the Flash player. Handy for saving videos for watching
offline, and means you don't have to keep upgrading Flash for sites that
insist on a newer version of the player.


%prep
%setup -q -n get-flash-videos
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
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc README README.fedora LICENSE
%{perl_vendorlib}/*
%{_bindir}/get_flash_videos
%{_bindir}/ff-get-flash-video
%{_mandir}/man1/*.1*


%changelog
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

* Sat Jan 31 2012 Alec Leamas <alec@nowhere.com>             1.24-1
- Intial packaging
