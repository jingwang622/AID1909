"""
存储二进制文件
"""
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

# 存储文件
with open('timg.jpg','rb') as f:
    data = f.read()
try:
    sql = "update class1 set img=%s where name = 'Abby';"
    cur.execute(sql,[data])
    db.commit()
except:
    db.rollback()


# 关闭游标和数据库连接
cur.close()
db.close()