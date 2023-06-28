# Augustus Installation

## Cmake

```reasonml
cd /path/to/AUGUSTUS && tar -zxf cmake-3.8.1.tar.gz
cd cmake-3.8.1
./configure --prefix=/path/to/AUGUSTUS/cmake
make
make install
```

## hislib 

```reasonml
cd /path/to/AUGUSTUS && tar -zxf htslib-1.11.tar.gz
mv htslib-1.11 htslib && cd htslib
autoheader
autoconf
sed -i 's/\-O2/\-O3 -march=armv8.2-a -mtune=tsv110/g' `grep -lr "\-O2" ./`
CC=`which gcc` ./configure --prefix=/path/to/AUGUSTUS/htslib
make -j 16
make install
```

## bfctools

```reasonml
cd /path/to/AUGUSTUS && tar -zxf bcftools-1.11.tar.gz
mv bcftools-1.11 bcftools && cd bcftools
autoheader
autoconf
sed -i 's/\-O2/\-O3 -march=armv8.2-a -mtune=tsv110/g' `grep -lr "\-O2" ./`
CC=`which gcc` ./configure --prefix=/path/to/AUGUSTUS/bcftools
make -j 16
make install
```

## samtools

```reasonml
cd /path/to/AUGUSTUS && tar -zxf samtools-1.11.tar.gz
mv samtools-1.11 samtools && cd samtools
autoheader
autoconf
sed -i 's/\-O2/\-O3 -march=armv8.2-a -mtune=tsv110/g' `grep -lr "\-O2" ./`
CC=`which gcc` ./configure --prefix=/path/to/AUGUSTUS/samtools
```

## Bamtools

```reasonml
cd /path/to/AUGUSTUS && tar -zxf bamtools-2.5.0.tar.gz
mv bamtools-2.5.0 bamtools && cd bamtools
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=../ ..
make -j 16
make install
```

## Augustus

```reasonml
cd /path/to/AUGUSTUS && tar -zxf Augustus-3.3.3.tar.gz && cd Augustus-3.3.3
export TOOLDIR=/path/to/AUGUSTUS
export LD_LIBRARY_PATH=/path/to/AUGUSTUS/bamtools/lib64:$LD_LIBRARY_PATH
export LIBRARY_PATH=/path/to/AUGUSTUS/bamtools/lib64:$LIBRARY_PATH

sed -i 's/\/usr\/include\/bamtools/\/path\/to\/AUGUSTUS\/bamtools\/include\/bamtools/g' `grep -rl "/usr/include/bamtools" ./`
sed -i 's/\/opt\/augustus/\/path\/to\/AUGUSTUS\/augustus_aarch64/g' Makefile

CC=`which gcc` CXX=`which g++` CXXFLAGS='-O3 -std=c++11 -march=armv8.2-a -mtune=tsv110' CFLAGS='-O3 -march=armv8.2-a -mtune=tsv110' make -j
make install
```