VERSION=1.25.99.03

git pull
rpmdev-bumpspec -n $VERSION -c "Update get-flash-videos to $VERSION" get-flash-videos.spec
spectool -g get-flash-videos.spec
rfpkg new-sources ./get-flash-videos-$VERSION.tar.gz
rfpkg ci -c && git show
echo Press enter to continue; read dummy;
rfpkg push && rfpkg build --nowait
