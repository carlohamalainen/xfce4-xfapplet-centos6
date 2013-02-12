xfce4-xfapplet-centos6
======================

Patch of the xfce4-xfapplet-plugin-0.1.0-1.el5.centos package to install on Centos 6.3.

To build the RPM from source:

    sudo yum install rpm-build

    git clone https://github.com/carlohamalainen/xfce4-xfapplet-centos6.git
    cd xfce4-xfapplet-centos6
    export RPMWORK=`pwd`

    mkdir ${RPMWORK}/BUILD
    mkdir ${RPMWORK}/RPMS
    mkdir ${RPMWORK}/SOURCES
    mkdir ${RPMWORK}/SPECS
    mkdir ${RPMWORK}/SRPMS

Edit $HOME/.rpmmacros:

    %_topdir    /your/working/directory/as/set/above
    %_tmppath   %{_topdir}/tmp

Now build the RPM:

    rpmbuild -bp ${RPMWORK}/SPECS/foo.spec
    rpmbuild -bc ${RPMWORK}/SPECS/foo.spec
    rpmbuild -bi ${RPMWORK}/SPECS/foo.spec
    rpmbuild -bb ${RPMWORK}/SPECS/foo.spec

This should provide an RPM:

    ${RPMWORK}/RPMS/x86_64/xfce4-xfapplet-plugin-0.1.0-15.el6.x86_64.rpm

