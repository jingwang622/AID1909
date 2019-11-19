"""
mysql.py
pymysql 操作的流程演示
"""
import pymysql
# 连接数据库
db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')
# 生成游标对象(用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()

# 执行各种数据库sql操作
cur.execute("delete from class1 where name = 'Tom';")
db.commit()

# 关闭游标和数据库
cur.close()
db.close()