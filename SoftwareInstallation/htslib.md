

## htslib Installation

```
cd /path/to/HTSLIB && tar -zxf htslib-1.11.tar.gz
mv htslib-1.11 htslib && cd htslib

autoheader
autoconf
sed -i 's/\-O2/\-O3 -march=armv8.2-a -mtune=tsv110/g' `grep -lr "\-O2" ./`
CC=`which clang` ./configure --prefix=/path/to/HTSLIB

make -j 16
make install
```

