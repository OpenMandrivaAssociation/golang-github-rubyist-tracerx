%global debug_package   %{nil}

%global provider        github
%global provider_tld    com
%global project         rubyist
%global repo            tracerx
# https://github.com/rubyist/tracerx
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          d7bcc0bc315bed2a841841bee5dbecc8d7d7582f
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        6.git%{shortcommit}%{?dist}
Summary:        Output tracing information in your Go app based on environment variables
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

%description
Tracerx is a simple tracing package that logs messages depending on environment
variables. It is very much inspired by git's GIT_TRACE mechanism.

%package devel
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{import_path}) = %{version}-%{release}

%description devel
Tracerx is a simple tracing package that logs messages depending on environment
variables. It is very much inspired by git's GIT_TRACE mechanism.

This package contains library source intended for building other packages which
use import path with %{import_path} prefix.

%prep
%autosetup -n %{repo}-%{commit}

%build

%install
install -Dpm0644 %{repo}.go %{buildroot}%{gopath}/src/%{import_path}/%{repo}.go

%files devel
%license LICENSE
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/%{repo}.go

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-1.gitd7bcc0b
- Initial package
