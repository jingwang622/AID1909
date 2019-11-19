import re
f = open('dict.txt','r')
for line in f:
    tup = re.findall(r'(\S+)\s+(.*)',line)
    print(tup)