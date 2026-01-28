# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 Python 学习和实践项目，包含多个学习模块：设计模式、数据结构与算法、MySQL 数据库操作、异步编程、并发编程等。项目主要用于学习和实验 Python 的各种特性和最佳实践。

## 环境配置

### Python 版本管理

项目使用 pyenv 管理 Python 版本：

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

### MySQL 配置

项目中的 MySQL 相关代码需要本地 MySQL 服务：

```shell
# 启动 MySQL
mysql.server start

# 后台启动 MySQL
brew services start mysql

# 连接 MySQL
mysql -u root -p
```

默认连接配置：`mysql+pymysql://root:123456@localhost:3306/test`

## 项目结构

### 核心模块

- **设计模式/** - 23 种设计模式的 Python 实现
  - 包括单例模式、工厂模式、观察者模式、策略模式等
  - 每个文件是一个独立的设计模式示例

- **数据结构与算法/** - 算法和数据结构练习
  - 面试题目实现
  - 算法学习笔记

- **mysql_study/** - MySQL 学习模块
  - `__init__.py` - SQLAlchemy ORM 示例，包含数据库连接池和模型定义
  - SQL 练习文件：创建表、增删查改、子查询、视图、约束等
  - `MySQL笔记.md` - MySQL 索引、事务、锁等核心概念笔记

- **inbox_message/** - 数据库消息系统示例
  - `mysql_config.py` - 数据库配置和连接管理
  - `user_message.py` - 用户消息模型和操作示例
  - 使用 SQLAlchemy ORM 和上下文管理器模式

- **python学习手册/** - Python 语言特性学习
  - 协程和异步编程示例（asyncio_test.py, flag_asyncio.py, spinner_asyncio.py）
  - 并发编程示例（flags_threadpool.py, spinner_thread.py）
  - 各种 Python 特性练习

### 工具文件

- **util.py** - 通用工具函数
  - `timeit` 装饰器：用于性能测试
  - `fib` 函数：斐波那契数列计算，用于测试多线程/多进程性能

- **builder.py** - 建造者模式实现示例

- **main.py** - 图像处理示例
  - 使用 OpenCV 进行高斯模糊处理
  - 异步 I/O 和线程池的性能对比
  - 展示了 asyncio 与 ThreadPoolExecutor 的结合使用

## 关键技术点

### 数据库操作模式

项目使用 SQLAlchemy ORM，推荐的数据库操作模式：

```python
from contextlib import contextmanager

@contextmanager
def get_db_session():
    session = DBsession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

# 使用方式
with get_db_session() as db_session:
    # 数据库操作
    db_session.query(Model).filter(...).first()
```

### 并发编程

项目包含多种并发模式的对比：

1. **多线程** - 适用于 I/O 密集型任务，但受 GIL 限制
2. **多进程** - 适用于 CPU 密集型任务，可充分利用多核
3. **协程** - 高效的异步 I/O，单线程执行，无锁机制

### 图像处理

使用 OpenCV (cv2) 进行图像处理：
- 高斯模糊：`cv2.GaussianBlur(img, kernel_size, sigma)`
- 核大小必须是奇数
- 较大的核会使图像更模糊

## 开发工作流

### Git 提交

项目包含自动提交脚本 `commit.sh`：

```shell
./commit.sh
```

该脚本会自动执行：add、commit（使用当前日期作为消息）、pull --rebase、push

### 离线包安装

在无网络环境下安装 Python 包：

```shell
# 在联网机器上下载依赖
mkdir package-deps
cd package-deps
pip download package-name

# 在离线机器上安装
cd package-deps
pip install --no-index --find-links=. *
```

## 代码风格

- 使用 UTF-8 编码：`# -*- coding: utf-8 -*-`
- 类使用大驼峰命名
- 函数和变量使用小写下划线命名
- 数据库模型类继承自 SQLAlchemy 的 Base 类
- 使用上下文管理器处理资源（数据库连接、文件等）
