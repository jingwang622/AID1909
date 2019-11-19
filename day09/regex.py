"""
regex.py re模块
"""
import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"(\w+):(\d+)"

# re模块调用
l = re.findall(pattern,s)
print(l)

# compile对象调用
regex = re.compile(pattern)
l1 = regex.findall(s,0,14)
print(l1)

# 使用正则表达式切割字符串
l2 = re.split(r':|,',s,2)
print(l2)

# 替换正则匹配内容
l3 = re.sub(r'[^\w]','**',s,2)
print(l3)


l4 = re.subn(r'[^\w]','**',s,2)
print(l4)
