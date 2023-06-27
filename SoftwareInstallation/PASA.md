

## PASA Installtion

## samtools

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

## gmap  

```
wget http://research-pub.gene.com/gmap/src/gmap-gsnap-2021-07-23.tar.gz
tar -xvf gmap-gsnap-2021-07-23.tar.gz
cd gmap-gsnap-2021-07-23/
sed -i 's/__asm__ ("cpuid"/\/\/__asm__ ("cpuid"/g' src/cpuid.c
sed -i 's/__asm__ ("xgetbv"/\/\/__asm__ ("xgetbv"/g' src/cpuid.c
./configure --prefix=/path/to/test/install/gmap
make -j8 && make install
```

## minimap2  

```
https://github.com/lh3/minimap2/archive/refs/tags/v2.22.tar.gz
tar -xvf minimap2-2.22.tar.gz
cd minimap2-2.22/
sed -i '1 i CC= gcc' Makefile
make arm_neon=1 aarch64=1
mkdir -p /path/to/test/install/minimap2
cp minimap2 /path/to/test/install/minimap2
```

## blat  

```
wget https://codeload.github.com/djhshih/blat/tar.gz/v35.1
tar -xvf blat-35.1.tar.gz
cd blat-35.1
export MACHTYPE=aarch64
make -j8
mkdir -p /path/to/test/install/blat
cp -r bin /path/to/test/install/blat
```

##  pblat  

```
wget https://github.com/icebert/pblat/archive/refs/tags/2.5.tar.gz
tar -xvf pblat-2.5.tar.gz
cd pblat-2.5/
sed -i 's/x86_64/aarch64/g' Makefile
sed -i 's/CFLAGS=-O -Wall/CFLAGS=-O -Wall -L.\/usr\/lib64 /g' Makefile
sed -i 's/HG_INC=-I.\/inc -I.\/htslib/HG_INC=-I.\/inc -I.\/htslib -
I.\/usr\/include/g' Makefile
sed -i 's/\&\& args != NULL//g' lib/htmshell.c
yumdownloader openssl-devel
yumdownloader krb5-devel
yumdownloader libcom_err-devel
yumdownloader openssl-libs
rpm2cpio openssl-devel-1.0.2k-25.el7_9.aarch64.rpm | cpio -ivdm
rpm2cpio krb5-devel-1.15.1-54.el7_9.aarch64.rpm | cpio -ivdm
rpm2cpio libcom_err-devel-1.42.9-19.el7.aarch64.rpm | cpio -ivdm
rpm2cpio openssl-libs-1.0.2k-25.el7_9.aarch64.rpm | cpio -ivdm
make -j8
mkdir -p /path/to/test/install/pblat
cp pblat /path/to/test/install/pblat
```

## URI

```
wget https://cpan.metacpan.org/authors/id/G/GA/GAAS/URI-1.35.tar.gz
tar -xvf URI-1.35.tar.gz
cd URI-1.35/
perl Makefile.PL PREFIX=/path/to/test/perl5
LIB=/path/to/test/usr/lib64/perl5
make && make install
cd ..
yumdownloader perl-DBD-SQLite
yumdownloader perl-DBI
rpm2cpio perl-DBD-SQLite-1.39-3.el7.aarch64.rpm | cpio -ivdm
rpm2cpio perl-DBI-1.627-4.el7.aarch64.rpm | cpio -ivdm
export
PERL5LIB=/path/to/test/usr/lib64/perl5/:/path/to/test/usr/lib64/perl5/URI/:/path/to/test/usr/lib64/perl5/vendor_perl/:/path/to/test/usr/lib64/perl5/vendor_perl/auto/:/path/to/test/usr/lib64/perl5/vendor_perl/DBD/:/path/to/test/usr/lib64/perl5/vendor_perl/DBI/:/path/to/test/usr/lib64/perl5/vendor_perl/Bundle
```

## pasa

```
wget https://github.com/PASApipeline/PASApipeline/archive/refs/tags/pasa-v2.5.2.tar.gz
tar -xvf pasa-v2.5.2.tar.gz
cd PASApipeline-pasa-v2.5.2/
make -j8
cd sample_data/
cp mysql.confs/alignAssembly.config ./
sed -i
's/DATABASE=sample_mydb_pasa/DATABASE=\/path\/to\/test\/database.sqlite/g'
alignAssembly.config
export PATH=/path/to/test/install/pblat:/path/to/test/install/blat/bin:/path/to/test/install/minimap2:/path/to/test/install/:/path/to/test/install/samtools/bin:/path/to/test/install/gmap/bin:/path/to/test/PASApip
eline-pasa-v2.5.2/:/path/to/test/PASApipeline-pasa-v2.5.2/bin:$PATH
```

