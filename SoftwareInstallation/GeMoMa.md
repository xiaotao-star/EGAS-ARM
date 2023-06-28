# Gemoma Installation

## java

```
wget https://download.oracle.com/otn/java/jdk/8u371-b11/ce59cff5c23f4e2eaf4e778a117d4c5b/jdk-8u371-linux-aarch64.tar.gz?AuthParam=1687918549_dc0ed6c7964bd03589656123b8b4ce1f

tar -zxvf jdk-8u371-linux-aarch64.tar.gz

vim ~/.bashrc

文件末尾加入以下三行
#jdk路径
export JAVA_HOME=/path/to/jdk路径  ##以自己实际情况为主
#指定jdk可执行文件
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
```

## Gemoma

```
http://www.jstacs.de/downloads/GeMoMa-1.9.zip
unzip GeMoMa-1.9.zip
```

