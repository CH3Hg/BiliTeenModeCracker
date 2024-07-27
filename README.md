# 哔哩哔哩青少年模式密码自动化破解程序
这是一个基于python的哔哩哔哩青少年模式密码自动化破解程序
## 原理
利用ADB（安卓调试桥）进行模拟输入，自动尝试每一种密码组合，并在达到限制次数后等待至次日0：00继续执行
## 需要额外安装的库
subprocess  用于adb输入  
datetime  用于等待  
itertools  用于生成密码组合
## 需要额外安装的组件
adb  用于subprocess库的支持
## 用法
1.下载adb https://developer.android.com/tools/releases/platform-tools?hl=zh-cn  
2.解压压缩包，将文件夹存放至除C盘外的任意一个盘的根目录    
3.将其添加至环境变量  
4.下载并安装python https://www.python.org/downloads/  
5.使用pip安装第三方支持库（请先安装python）
6.下载脚本
7.打开手机的“ADB调试”，通常还需打开“开发者选项”  
8.使用数据线连接手机后双击运行脚本（不要通过IDLE运行，会在倒计时那一步卡住）  
###### 翻译由ChatGPT-4o提供
# Bilibili Teen Mode Password Automation Cracking Program
This is a Bilibili Teen Mode password automation cracking program based on Python.
## Principle
Using ADB (Android Debug Bridge) to simulate input, the program automatically attempts every possible password combination. If the attempt limit is reached, it waits until the next day at 00:00 to continue execution.
## Additional Libraries Required
subprocess: Used for ADB input  
datetime: Used for waiting  
itertools: Used for generating password combinations
## Additional Components Required
adb: Used to support the subprocess library
## Usage
1.Download ADB from https://developer.android.com/tools/releases/platform-tools?hl=zh-cn.  
2.Extract the compressed package and place the folder in the root directory of any drive other than the C drive.  
3.Add it to the environment variables.  
4.Download and install Python from https://www.python.org/downloads/.  
5.Use pip to install third-party support libraries (please install Python first).  
6.Download the script.  
7.Enable "ADB debugging" on your phone, usually found in "Developer Options".  
8.Connect your phone via a data cable and double-click to run the script (do not run through IDLE, as it will get stuck at the countdown step).  
###### Translation provided by ChatGPT-4o.
