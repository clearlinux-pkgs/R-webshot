#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-webshot
Version  : 0.5.4
Release  : 49
URL      : https://cran.r-project.org/src/contrib/webshot_0.5.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/webshot_0.5.4.tar.gz
Summary  : Take Screenshots of Web Pages
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: R-webshot-license = %{version}-%{release}
Requires: R-callr
Requires: R-jsonlite
Requires: R-magrittr
BuildRequires : R-callr
BuildRequires : R-jsonlite
BuildRequires : R-magrittr
BuildRequires : buildreq-R

%description
Markdown documents.

%package license
Summary: license components for the R-webshot package.
Group: Default

%description license
license components for the R-webshot package.


%prep
%setup -q -n webshot
cd %{_builddir}/webshot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664233178

%install
export SOURCE_DATE_EPOCH=1664233178
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-webshot
cp %{_builddir}/webshot/inst/NOTICE %{buildroot}/usr/share/package-licenses/R-webshot/23b9103c4b7912d9e985e9786f192aca64d7ff52 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/webshot/DESCRIPTION
/usr/lib64/R/library/webshot/INDEX
/usr/lib64/R/library/webshot/Meta/Rd.rds
/usr/lib64/R/library/webshot/Meta/features.rds
/usr/lib64/R/library/webshot/Meta/hsearch.rds
/usr/lib64/R/library/webshot/Meta/links.rds
/usr/lib64/R/library/webshot/Meta/nsInfo.rds
/usr/lib64/R/library/webshot/Meta/package.rds
/usr/lib64/R/library/webshot/NAMESPACE
/usr/lib64/R/library/webshot/NEWS.md
/usr/lib64/R/library/webshot/NOTICE
/usr/lib64/R/library/webshot/R/webshot
/usr/lib64/R/library/webshot/R/webshot.rdb
/usr/lib64/R/library/webshot/R/webshot.rdx
/usr/lib64/R/library/webshot/casperjs/bin/bootstrap.js
/usr/lib64/R/library/webshot/casperjs/modules/casper.js
/usr/lib64/R/library/webshot/casperjs/modules/cli.js
/usr/lib64/R/library/webshot/casperjs/modules/clientutils.js
/usr/lib64/R/library/webshot/casperjs/modules/colorizer.js
/usr/lib64/R/library/webshot/casperjs/modules/events.js
/usr/lib64/R/library/webshot/casperjs/modules/http.js
/usr/lib64/R/library/webshot/casperjs/modules/mouse.js
/usr/lib64/R/library/webshot/casperjs/modules/pagestack.js
/usr/lib64/R/library/webshot/casperjs/modules/querystring.js
/usr/lib64/R/library/webshot/casperjs/modules/tester.js
/usr/lib64/R/library/webshot/casperjs/modules/utils.js
/usr/lib64/R/library/webshot/casperjs/modules/xunit.js
/usr/lib64/R/library/webshot/casperjs/package.json
/usr/lib64/R/library/webshot/examples/shiny.Rmd
/usr/lib64/R/library/webshot/help/AnIndex
/usr/lib64/R/library/webshot/help/aliases.rds
/usr/lib64/R/library/webshot/help/figures/r-small-resized.png
/usr/lib64/R/library/webshot/help/figures/r-small-zoomed.png
/usr/lib64/R/library/webshot/help/paths.rds
/usr/lib64/R/library/webshot/help/webshot.rdb
/usr/lib64/R/library/webshot/help/webshot.rdx
/usr/lib64/R/library/webshot/html/00Index.html
/usr/lib64/R/library/webshot/html/R.css
/usr/lib64/R/library/webshot/tests/testthat.R
/usr/lib64/R/library/webshot/tests/testthat/test-url.R
/usr/lib64/R/library/webshot/utils.js
/usr/lib64/R/library/webshot/webshot.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-webshot/23b9103c4b7912d9e985e9786f192aca64d7ff52
