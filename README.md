# rpm-spec-k9s

```
yum install rpmdevtools yum-utils
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
wget https://raw.githubusercontent.com/dborisov/rpm-spec-k9s/master/k9s.spec -O ~/rpmbuild/SPECS/k9s.spec
yum-builddep ~/rpmbuild/SPECS/k9s.spec
spectool -g -R ~/rpmbuild/SPECS/k9s.spec
rpmbuild -ba ~/rpmbuild/SPECS/k9s.spec
```