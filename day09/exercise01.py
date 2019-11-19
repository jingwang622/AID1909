import re
"""
匹配邮箱地址
abc@123.com
def@tedu.cn
abcd@xxx.com.cn
"""
# list01 = re.search('\w+\@\d+\.com','abc@123.com def@tedu.cn abcd@xxx.com.cn').group()
# print(list01)
"""
匹配数字
12 -133 1.5 -4.7 45.8% 1/2
"""
# list01 = re.findall('-?\d+\.?/?\d?\%?','12 -133 1.5 -4.7 45.8% 1/2')
# print(list01)
"""
匹配一段文字中书名
《xxx》《啊-大海》《哈姆雷特》
"""
list01 = re.findall(r'《.+?》','《xxx》《啊-大海》《哈姆雷特》')
print(list01)

"""
匹配身份正号（18）
"""