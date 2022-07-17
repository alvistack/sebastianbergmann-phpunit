%global debug_package %{nil}

Name: phpunit
Epoch: 100
Version: 9.5.21
Release: 1%{?dist}
BuildArch: noarch
Summary: The PHP Unit Testing framework
License: BSD-2-Clause
URL: https://github.com/sebastianbergmann/phpunit/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
Requires: php-cli >= 7.3

%description
PHPUnit is a programmer-oriented testing framework for PHP. It is an
instance of the xUnit architecture for unit testing frameworks.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -d %{buildroot}%{_datadir}/php/vendor
cp -rfT vendor %{buildroot}%{_datadir}/php/vendor
pushd %{buildroot}%{_bindir} && \
    ln -fs %{_datadir}/php/vendor/phpunit/phpunit phpunit && \
    popd
chmod a+x %{buildroot}%{_datadir}/php/vendor/phpunit/phpunit
fdupes -qnrps %{buildroot}%{_datadir}/php/vendor

%check

%files
%license LICENSE
%dir %{_datadir}/php
%dir %{_datadir}/php/vendor
%{_bindir}/*
%{_datadir}/php/vendor/*

%changelog
