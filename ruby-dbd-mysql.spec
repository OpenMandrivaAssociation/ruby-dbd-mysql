%define base_name	dbd-mysql
%define name	ruby-%{base_name}
%define version	0.4.4
%define release	3

# Be backportable
%{!?ruby_vendorlibdir:%define ruby_vendorlibdir %ruby_sitelibdir}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	MySQL driver for ruby-DBI
Group:		Development/Ruby
License:	BSD-like
URL:		https://ruby-dbi.rubyforge.org/
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



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.4-2mdv2011.0
+ Revision: 614724
- the mass rebuild of 2010.1 packages

* Sun Apr 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.4-1mdv2010.1
+ Revision: 531333
- new version

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.3-1mdv2010.0
+ Revision: 397042
- import ruby-dbd-mysql


* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.3-1mdv2010.0
- first mdv release 
