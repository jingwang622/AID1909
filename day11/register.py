"""
write_db.py 写数据库
insert update delete
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'business',
                     charset = 'utf8')
# 生成游标对象(用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()
try:
    print("注册")
    name = input("请输入姓名：")
    password = input("请输入密码：")
    sql = "select name from custom where name = '%s';"%name
    cur.execute(sql)
    name_tuple = cur.fetchall()
    print(name_tuple)
    for item in name_tuple:
        print(item)
        if name not in item:
            sql = "insert into custom(name,password)" \
                  "values(%s,%s);"
            print(sql)
    cur.execute(sql,[name,password])
    db.commit() # 同步写操作结果
except Exception as e:
    print(e)
    db.rollback()# 出错时将数据库回复到之前状态

# 关闭游标和数据库
cur.close()
db.close()