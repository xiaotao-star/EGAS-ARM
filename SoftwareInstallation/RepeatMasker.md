

## RepeatMasker Installation

## rmblast

```
wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.13.0/ncbi-blast-2.13.0+-src.tar.gz 
tar -xzvf ncbi-blast-2.13.0+-src.tar.gz

wget http://www.repeatmasker.org/isb-2.10.0+-rmblast.patch.gz
gunzip isb-2.10.0+-rmblast.patch.gz

cd ncbi-blast-2.13.0+-src
patch -p1 < ../isb-2.10.0+-rmblast.patch 
cd c++

 ./configure --with-mt --without-debug --without-krb5 \
--without-openssl --with-projects=scripts/projects/rmblastn/project.lst \
--prefix=/path/to/rmblast
make -j$(nproc)
make -j$(nproc) install
export PATH=/path/to/rmblast/bin:$PATH
```

## TRF

```
wget https://hub.fastgit.xyz/Benson-Genomics-Lab/TRF/archive/refs/tags/v4.09.1.tar.gz
tar -xzvf v4.09.1.tar.gz

cd TRF-4.09.1

mkdir build && cd build
 ../configure \
--prefix=/path/to/TRF
make -j$(nproc) && make install

export PATH=/path/to/TRF/bin:$PATH
```

## RepeatMasker

```
wget http://www.repeatmasker.org/RepeatMasker/RepeatMasker-4.1.2-p1.tar.gz
tar -xvf RepeatMasker-4.1.2-p1.tar.gz

cd ./RepeatMasker
perl ./configure -libdir /path/to/RepeatMasker/Libraries/ \
 -rmblast_dir /path/to/rmblast/bin \
 -trf_prgm /path/to/TRF/bin/trf \ 
 -default_search_engine rmblast
 
注：
-libdir：重复序列数据库路径，此处使用默认重复序列库
-rmblast_dir：RMBLAST的安装路径
-trf_prgm：TRF可执行程序的路径
-default_search_engine：默认搜索引擎

export PATH=/path/to/RepeatMasker:$PATH
export PATH=/path/to/RepeatMasker/utils:$PATH
```

