# 博乐工作日志

## 2020-11

### 2020-11-16

入职培训，熟悉工作环境，安装开发软件vscode，熟悉Crash Frency，完成新手教程

### 2020-11-17

学习Python2.7，安装MySQL、MySQL workbench，RDM，熟悉macOS系统

### 2020-11-18

python面向对象部分，异常处理

MySQL连接不上

#### Socket学习

Socket是在应用层和传输层之间的一个抽象层，他把TCP/IP层复杂的操作抽象为几个简单的接口，供应用层调用实现进程在网络中的通信。

Socket保证了不同计算机之间的通信，也就是网络通信。对于网站，通信模型是服务器与客户端之间的通信。两端都建立了一个Socket对象，然后通过Socket对象进行传输。通常服务器处于一个无限循环，等待客户端的连接。

### 2020-11-19

当前任务
/sharetoall/10/Phoenix Studio/Casino System/System Module/01_更新计划/2020.11.24

python学习
元组元素不可修改，但是内存占用和效率要优于list

jupyter打开报错
使用`LANG=zn jupyter notebook`

阿里云桌面添加ssh并git代码，[参考网址](https://blog.csdn.net/Suo_ivy/article/details/79940839)

```
ssh-agent bash
ssh-add ~/.ssh/jiangchenrui
ssh -T git@10.10.10.228
```

[SQL索引](https://www.cnblogs.com/hyd1213126/p/5828937.html)

### 2020-11-20

阅读login.py代码
hasattr(object, name)用于判断objec是否有name属性
[python协程](https://mydevops.github.io/2017/03/18/Python-2-Python-%E5%8D%8F%E7%A8%8B/)

@classmethod
在类例定义可以不实例化类就可以直接调用
```
class A(object):
    num = "类属性"
    
    def func1(self):
        print 'func1'
        print self
        
    @classmethod
    def func2(cls):
        print 'func2'
        print cls
        print cls.num
        cls().func1()

        
A.func2()
```

### 2020-11-23

之前的ssh添加私钥只能暂时生效，不能永久生效，需要在.ssh文件夹下添加config文件，添加如下内容
```
Host *
    HostName github
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/rsa
    User jiangchenrui
```
阅读d级活动代码

设计模式六大原则

* 开闭原则
* 里氏代换原则
* 依赖倒转原则
* 接口隔离原则
* 迪米特法则（最少知道原则）
* 合成复用原则

### 2020-11-24

明确rocket修改目标

重构inbox，发送礼物有过期失效问题

### 2020-11-25

[python代码优化](https://xzhren.github.io/posts/2016/2016-08-22-[%E4%BB%96%E5%B1%B1%E4%B9%8B%E7%9F%B3]-1-Python-%E4%BB%A3%E7%A0%81%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96%E6%8A%80%E5%B7%A7.html)

[python输入](https://www.jianshu.com/p/ba55536e0a39)

```python
# python循环输入多行多列
import sys
def __name__ == '__main__':
    inputList = []
    while True:
        item = sys.stdin.readline().strip()
        if item == '':
            break
        item = list(item.split())
        inputList.append(item)
    print(inputList)
```

### 2020-11-26

优化indox的log，配置B级活动rocket

### 2020-11-27

完成rocket阶段奖励配置

### 2020-11-30

