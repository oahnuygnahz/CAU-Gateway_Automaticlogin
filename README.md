# 中国农大网关自动登录

作者：张云浩    QQ : 3358023393(新)		

关键词 ：China Agricultural University gateway_automaticlogin，中国农业大学

## **特性**

- 适用于学校绝大部分环境（网线和WIFI）
- 只需双击即可完成‘登录’或‘注销操作’
- 没有物理连接时，无需关闭程序，插上物理连接或连接WIFI即可自动识别并登录
- 无与伦比的速度

## **如何使用**

- 点击上方Download ZIP按钮，即可将整个项目下载至电脑。
- 解压ZIP文件，打开其中/User目录，点击'login.exe'或‘logout.exe’进行第一次设置(即输入一次账号和密码，这个操作会自动生成配置文件gateway.setup)
- 以后使用只需点击'login.exe'或'logout.exe'即可自动''登录''或''注销''网关。

**注**：

- 建议使用 管理员模式 + win7兼容模式 打开（为了最大的兼容性,打包环境为win7-32bit）。
- **请妥善保管好您的配置文件。**
- 您可以任意移动包含'login.exe''logout.exe''gateway.setup'这三个文件的文件夹，并不影响使用。

## **当前版本**

- 版本ver1.5.1:


​	1.修复了一个潜在的可能导致断开网线后不断尝试连接，出现连接错误的BUG。

## **历史版本**

- 版本Ver1.5.0:

  1.增加了自动重连功能，当网线或WIFI网络没有连接上时，会自动重新尝试连接，直到成功为止。

- 版本Ver1.4.0:

  1.现在可以在WIFI环境下进行第一次设置。

  2.优化了不必要的程序，提升了‘登录’与‘注销’的速度。

- 版本ver1.3、ver1.2、ver1.1、ver1.0略

## **开发信息**

语言：Python 2.7.11

打包环境： windows7 Home Basic 32-bit

- gateway_tools.py说明：
  - 在文件最后选择'login'或'logout'来改变使用目的。
  - 需要打包的login.py或logout.py基于gateway_tools.py，仅仅改变最后的方式变量。

