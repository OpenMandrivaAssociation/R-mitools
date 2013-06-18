%global packname  mitools
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          2.2
Release:          2
Summary:          Tools for multiple imputation of missing data
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/mitools_2.2.tar.gz
Requires:         R-RODBC R-DBI 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-RODBC R-DBI 

%description
Tools to perform analyses and combine results from multiple-imputation

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/dta
%{rlibdir}/%{packname}/help


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 776374
- Import R-mitools
- Import R-mitools


