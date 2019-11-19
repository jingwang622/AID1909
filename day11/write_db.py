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
                     database = 'stu',
                     charset = 'utf8')
# 生成游标对象(用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()

# 执行写数据库sql操作
# name = input("请输入姓名：")
# age = input("请输入年龄：")
# score = input("请输入分数：")
try:
    # Insert插入,合成sql语句要顾虑整体的格式，保证sql正确
    # 使用execute给sql传递参量
    # sql = "insert into class1(name,age,score) " \
    #       "values('%s',%s,%s);"%(name,age,score)
    # sql = "insert into class1(name,age,score) " \
    #       "values(%s,%s,%s);"
    # print(sql)
    # update 操作
    # sql = "update class1 set sex = 'm'" \
    #       "where name = 'Abby';"
    # cur.execute(sql)
    # sql = "delete from class1 where sex is null;"
    # cur.execute(sql)
    # 同时执行多次sql语句
    exe = []
    for i in range(3):
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        score = input("请输入分数：")
        exe.append((name,age,score))
    sql = "insert into class1(name,age,score)" \
          "values(%s,%s,%s);"
    cur.executemany(sql,exe)
    db.commit() # 同步写操作结果
except Exception as e:
    print(e)
    db.rollback()# 出错时将数据库回复到之前状态

# 关闭游标和数据库
cur.close()
db.close()