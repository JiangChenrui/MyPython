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

