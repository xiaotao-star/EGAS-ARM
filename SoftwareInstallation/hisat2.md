# hisat2 installatiion

```
unzip hisat2-master.zip
cd hisat2-master

export NO_TBB=1
export POPCNT_CAPABILITY=0
```

vi Makefile

按“i”进入编辑模式，修改文件的“BITS=64 aarch64”分支，在第140和141行之间插入以下粗体部分内容。
目前“BITS=64”只支持x86，不支持aarch64，需要新增一个aarch64的分支

修改前：

```reasonml
BITS=32
ifeq (x86_64,$(shell uname -m))
BITS=64
endif
```

修改后：

```reasonml
BITS=32
ifeq (x86_64,$(shell uname -m))
BITS=64
endif
ifeq (aarch64,$(shell uname -m))
BITS=64
endif
```

vi Makefile

按“i”进入编辑模式，修改文件的-m64以及-msse2的aarch64分支，在第159和160行之间插入以下粗体部分内容。“Makefile”编译选项-m64/-msse2只支持x86，不支持aarch64，需要增加aarch64分支。

修改前：

```reasonml
ifeq (32,$(BITS))
        BITS_FLAG = -m32
endif
 
ifeq (64,$(BITS))
        BITS_FLAG = -m64
endif
SSE_FLAG=-msse2
```

修改后：

```reasonml
ifeq (32,$(BITS))
        BITS_FLAG = -m32
endif
 
ifeq (64,$(BITS))
        BITS_FLAG = -m64
endif
SSE_FLAG=-msse2
 
ifeq (aarch64,$(shell uname -m))
        BITS_FLAG =
        SSE_FLAG =
endif
```

vi Makefile

按“i”进入编辑模式，修改文件的FLAGS参数。

修改前：

```reasonml
EXTRA_FLAGS += -DPOPCNT_CAPABILITY
DEBUG_FLAGS    = -O0 -g3 $(BIToS_FLAG) $(SSE_FLAG) 
DEBUG_DEFS     = -DCOMPILER_OPTIONS="\"$(DEBUG_FLAGS) $(EXTRA_FLAGS)\""
RELEASE_FLAGS  = -O3 $(BITS_FLAG) $(SSE_FLAG) -funroll-loops -g3 
RELEASE_DEFS   = -DCOMPILER_OPTIONS="\"$(RELEASE_FLAGS) $(EXTRA_FLAGS)\""
NOASSERT_FLAGS = -DNDEBUG
FILE_FLAGS     = -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE
```

修改后：

```reasonml
EXTRA_FLAGS += 
DEBUG_FLAGS    = -O0 -g3 $(BIToS_FLAG) $(SSE_FLAG) -funroll-loops -std=c++98
DEBUG_DEFS     = -DCOMPILER_OPTIONS="\"$(DEBUG_FLAGS) $(EXTRA_FLAGS)\""
RELEASE_FLAGS  = -O3 $(BITS_FLAG) $(SSE_FLAG) -funroll-loops -g3 -std=c++98 -Xlinker --allow-multiple-definition
RELEASE_DEFS   = -DCOMPILER_OPTIONS="\"$(RELEASE_FLAGS) $(EXTRA_FLAGS)\""
NOASSERT_FLAGS = -DNDEBUG
FILE_FLAGS     = -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE
```

执行以下命令修改“aligner_sw.h”和“sse_util.h”头文件。

将“sse2neon.h”文件上传到“third_party”目录下。

vim  “aligner_sw.h” 头文件。

```reasonml
vi aligner_sw.h
```

按“i”进入编辑模式，将

“#include <emmintrin.h>”替换为 “#include <sse2neon.h>”

修改前：

```reasonml
#include <emmintrin.h>
```

修改后：

```reasonml
#include <sse2neon.h>
```

按“Esc”键，输入**:wq!**，按“Enter”保存并退出编辑。

修改“sse_util.h”文件执行类似操作即可。



执行以下命令进行编译安装。

```reasonml
make
```





