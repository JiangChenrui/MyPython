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
   
   if which pyenv > /dev/null;
     then eval "$(pyenv init -)";
   fi
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

   

