# 将元组转换成字符串
# import time
# tuple = (23,34,time.localtime())
# msg = "%s %-16s %s"%tuple  # %-16s左对齐
# print(msg)

# 输入密码不被看见，在pycharm中不可用，终端可用
# import getpass
# print("请输入密码：")
# passwd = getpass.getpass()
# print(passwd)

# 加密算法学习网址 https://www.cnblogs.com/pycode/p/hashlib.html hashlib
low = hashlib.md5()
low.update('ab'.encode('utf-8'))
res = low.hexdigest()
print("普通加密:",res)

high = hashlib.md5(b'beyondjie')
high.update('ab'.encode('utf-8'))
res = high.hexdigest()
print("采用key加密:",res)

# 输出结果：
# 普通加密: 187ef4436122d1cc2f40dc2b92f0eba0
# 采用key加密: 1b073f6b8cffe609751e4c98537b7653