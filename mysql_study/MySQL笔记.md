## MySQL安装

[Mac安装mysql](https://blog.csdn.net/w605283073/article/details/80417866)

```shell
brew install mysql
# 启动mysql
mysql.server start
# 初始化
mysql_secure_installation
# 连接MySQL
mysql -u root -p
# 后台启动mysql
brew services start mysql
```

## innoDB数据存储
* 磁盘与内存交互对基本单位:页
* 数据库分配单位:段

## 索引

### 索引分类

1. 索引是帮助MySQL高效获取数据的数据结构
   * 优点
       * 降低数据库IO成本
       * 保证数据唯一性
       * 加速表和表的连接
       * 减少查询中分组和排序的时间
   * 缺点
       * 创建和维护都会耗费时间
       * 占用磁盘空间
       * 降低更新表的速度
2. 聚簇索引(叶子节点存储完整的记录)
	* 优点
       * 数据访问快
       * 排序查找和范围查找速度快
       * 节省大量IO操作
	* 缺点
       * 插入速度严重依赖插入顺序
       * 更新主键的代价很高
       * 二级索引访问需要两次索引查找
3. 二级索引
4. 联合索引

### 索引设计原则

1. 字段的数值有唯一性的限制
2. 频繁作为WHERE查询条件对字段
3. 经常GROUP BY和ORDER BY的列
4. UPDATE, DELETE的WHERE条件列
5. DISTINCT字段需要创建索引
6. 多表JOIN连接操作时，创建索引需要注意
7. 使用列的类型小的创建索引
8. 使用字符串前缀创建索引
9. 区分度高的列适合创建索引
10. 使用最频繁的列放到联合索引的左侧
11. 多个字段都要创建索引的情况下，联合索引优于单值索引

### 不适合创建索引的情况

1. 在where中用不到的字段，不要设置索引
2. 数据量小的表最好不要使用索引
3. 有大量重复数据的列上不要建立索引
4. 避免对经常更新的表创建过多的索引
5. 不建议用无序的值作为索引
6. 删除不再使用或者很少使用的索引
7. 不要定义冗余或重复的索引

### 查看系统性能参数

```mysql
SHOW [GLOBAL|SESSION] STATUS LIKE '参数';
```

一些常用的性能参数如下: 

* Connections:连接MySQL服务器的次数。

*  Uptime: MySQL服务器的上线时间

*  Slow_queries:慢查询的次数

*  Innodb_rows_read:Select查询返回的行数 

*  Innodb_rows_inserted:执行INSERT操作插入的行数 

*  Innodb_rows_updated:执行UPDATE操作更新的行数 

*  Innodb_rows_deleted:执行DELETE操作删除的行数 

*  Com_select:查询操作的次数

*  Com_insert:插入操作的次数。对于批量插入的 INSERT 操作，只累加一次。 

*  Com_update:更新操作的次数

*  Com_delete:删除操作的次数

### 统计SQL的查询成本：last_query_cost

```mysql
SHOW STATUS LIKE 'last_query_cost';
```

### 慢查询日志

```shell
mysqldumpslow -s t -t 5 /var/lib/mysql/atguigu01-slow.log
```

### 













