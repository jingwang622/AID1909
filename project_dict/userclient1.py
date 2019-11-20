from socket import *
class UserClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd
    def register(self):
        while True:
            tuple_name = self.input_message()
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
                return True
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
    def select_word(self,choice):
        while True:
            self.sockfd.send(choice.encode())
    def select_history_record(self):
        while True:
            self.sockfd.send(choice.encode())
    def log_out(self):
        pass
    def enter_another_view(self):
        print("S 查单词\n"
              "H 历史记录\n"
              "Z 注销")
        choice = input("请输入二级操作命令:")
        if choice == "S":
            self.select_word(choice)
        elif choice == "H":
            self.select_history_record(choice)
        elif choice == "Z":
            self.log_out(choice)
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
                if uc.login():
                    uc.enter_another_view()
        elif choice == 'L':
            if uc.login():
                uc.enter_another_view()
        else:
            uc.exit()

    sockfd.close()
if __name__ == '__main__':
    main()