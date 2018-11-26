# learnselenium
学习Selenium爬虫，模拟登录PayPal。免责声明：本代码仅用于学习Selenium，不可用于大规模测试登录PayPal或者对其发起DDos攻击，违者后果自负。编写本代码视为自身学习目的，特别是用Python实现多线程/多进程间通信，理解并发与并行的实际应用。

运行环境部署
----
`CentOS7`
* Pyhton虚拟环境安装
* Selenium + Chrome + WebDriver环境安装
* 环境测试

### Pyhton虚拟环境安装
```Shell
cd $HOME
curl https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh -O | sh
按提示完成安装后再输入以下命令创建Python3.6.6的虚拟环境
conda create -n learnselenium python=3.6.6
conda activate learnselenium

##### 安装依赖 
pip install requests Sqlite3Worker selenium

##### 安装chromedriver
cd $HOME/anaconda3/bin
wget https://chromedriver.storage.googleapis.com/2.44/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm -f chromedriver_linux64.zip

./chromedriver --version
ChromeDriver 2.44.609551 (5d576e9a44fe4c5b6a07e568f1ebc753f1214634)

##### 安装chome浏览器
cd $HOME
wget https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/609211/chrome-linux.zip
unzip chrome-linux.zip
cd chrome-linux

./chrome --version
Chromium 72.0.3616.0

##### 修改PATH
vim ~/.bash_profile
$PATH:$HOME/chrome-linux
cd $HOME

chrome --version
如果没有任何问题，环境安装完成
```
