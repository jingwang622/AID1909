"""
练习3：
使用数据库完成登录注册功能，数据表自己定

*注册方法，收集用户信息，将用户信息存储到数据库，用户名不能重复
*登录方法：获取用户名密码，与数据库信息比对，判定是否允许登录
"""
import pymysql
class DataBase:
    def __init__(self):
        self.db = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = '123456',
            database = 'business',
            charset = 'utf8'
        )
        self.cur = self.db.cursor()

    def register(self,name,passwd):
        sql = "select name,password from custom where name = '%s';"%name
        self.cur.execute(sql)
        if not self.cur.fetchall():
            try:
                sql = 'insert into custom(name,password) ' \
                      'values(%s,%s);'
                self.cur.execute(sql,[name,passwd])
                self.db.commit()
                return "注册成功"
            except:
                self.db.rollback()
                return "注册失败"

        else:
            return "注册失败"

    def login(self,name,passwd):
        sql = "select name,password from custom " \
              "where name = %s and password = %s;"
        self.cur.execute(sql,[name,passwd])
        if self.cur.fetchone():
            print("1111111")
            return "登录成功"
        else:
            return "登录失败"


if __name__ == '__main__':
    db = DataBase()
    # print(db.register("xiaoli",234))
    print(db.login("xiaoming",123))