# rpm-spec-k9s

This repo contains rpm spec file for building k9s tool.
Prebuilt rpm package for CentOS Stream 8 can be downloaded from the releases page.

## Manual package building

```
yum install rpmdevtools yum-utils
rpmdev-setuptree
wget https://raw.githubusercontent.com/dborisov/rpm-spec-k9s/master/k9s.spec -O ~/rpmbuild/SPECS/k9s.spec
yum-builddep ~/rpmbuild/SPECS/k9s.spec
spectool -g -R ~/rpmbuild/SPECS/k9s.spec
rpmbuild -ba ~/rpmbuild/SPECS/k9s.spec
```
