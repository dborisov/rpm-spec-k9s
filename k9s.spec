%define debug_package %{nil}

Name:           k9s
Version:        0.25.18
Release:        1%{?dist}
Summary:        Kubernetes CLI To Manage Your Clusters In Style!
License:        Apache-2.0
URL:            https://k9scli.io/
Source0:        https://github.com/derailed/k9s/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  make, git, go >= 1.14

%description
K9s provides a terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources.

%prep
%autosetup -n %{name}-%{version}

%build
make build

%install
install -D -m 0755 %{_builddir}/%{name}-%{version}/execs/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Jan 07 2022 Denis Borisov <dborisov86@gmail.com> 0.25.18-1
- Initial
