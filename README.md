
## 基于 Django 框架的电商小项目 

![](https://img.shields.io/badge/Python-2.7-brightgreen.svg)
![](https://img.shields.io/badge/Django-1.11-green.svg)
![](https://img.shields.io/badge/MySQL-5.7.22-orange.svg)


#### 网站已部署到服务器 -> [查看](https://meicai.kangbingbing.com)

自学 Python 过程中练习的电商项目, 商品数据及图片从电商网站爬的。可参考 -> [链接](https://github.com/kangbingbing/Python/blob/master/dianshang.py)


## 主要功能：  
* 账号注册、登录等功能。
* 首页轮播图、商品类别、热销商品。
* 商品列表、搜索商品。
* 我的订单、收货地址、最近浏览。
* 添加购物车、结算。


## 环境
* Python 2.7
* Django 1.11
* MySQL 5.7.22


### 快速启动该项目
1.安装Python 2.x

2.安装MySQL 5.7 并创建tiantian数据库

    mysql -u root -p
    Enter password: 
    mysql> create database tiantian;
    
3.项目下载

    git clone https://github.com/kangbingbing/PythonWeb-Django.git

4.安装依赖包

    pip install -r requirements.txt

5.修改配置

```python
# setting.py
# 将数据库密码换成自己的
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tiantian',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```
6.建表

	生成迁移文件：根据模型类生成sql语句
    python manage.py makemigrations
    执行迁移：执行sql语句生成数据表
    python manage.py migrate
    
7.运行项目

    python manage.py runserver

在浏览器地址栏输入：[127.0.0.1:8000](http://127.0.0.1:8000/)



## 展示图

<img src="https://ws1.sinaimg.cn/large/9e1008a3ly1ftnchtn232j21y419ykjn.jpg" width="600" hegiht="400"/>

<img src="https://ws1.sinaimg.cn/large/9e1008a3ly1ftnchqn33sj21y61fmhdu.jpg" width="600" hegiht="400"/>

<img src="https://ws1.sinaimg.cn/large/9e1008a3ly1ftncg8ce89j221m1gcnpd.jpg" width="600" hegiht="400"/>

<img src="https://ws1.sinaimg.cn/large/9e1008a3ly1ftnchpqx47j21xu1eealx.jpg" width="600" hegiht="400"/>
