"""
write_db.py 写数据库
insert update delete
"""
import pymysql
import re

# 连接数据库
db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'dict',
                     charset = 'utf8')
# 生成游标对象(用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()

try:
    exe = []
    f = open('dict.txt', 'r')
    for line in f:
        # 获取单词和解释
        # word = line.split(" ")[0]
        # mean = line.split("  ")[-1]
        tup = re.findall(r'(\S+)\s+(.*)',line)[0]
        exe.append(tup)
    f.close()
    sql = "insert into words(word,mean)" \
          "values(%s,%s);"
    cur.executemany(sql,exe)
    db.commit() # 同步写操作结果
except Exception as e:
    print(e)
    db.rollback()# 出错时将数据库回复到之前状态

# 关闭游标和数据库
cur.close()
db.close()