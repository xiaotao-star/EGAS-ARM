

## samtools Installation

```
cd /path/to/SAMTOOLS && tar -zxf samtools-1.11.tar.gz
cd samtools-1.11

autoheader
autoconf
sed -i 's/\-O2/\-O3 -march=armv8.2-a -mtune=tsv110/g' `grep -lr "\-O2" ./`
CC=`which clang` ./configure --prefix=/path/to/SAMTOOLS --with-htslib=/path/to/HTSLIB

make -j 16
make install
```

