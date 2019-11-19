import re
str = "10f3.116c.e6a7"
regex1 = re.compile(r'(([a-f0-9]){4}.){2}([a-f|0-9]{4})(.[a-f|0-9]{4})?')

print(regex1.search(str).group())