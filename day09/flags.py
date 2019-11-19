"""
功能扩展标志
"""
import re
s = """Hello
北京
"""
# 只能匹配ascii编码
# regex = re.compile(r'\w+',flags = re.A)
regex = re.compile(r'\w+',flags=re.S)
l = regex.findall(s)
print(l)