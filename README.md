# 关于这个项目

## 历史
### 项目的由来
很早的时候，大约还是2007年以前，因为工作的原因，一直使用PHP进行开发，但是经常会遇到乱码的问题，从服务器到客户端，各种奇怪问题，非常头疼，那时候用PHP写了一个简单脚本方便自己使用。随着时间的推移，后来觉得PHP作为shell执行还是不太方便，毕竟不能总是安装解析器，于是2014年开始使用Python来重新构建了这个脚本。大大方便了自己的日常使用。偶尔转换电影字幕啥的也不在话下

## 使用方法
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

