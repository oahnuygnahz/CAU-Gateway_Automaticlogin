# 中国农大网关自动登录

作者：张云浩    QQ : 3358023393(新)



## **如何使用**

- 点击上方Download ZIP按钮，即可将整个项目下载至电脑。
- 解压ZIP文件，打开其中/User目录，点击'login.exe'或‘logout.exe’进行第一次设置(即输入一次账号和密码，这个操作会自动生成配置文件gateway.setup)
- 以后使用只需点击'login.exe'或'logout.exe'即可自动''登录''或''注销''网关。

**注**：

- 建议使用 管理员模式 + win7兼容模式 打开（为了最大的兼容性,打包环境为win7-32bit）。
- **第一次使用请在有实体网线连接下进行设置(只需输入账号密码一次)。**
- **请妥善保管好您的配置文件。**
- 你可以任意移动包含'login.exe''logout.exe''gateway.setup'这三个文件的文件夹，并不影响使用。

## **开发信息**

语言：Python 2.7.11

打包环境： windows7 Home Basic 32-bit

- gateway_tools.py说明：
  - 在文件最后选择'login'或'logout'来改变使用目的。
  - 需要打包的login.py或logout.py基于gateway_tools.py，仅仅改变最后的方式变量。