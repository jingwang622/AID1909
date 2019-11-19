"""
read_db.py
pymysql 读数据库
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

# select 操作
sql = "select img from class1 where name = 'Abby';"
cur.execute(sql) # 执行语句
data = cur.fetchone()
with open('Abby.jpg','wb') as f:
    f.write(data[0])

# cur可迭代对象，通过迭代获取select结果
# for i in cur:
#     print(i)
# print("===============================")
# # 获取一个查询结果
# print(cur.fetchone())
#
# # 获取三个查询结果
# print(cur.fetchmany(3))
#
# # 获取所有查询结果
print(type(cur.fetchall()))

# 关闭游标和数据库连接
cur.close()
db.close()