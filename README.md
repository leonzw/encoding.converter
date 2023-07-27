# 关于这个项目

## 历史
### 项目的由来
很早的时候，大约还是2007年以前，因为工作的原因，一直使用PHP进行开发，但是经常会遇到乱码的问题，从服务器到客户端，各种奇怪问题，非常头疼，那时候用PHP写了一个简单脚本方便自己使用。随着时间的推移，后来觉得PHP作为shell执行还是不太方便，毕竟不能总是安装解析器，于是2014年开始使用Python来重新构建了这个脚本。大大方便了自己的日常使用。偶尔转换电影字幕啥的也不在话下

## 安装使用
>目前还没有编纂到pip里面，考虑后期会迁移过去

这个脚本使用非常简单，可以按照下面步骤来实现安装

### 安装步骤

1. 下载源代码
```bash
git clone git@github.com:leonzw/encoding.converter.git
```

2. 虚拟一下virtualenv环境
```bash
  # 初始化venv
  virtualenv venv
  # 激活使用
  source venv/bin/activate
```

3. 安装类库
```bash
pip install -r requirements.txt
```

4. 大功告成，可以添加快捷方式到系统环境里面方便调用
```bash
ln -s index.py /usr/local/bin/encoding-convert 
```

### Usage使用方法
```bash
# 输入下面指令可以查询使用方法
$python index.py
usage: index.py [-h] [-t] -f SOURCE FILE [-tc TARGET_CODE] [-v]
index.py: error: the following arguments are required: -f/--file
```
##### Help 指令
```bash
# 输入 --help查看具体参数
$python index.py --help
INFO Start converting ... 
usage: index.py [-h] [-t] -f SOURCE FILE [-tc TARGET_CODE] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -t, --test-only       仅测试编码，不转换
  -f SOURCE FILE, --file SOURCE FILE
                        FILE path to be converted
  -tc TARGET_CODE, --target-encoding TARGET_CODE
                        目标文件编码
  -v, --verbose         调试模式

```

> 如果只是测试文件的源码格式，可以只用 -t参数，则不会转换文档，只测试文档编码类型

##### 调试信息
如果使用过程中想查看更多调试信息，可以通过 -v或者 --verbose
```bash
python index.py -f ./example/test.txt -v
```