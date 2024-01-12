## MySQL 安装

[Mac 安装 mysql](https://blog.csdn.net/w605283073/article/details/80417866)

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

[字段扩容](https://mp.weixin.qq.com/s/R9j58nSXgKNK94PYMB-Otg)

## innoDB 数据存储

- 磁盘与内存交互对基本单位:页
- 数据库分配单位:段

## 索引

### 索引分类

1. 索引是帮助 MySQL 高效获取数据的数据结构
   - 优点
     - 降低数据库 IO 成本
     - 保证数据唯一性
     - 加速表和表的连接
     - 减少查询中分组和排序的时间
   - 缺点
     - 创建和维护都会耗费时间
     - 占用磁盘空间
     - 降低更新表的速度
2. 聚簇索引(叶子节点存储完整的记录)
   - 优点
     - 数据访问快
     - 排序查找和范围查找速度快
     - 节省大量 IO 操作
   - 缺点
     - 插入速度严重依赖插入顺序
     - 更新主键的代价很高
     - 二级索引访问需要两次索引查找
3. 二级索引
4. 联合索引

### 索引设计原则

1. 字段的数值有唯一性的限制
2. 频繁作为 WHERE 查询条件对字段
3. 经常 GROUP BY 和 ORDER BY 的列
4. UPDATE, DELETE 的 WHERE 条件列
5. DISTINCT 字段需要创建索引
6. 多表 JOIN 连接操作时，创建索引需要注意
7. 使用列的类型小的创建索引
8. 使用字符串前缀创建索引
9. 区分度高的列适合创建索引
10. 使用最频繁的列放到联合索引的左侧
11. 多个字段都要创建索引的情况下，联合索引优于单值索引

### 不适合创建索引的情况

1. 在 where 中用不到的字段，不要设置索引
2. 数据量小的表最好不要使用索引
3. 有大量重复数据的列上不要建立索引
4. 避免对经常更新的表创建过多的索引
5. 不建议用无序的值作为索引
6. 删除不再使用或者很少使用的索引
7. 不要定义冗余或重复的索引

### 索引失效

1. 最佳做前缀匹配法则
2. 计算、函数、类型转换导致索引失效
3. 不等于
4. 联合索引中间的索引判断有范围

### 优化数据库结构

1. 拆分表
2. 增加中间表
3. 增加冗余字段
4. 优化数据类型
5. 优化插入记录的速度
6. 使用非空约束
7. 分析表、检查表和优化表

### 查看系统性能参数

```mysql
SHOW [GLOBAL|SESSION] STATUS LIKE '参数';
```

一些常用的性能参数如下:

- Connections:连接 MySQL 服务器的次数。

- Uptime: MySQL 服务器的上线时间

- Slow_queries:慢查询的次数

- Innodb_rows_read:Select 查询返回的行数

- Innodb_rows_inserted:执行 INSERT 操作插入的行数

- Innodb_rows_updated:执行 UPDATE 操作更新的行数

- Innodb_rows_deleted:执行 DELETE 操作删除的行数

- Com_select:查询操作的次数

- Com_insert:插入操作的次数。对于批量插入的 INSERT 操作，只累加一次。

- Com_update:更新操作的次数

- Com_delete:删除操作的次数

### 统计 SQL 的查询成本：last_query_cost

```mysql
SHOW STATUS LIKE 'last_query_cost';
```

### 慢查询日志

```shell
mysqldumpslow -s t -t 5 /var/lib/mysql/atguigu01-slow.log
```

## 事务

保持数据一致性，一组操作单元，使数据从一种状态变换到另一种状态

### 事务的ACID特性

* 原子性
* 一致性
* 隔离性-事务的执行不能被其它事务干扰
* 持久性

### 事务的状态

活动的->部分提交的->提交的

失败的->中止的

### 数据并发问题

1. 脏写

    对于两个事务SessionA、SessionB，A修改了另一个事务B修改过的数据，那就意味着发生了脏写

2. 脏读

    对于两个事务SessionA、SessionB，A读取了B更新但还没提交的字段，之后B回滚，A读取的内容是`临时且无效`的

3. 不可重复读

    A读取了一个字段，B更新了该字段，之后A再次读取了同一个字段

4. 幻读

    A读取了一个字段，B在该表插入了一些新的行，之后A再次读取会多出几行

### SQL种的四种隔离级别

1. READ UNCOMMITTED：读未提交
2. READ COMMITED：读已提交
3. REPEATABLE READ：可重复读
4. SERIALIZABLE：可串行化

|     隔离级别     | 脏读可能性 | 不可重复读可能性 | 幻读可能性 | 加锁读 |
| :--------------: | :--------: | :--------------: | :--------: | :----: |
| READ UNCOMMITTED |    Yes     |       Yes        |    Yes     |   No   |
|  READ COMMITED   |     No     |       Yes        |    Yes     |   No   |
| REPEATABLE READ  |     No     |        No        |    Yes     |   No   |
|   SERIALIZABLE   |     No     |        No        |     No     |  Yes   |

查看隔离级别

```mysql
# 查看隔离级别，MySQL 5.7.20的版本之前：
SHOW VARIABLES LIKE 'tx_isolation';
# 查看隔离级别，MySQL 5.7.20的版本及之后：
SHOW VARIABLES LIKE 'transaction_isolation';
SELECT @@transaction_isolation;
# 设置隔离级别
SET [GLOBAL|SESSION] TRANSACTION_ISOLATION = '隔离级别'
#其中，隔离级别格式：
> READ-UNCOMMITTED
> READ-COMMITTED
> REPEATABLE-READ
> SERIALIZABLE
```

## 锁

### 1. 从数据操作类型划分：读锁、写锁

### 2. 从数据操作的粒度划分：表级锁、页级锁、行锁

- 表锁
    1. 表级别的共享锁（S锁）、排他锁（X锁）
    
        共享锁（S锁）
    
        ```mysql
        SELECT column FROM table ... LOCK IN SHARE MODE
        ```
    
        排他锁（X锁）
    
        ```mysql
        SELECT column FROM table ... FOR UPDATE;
        ```
    
    2. 意向锁
    
    3. 自增锁
    
    4. 元数据锁
    
- 行锁
    1. 记录锁
    2. 间隙锁
    3. 临键锁
    4. 插入意向锁

* 页锁

### 3. 从对待锁的态度划分

* 悲观锁
* 乐观锁

### 4. 按加锁的方式划分

* 隐式锁
* 显式锁

### 5.其它锁

* 全局锁
* 死锁















































