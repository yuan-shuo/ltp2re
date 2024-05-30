## 指定PDF存放路径，批量将PDF构建至neo4j图数据库中

1.配置环境；

2.找到l2neo.py文件，把line18（link）修改成你的数据库登录账号密码；

3.找到main.py文件，把line22（link）修改成你的数据库登录账号密码，把line29（folder_path）改成PDF存放路径，把line33（target_dir）改成执行失败的PDF存放路径，当你的PDF出现问题无法被处理时，这个PDF会被转移至此目录；

4.把本地neo4j启动；

5.直接运行main.py就可以了。
