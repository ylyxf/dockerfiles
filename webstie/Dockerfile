FROM centos:7
MAINTAINER ylyxf "ylyxf@126.com" 

#加入非官方源
ADD nginx.repo /etc/yum.repos.d/nginx.repo

#更新yum缓存
RUN yum makecache

#安装nignx
RUN yum install -y nginx

#增加nginx配置文件
ADD nginx.conf /etc/nginx/nginx.conf

#增加数据卷
#VOLUME /var/blog

EXPOSE 80

# 最后执行 docker run -d -p 80:80 --name website -v /var/blog:/var/blog:ro whatsarchit/website:test nginx -g "daemon off;"