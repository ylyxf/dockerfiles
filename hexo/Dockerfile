FROM centos:7
MAINTAINER ylyxf "ylyxf@126.com" 

# 生成网站内容 
# nodejs 用户生成博客
# python 用于脚本处理

#加入非官方源
ADD khara-nodejs-epel-7.repo /etc/yum.repos.d/khara-nodejs-epel-7.repo
#更新yum缓存
RUN yum makecache

#安装nodejs
RUN yum install -y nodejs nodejs-npm 
RUN yum install -y git

#安装hexo
RUN npm config set registry https://registry.npm.taobao.org 
RUN npm install hexo-cli -g

#下载博客代码
WORKDIR /var/tmp
RUN git clone https://github.com/ylyxf/blog.git

#安装hexo模块
WORKDIR /var/tmp/blog
RUN npm install

#增加python部署网站脚本
ADD updateblog.py /opt/blog/htbin/updateblog.py

#授权操作
RUN chmod +x /opt/blog/htbin/updateblog.py
RUN chmod -R a+w /var/tmp/blog


#增加nginx配置文件
VOLUME /var/blog

#设置工作目录
WORKDIR /opt/blog/
EXPOSE 8000

# 最后执行 docker run -d -p 8000:8000  -v /var/blog:/var/blog --name hexo whatsarchit/hexo python -m CGIHTTPServer
