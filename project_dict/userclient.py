from socket import *
import getpass
class UserClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd
    def register(self):
        while True:
            tuple_name = self.input_message()
            repasswd = input("请输入确认密码：")
            if tuple_name[1] != repasswd:
                print("两次密码不一致")
                continue
            if (' ' in tuple_name[0]) or (' ' in tuple_name[1]):
                print("姓名或者密码有空格")
                continue
            message = "R " + tuple_name[0] + " " + tuple_name[1]
            self.sockfd.send(message.encode())
            result = self.sockfd.recv(1024)
            if result.decode() == "注册成功":
                return True
            else:
                print(result.decode())
                continue

    def login(self):
        while True:
            tuple_name = self.input_message()
            message = "L " + tuple_name[0] + " " + tuple_name[1]
            self.sockfd.send(message.encode())
            result = self.sockfd.recv(1024)
            if result.decode() == "登录成功":
                return tuple_name
            else:
                print(result.decode())
                continue

    def exit(self):
        message = "E"
        self.sockfd.send(message.encode())
        self.sockfd.recv(1024)
    def input_message(self):
        name = input("请输入用户姓名：")
        passwd = input("请输入密码：")
        return (name,passwd)
    def select_word(self,tuple_name):
        while True:
            word = input("请输入单词：")
            if word == "##":
                break
            message = "S " + word + " "+ tuple_name[0]
            self.sockfd.send(message.encode())
            result = self.sockfd.recv(1024)
            print(result.decode())
    def select_history_record(self,message):
            self.sockfd.send(message.encode())
            result = self.sockfd.recv(1024)
            print(result.decode())
    def enter_another_view(self,uc,tuple_name):
        while True:
            print("S 查单词\n"
                  "H 历史记录\n"
                  "Z 注销")
            choice = input("请输入二级操作命令:")
            if choice == "S":
                self.select_word(tuple_name)
            elif choice == "H":
                message = "H " + tuple_name[0]
                self.select_history_record(message)
            elif choice == "Z":
                return
            else:
                print("请输入正确选项")


def main():
    # 创建套接字
    sockfd = socket()
    # 服务器地址
    server_addr = ('127.0.0.1', 8880)
    # 连接服务器
    sockfd.connect(server_addr)
    # 发送消息
    uc = UserClient(sockfd)
    while True:
        print("R register\n"
              "L login\n"
              "E exit")
        choice = input("输入一级操作命令：")
        if choice == "R":
            if uc.register():
                choice = "L"
                tuple_name = uc.login()
                if tuple_name:
                    uc.enter_another_view(uc,tuple_name)
        elif choice == 'L':
            tuple_name = uc.login()
            if tuple_name:
                uc.enter_another_view(uc,tuple_name)
        else:
            uc.exit()

    sockfd.close()
if __name__ == '__main__':
    main()