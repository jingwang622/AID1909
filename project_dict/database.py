import pymysql
import time
import hashlib
class DataBase:
    def __init__(self,host = 'localhost',port = 3306,user = 'root',password='123456',database ='dict',charset='utf8'):
        self.db = pymysql.connect(host=host,
                         user=user,
                         password=password,
                         database=database,
                         charset=charset)
        self.cur = None
    def create_cur(self):
        self.cur = self.db.cursor()
    def close(self):
        if self.cur:
            self.cur.close()
        self.db.close()
    def change_passwd(self,passwd):
        salt = "#0789"
        hash = hashlib.md5(salt.encode())
        hash.update(passwd.encode())
        res = hash.hexdigest()
        return res
    def query_user_by_name(self,name):
        sql = "select name,passwd from user where name = '%s';"%name
        self.cur.execute(sql)
        if self.cur.fetchone():
            return True
        else:
            return False

    def insert_user(self,name,passwd):
        try:
            passwd = self.change_passwd(passwd)
            sql = "insert into user(name,passwd) values(%s,%s);"
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            self.db.close()

    def query_user_by_name_passwd(self, name,passwd):
        passwd = self.change_passwd(passwd)
        sql = "select name,passwd from user where name = %s and passwd = %s;"
        self.cur.execute(sql,[name,passwd])
        if self.cur.fetchone():
            return True
        else:
            return False
    def select_mean_by_word(self,word):
        sql = "select mean from words where word = '%s'"%word
        self.cur.execute(sql)
        mean = self.cur.fetchone()
        if mean:
            return "单词解释为："+mean[0]
        else:
            return "不存在"
    def insert_word_record(self,word,name):
        try:
            sql = "insert into historyrecord(name,word,querytime) values(%s,%s,now());"
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            self.db.close()
    def select_history_record(self,name):
        record_new = ""
        sql = "select name,word,querytime from historyrecord where name = '%s' order by querytime LIMIT 10" % name
        print(sql)
        self.cur.execute(sql)
        record = self.cur.fetchall()
        if record:
            return record
        else:
            return "没有记录"