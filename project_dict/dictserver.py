from socket import *
from threading import Thread
from database import DataBase
class DictServer(Thread):
    def __init__(self,c):
        self.c = c
        self.db = DataBase()
        super().__init__()
    # 注册
    def register(self, name, passwd):
        if self.db.query_user_by_name(name):
            return "用户名有重复"
        else:
            self.db.insert_user(name,passwd)
            return "注册成功"
    # 登录
    def login(self, name, passwd):
        if self.db.query_user_by_name_passwd(name,passwd):
            return "登录成功"
        else:
            return "用户名或密码不正确"
    # 退出
    def exit(self):
        self.c.send("退出".encode())
        os._exit(0)
    # 查找单词
    def select_word(self,word,name):
        mean = self.db.select_mean_by_word(word)
        self.c.send(mean.encode())
        if mean is not "不存在":
            print("=============")
            self.db.insert_word_record(word,name)
    # 查找查询历史记录
    def select_history_record(self,name):
        print(name)
        history_record = self.db.select_history_record(name)
        print(history_record)
        self.c.send(history_record.encode())

    # 注销
    def log_out(self):
        pass
    def run(self):
        # 创建游标
        self.db.create_cur()
        while True:
            message = self.c.recv(1024)
            message_list = message.decode().split(" ")
            if not message or message_list[0] == 'E':
                return
            elif message_list[0] == "R":
                result = self.register(message_list[1],message_list[2])
                self.c.send(result.encode())
            elif message_list[0] == 'L':
                result = self.login(message_list[1],message_list[2])
                self.c.send(result.encode())
            elif message_list[0] == 'E':
                self.exit()
            elif message_list[0] == 'S':
                self.select_word(message_list[1],message_list[2])
            elif message_list[0] == 'H':
                self.select_history_record(message_list[1])
            elif message_list[0] == 'Z':
                pass
            else:
                print("请输入正确选项")




def main():
    # 创建套接字
    sockfd = socket(AF_INET,SOCK_STREAM)
    # 设置端口立即被重用
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # 设置链接本机网络地址
    sockfd.bind(('127.0.0.1',8880))
    # 设置监听
    sockfd.listen(1024)
    ds_list = []
    while True:
        print("等待链接....")
        try:
            c,addr= sockfd.accept()
            print("已经链接：...")
        except KeyboardInterrupt as e:
            print(e)
            sockfd.close()
        except Exception as e:
            print(e)
            continue
        # 有客户端链接
        ds = DictServer(c)
        ds.setDaemon(True)
        ds.start()

if __name__ == '__main__':
    main()