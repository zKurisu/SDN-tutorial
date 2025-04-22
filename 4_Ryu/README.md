# Ryu
Ryu 是一个基于 Python 的开源 SDN (软件定义网络) 控制器框架, 用于管理和控制 OpenFlow 交换机.

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

Ryu Controller 的编写逻辑为:
- 定义继承自 `app_manager.RyuApp` 的类, 这是入口, 整个文件就是在完善这个类
- 利用 `set_ev_cls` 修饰器添加事件处理函数 (这个修饰器主要的作用就是为从函数传入的事件设置类别)

