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
* 磁盘与内存交互对基本单位：页
* 数据库分配单位：段

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
5. 
