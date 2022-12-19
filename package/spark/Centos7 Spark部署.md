
##  一、安装包下载：

Spark 官网下载: [https://spark.apache.org/downloads.html](https://spark.apache.org/downloads.html)

Hadoop 官网下载: [https://hadoop.apache.org/releases.html](https://hadoop.apache.org/releases.html)


目前使用Spark 版本为: spark-2.4.3  Hadoop版本为: hadoop-2.10.1



## 二、配置自登陆
检测是否可以自登陆，不需要密码则配置正常:

```csharp
ssh localhost
```
 

在搭建Hadoop环境时，出现localhost.localdomain: Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password)问题，

这个问题是由于即使是本机使用SSH服务也是需要对自己进行公私钥授权的，所以在本机通过ssh-keygen创建好公私钥，然后将公钥复制到公私钥的认证文件中就可以了

```csharp
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```


也有可能还会有权限问题报错

> Permission denied (publickey,gssapi-keyex,gssapi-with-mic).



增加ssh keys权限

```csharp
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```


## 三、下载并配置JAVA环境


1. 下载java

```csharp
sudo yum -y install gcc gcc-c++ make openssl-devel gmp-devel mpfr-devel libmpc-devel emacs-filesystem libmpcdevel libaio numactl autoconf automake libtool libffi-devel  snappy snappy-devel zlib zlib-devel bzip2 bzip2-devel lz4-devel libasan lsof sysstat telnet psmisc && sudo yum install -y which java-1.8.0-openjdk java-1.8.0-openjdk-devel && sudo yum clean all
```


2. 在Centos7上，通过yum install java，安装openjdk。安装后，执行echo $JAVA_HOME发现返回为空。说明JAVA_HOME没有配置，需要到/etc/profile中配置JAVA_HOME

查找并配置JAVA_HOME

```csharp
which java

ls -lrt /usr/bin/java

ls -lrt /etc/alternatives/java
```

通过该命令查询到openjdk的安装路径后，编辑/etc/profile文件中配置JAVA_HOME


```csharp
export JAVA_HOME=/data/etc/java/jdk1.8.0_291
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib:$CLASSPATH
export JAVA_PATH=${JAVA_HOME}/bin:${JRE_HOME}/bin
export PATH=$PATH:${JAVA_PATH}
```


## 四、Spark配置

1. 执行命令

```csharp
tar -xzvf spark-2.4.3-bin-hadoop2.7.tgz
cd spark-2.4.3-bin-hadoop2.7/conf
cp spark-defaults.conf.template spark-defaults.conf
```

2. 修改spark配置

vi spark-defaults.conf


```csharp
spark.executor.heartbeatInterval   110s
spark.rpc.message.maxSize         1024
spark.hadoop.dfs.replication      1
# 临时文件路径
spark.local.dir                   /data/spark_test/temp/spark-tmp
spark.driver.memory               10g
spark.driver.maxResultSize         10g
```


3. 修改启动 spark WEBUI master端口

```csharp
vi sbin/start-master.sh
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/7f9308776bcb438a8b24256c15b943eb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATGF1Z2hpbmdAbWU=,size_20,color_FFFFFF,t_70,g_se,x_16)


4. 启动spark服务:

```csharp
./sbin/start-all.sh
```

5. jps可以查看服务启动状态
![在这里插入图片描述](https://img-blog.csdnimg.cn/46736abeb231436da69e9a1e12be3257.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATGF1Z2hpbmdAbWU=,size_20,color_FFFFFF,t_70,g_se,x_16)

6. 查看端口是否正常启动:

lsof -i:19080
![在这里插入图片描述](https://img-blog.csdnimg.cn/d63694d85fa14fe69e576cf9a8781757.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATGF1Z2hpbmdAbWU=,size_20,color_FFFFFF,t_70,g_se,x_16)


7. 打开spark web 界面:

查看自身ip:

```csharp
ifconfig | grep inet 
```


打开web : 127.0.0.1:19080

![在这里插入图片描述](https://img-blog.csdnimg.cn/83a54b1326d8433c8b03fe08ec8abf89.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATGF1Z2hpbmdAbWU=,size_20,color_FFFFFF,t_70,g_se,x_16)


8. 运行example 测试是否正常运行：

```csharp
./bin/spark-submit --class org.apache.spark.examples.SparkPi --master spark://页面上显示的端口ip  ./examples/jars/spark-examples_2.11-2.4.3.jar
```


## 五、HDFS配置

1. 解压
```csharp
tar -xzvf hadoop-2.10.1.tar.gz

cd hadoop-2.10.1
```



2. 修改 etc/hadoop/hdfs-site.xml

```csharp
<configuration>
  <property>
     <name>dfs.replication</name>
     <value>1</value>
  </property>
  <property>
     <name>dfs.namenode.name.dir</name>
     <value>/data/spark_test/temp/hdfs/dfs/name</value>
  </property>
  <property>
     <name>dfs.datanode.data.dir</name>
     <value>/data/spark_test/temp/hdfs/dfs/data</value>
  </property>
  <property><name>dfs.permission</name><value>false</value></property>
<property>
    <name>dfs.client.block.write.replace-datanode-on-failure.policy</name>
    <value>NEVER</value>
</property>
<property><name>dfs.permissions.enabled</name><value>false</value></property>
<property><name>dfs.webhdfs.enabled</name><value>true</value></property>
</configuration>
```


3. 修改 etc/hadoop/core-site.xml

```csharp
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://自身ip:19000</value>
    </property>
    <!-- 指定hadoop运行时产生文件的存储路径 -->
    <property>
        <name>hadoop.tmp.dir</name>
        <!-- 配置到hadoop目录下temp文件夹 -->
        <value>/data/spark_test/temp/hdfs-tmp</value>
    </property>

    <!-- 当前用户全设置成root -->
    <property>
    <name>hadoop.http.staticuser.user</name>
    <value>root</value>
    </property>

</configuration>
```


4. 修改  etc/hadoop/hadoop-env.sh JAVA_HOME

配置自身JAVA_HOME到 env.sh中


5. 格式化hdfs

```csharp
/bin/hdfs namenode -format
```


6. 启动dfs

```csharp
./sbin/start-dfs.sh
```


7. 查看端口启动状态

```csharp
lsof -i:19000
```


8. 打开hdfs web 界面: 默认端口是50700

查看自身ip:

```csharp
ifconfig | grep inet 
```






