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
        if self.cur.fetchall():
            pass
        else:
            return "注册失败"

    def login(self,name,passwd):
        pass


if __name__ == '__main__':
    db = DataBase()
    # db.register()
    # db.login()