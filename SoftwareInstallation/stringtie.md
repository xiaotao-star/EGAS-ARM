# stringtie Installation

```
tar -xvf stringtie-2.2.1.tar.gz
cd stringtie-2.2.1

make release
```

(注意!!!：在编译过程中会出现错误，在htslib/build_lib.sh中的链接会出现失效，例如：bzip2-1.0.8.tar.gz，xz-5.2.5.tar.gz)



需要我们手动下载版本后再进行编译,阅读htslib/build_lib.sh代码进行适当修改，下面以bzip2-1.0.8为例进行更改：

```
cd htslib
tar -xvf  bzip2-1.0.8.tar.gz
mv bzip2-1.0.8 bzip2
```

所有错误修改完毕后再返回到stringtie-2.2.1，再继续进行make release 编译。 
