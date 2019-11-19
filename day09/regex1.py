"""
regex1.py
"""
import re
s = "今年是2019年,建国70周年"
pattern = r"\d+"

# 返回匹配结果的迭代对象
it = re.finditer(pattern,s)
# 迭代match对象（为了获取匹配内容更丰富的信息）
for i in it:
    print(i.group()) # 获取match对象对应的匹配内容

# 完全匹配一个字符串
m = re.fullmatch(r'^.+$',s)
print(m.group())

# match 匹配字符串开头位置
m1 = re.match(r'\w+',s)
print(m1.group())

# search 匹配第一处
m2 = re.search(r'(\d+)',s).group()
print(m2)
