%define base_name	dbd-mysql
%define name	ruby-%{base_name}
%define version	0.4.4
%define release	%mkrel 1

# Be backportable
%{!?ruby_vendorlibdir:%define ruby_vendorlibdir %ruby_sitelibdir}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	MySQL driver for ruby-DBI
Group:		Development/Ruby
License:	BSD-like
URL:		http://ruby-dbi.rubyforge.org/
Source:		http://rubyforge.org/frs/download.php/69558/%{base_name}-%{version}.tar.gz
BuildRequires:	ruby
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This is a MySQL driver for ruby-DBI.

%prep
%setup -q -n %{base_name}-%{version}

%build
ruby setup.rb config \
	--bin-dir=%{buildroot}%{_bindir} \
	--rb-dir=%{buildroot}%{ruby_vendorlibdir}
ruby setup.rb setup

%install
rm -rf %{buildroot}
ruby setup.rb install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog LICENSE
%{ruby_vendorlibdir}/dbd

