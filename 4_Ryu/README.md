# Ryu
Ryu 是一个基于 Python 的开源 SDN (软件定义网络) 控制器框架, 用于管理和控制 OpenFlow 交换机. 详细的文档可以看 [Ryu 官方文档](https://ryu.readthedocs.io/en/latest/) 以及 Ryu book (自己找下资源只有).

# 安装
## 软件包
在 Archlinux 上, 可以通过 AUR 安装:
```sh
yay -S python-ryu
```

如果遇到下面报错:

![yay error](./img/yay-install-ryu-error.png)

解决办法为:
```sh
pip uninstall setuptools
pip install setuptools==67.6.1
yay -S python-ryu
```

由于各种依赖问题, 不太建议这种安装方式.

## pip (推荐)
最好用 `python3.8` 构建虚拟环境运行.

Archlinux 上管理多版本 python:
```sh
sudo pacman -S pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
source ~/.bashrc

pyenv install 3.8
pyenv global 3.8.xx
```
(xx 为你安装的具体版本, 我这里是 `20`)

构建 `venv` 虚拟环境:
```sh
python3.8 -m venv ryu
source ryu/bin/activate
pip install ryu
pip uninstall eventlet
pip install eventlet==0.30.0
ryu-manager --version
```

测试:
```sh
git clone https://github.com/faucetsdn/ryu.git Ryu
ryu-manager Ryu/ryu/app/simple_switch_13.py
```

![ryu-manager run](./img/ryu-manager-ok.png)


# 结构
![ryu architecture](./img/Ryu-SDN-controller-architecture.png)

- WSGI 定义 REST API 作为北向接口
- `Application` 以 OpenFlow 作为南向接口与基础设备通信

Ryu Controller 的主要编写逻辑为:
- 定义继承自 `app_manager.RyuApp` 的类, 这是入口, 整个文件就是在完善这个类
- 利用 `set_ev_cls` 修饰器添加事件处理函数 (这个修饰器主要的作用就是为从函数传入的事件设置类别)

# ryu 库基本结构
```sh
git clone https://github.com/faucetsdn/ryu.git Ryu
cd Ryu/ryu
```

该目录下的文件, 就是编写 Ryu 控制器的所有接口库:
```sh
tree -L 1
.
├── app
├── base
├── cfg.py
├── cmd
├── contrib
├── controller
├── exception.py
├── flags.py
├── hooks.py
├── __init__.py
├── lib
├── log.py
├── ofproto
├── __pycache__
├── services
├── tests
├── topology
└── utils.py
```
`app` 目录下有许多官方的 `application` 示例, 后续也会作为例子介绍.

一些重要的接口, 比如:
- `ryu.base.app_manager` 库中的 `RyuApp` 类
- `ryu.controller.handler` 中的 `set_ev_cls` 修饰器
- `ryu.controller.ofp_event` 库, 包含一些事件类

# Hello World
假设工作目录为 `~/myRyu`:
```sh
cd ~/myRyu
mkdir hello_ryu.py
```

内容:
```python
from ryu.base import app_manager
import logging
logging.basicConfig(level=logging.DEBUG)

class L2Switch(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)
        logging.debug("Hello Ryu!")
```

运行:
```sh
ryu-manager --verbose hello_ryu.py
loading app hello_ryu.py
instantiating app hello_ryu.py of L2Switch
Hello Ryu!
BRICK L2Switch
```

- 这里 `ryu-manager` 以继承自 `app_manager.RyuApp` 的类为入口
- `super(L2Switch, self).__init__(*args, **kwargs)` 将参数传递给父类的 `__init__` 函数来初始化, `*args` 捕获所有位置参数, `**kwargs` 捕获所有命名参数
- `super` 函数的语法如下:
```python
super(ChildClass, self).method(args)
```
- `ChildClass` 表明从哪个类开始查找父类
- `self` 指明用哪个实例来调用父类的方法

