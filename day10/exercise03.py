import re
str = "诸葛亮"
print(re.match('\w{3}',str).group())