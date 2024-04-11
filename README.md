# MyPython
python学习记录

## macos 安装pyenv

1. 使用brew安装pyenv

   ```shell
   brew install pyenv
   ```

2. 在`~/.zshrc`文件加入配置

   ```shell
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)"
   ```
   
   之后在命令行输入`source ~/.zshrc`刷新配置

3. pyenv常用命令

   ```shell
   # 查看管理的所有版本
   pyenv versions
   # 查看可安装的版本
   pyenv install --list
   # 安装指定的 python 版本
   pyenv install 3.x
   # 设置 python 版本（全局有效）
   pyenv global 3.x
   # 设置 python 版本（当前目录有效）
   pyenv local 3.x
   # 卸载 python 版本
   pyenv uninstall 3.x
   ```

4. MySQL 的连接池使用情况可以通过以下两种方式查看：

   1. 查看 MySQL 的全局状态：执行 `show global status like '%thread%';` 命令，可以查看所有的线程相关的状态信息。其中，常见的线程状态如下：

   - Threads_connected: 表示当前连接池中已连接的线程数量。

   - Threads_running: 表示当前正在运行的线程数量。

   2. 查看当前会话状态：执行 `show processlist;` 命令，可以查看当前所有连接的会话状态信息。其中，常见的状态信息如下：

   - Sleep: 表示当前线程处于睡眠状态，等待请求。

   - Query: 表示当前线程正在执行查询语句。

   - Locked: 表示当前线程正在等待锁。

   - Connecting: 表示当前线程正在连接到 MySQL 服务器。

   - Sending data: 表示当前线程正在向客户端传输数据。

   - Writing to net: 表示当前线程正在将数据写入网络套接字。

   - Sorting result: 表示当前线程正在对结果进行排序。

通过这两种方式，我们可以查看连接池的连接情况、当前线程的状态，以及运行状态。可以根据这些信息来了解 MySQL 数据库当前的连接池状况。

## 使用python对图片进行高斯模糊

```python
# -*- coding: utf-8 -*-
# 'input.jpg' 是你要处理的图片的文件名。你需要替换为你实际的文件路径。
# cv2.GaussianBlur() 函数用于应用高斯模糊。它接收三个参数：原图像、核大小以及标准差。其中，核大小必须是奇数，用于确定高斯核的大小；标准差通常设为0，让函数自动计算标准差。
# (15, 15) 是高斯核的大小，你可以按需修改。较大的核会使图像更模糊。
# 'output.jpg' 是保存处理后图片的文件名。你需要根据需要替换。
# 注意：运行上述代码需要安装OpenCV库。如果还没有安装，可以通过pip命令进行安装：pip install opencv-python

import cv2

# 读取图像
img = cv2.imread('input.jpeg')

# 应用高斯模糊
blur_img = cv2.GaussianBlur(img, (499, 499), 0)

# 保存处理后的图像
cv2.imwrite('output.jpg', blur_img)
```

## python协程

程的特点在于是一个线程执行，那和多线程比，协程有何优势？

最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

Python对协程的支持是通过generator实现的。

在generator中，我们不但可以通过`for`循环来迭代，还可以不断调用`next()`函数获取由`yield`语句返回的下一个值。

但是Python的`yield`不但可以返回一个值，它还可以接收调用者发出的参数。

