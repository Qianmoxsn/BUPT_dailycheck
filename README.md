# Auto_Check_plus
2022/3/15  
by Xuan

## 环境准备
### 1.python
下载地址：https://www.python.org/downloads/windows/  
（py 3.7.8）：https://www.python.org/downloads/release/python-378rc1/
### 2.selenium库
`win+R`输入`cmd` 打开cmd  
>pip install selenium
### 3.浏览器  （以edge为例，其余同理）
_参考文章：https://blog.csdn.net/tk1023/article/details/109078613_  

浏览器驱动下载地址：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/  
>在`设置`-`关于Microphone Edge`中查询浏览器版本并下载**对应版本**驱动
#### 驱动安装：
1.解压安装包  
2.将`msedgedriver.exe`文件移动至python安装目录  
（默认为`C:\Users\**\AppData\Local\Programs\Python\Python3*`）  
+ 注：此版本不需要修改`msedgedriver.exe`文件名
# 代码修改
>在第40、41行填入自己的账号密码  

    if __name__ == '__main__':
        account = "****"
        password = "****"
        if login(account, password) is True:
            report()

        sleep(5)
        driver.close()
# 设置计划任务
参考文章：https://blog.csdn.net/mooncrystal123/article/details/83586780
### 打开任务计划程序应用
### 点击创建任务(基本任务)
<img height="" src="https://s3.bmp.ovh/imgs/2022/03/8ae9128da03322a8.png" width=""/>

## 设置
<img src="https://img-blog.csdnimg.cn/20181031164903790.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vb25jcnlzdGFsMTIz,size_16,color_FFFFFF,t_70"/>
<img src="https://img-blog.csdnimg.cn/2018103116494672.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vb25jcnlzdGFsMTIz,size_16,color_FFFFFF,t_70"/>

### 自行设置运行时间

<img src="https://img-blog.csdnimg.cn/20181031165133695.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vb25jcnlzdGFsMTIz,size_16,color_FFFFFF,t_70"/>  
<img src="https://img-blog.csdnimg.cn/20181031165455630.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vb25jcnlzdGFsMTIz,size_16,color_FFFFFF,t_70"/>
<img src = 'https://s3.bmp.ovh/imgs/2022/03/7fdacd32a0d59199.png' />

### 保存，运行

