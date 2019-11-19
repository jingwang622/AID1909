"""
练习1： 编写程序完成：使用input输入一个单词，打印出该单词的解释（或者这一行），如果输入的单词单词本中没有，则打印“找不到该单词”
       温馨提示： 每个单词占一行
                单词和解释之间一定有空格
                单词按顺序排列
"""

word = input("单词:") # 待查找单词

# 默认r方式打开
f = open('dict.txt')

# 每次取一行
for line in f:
    # 提取一行中的单词
    tmp = line.split(' ')[0]
    # 遍历的单词已经比目标大了
    if tmp > word:
        print("没有找到该单词")
        break
    elif tmp == word:
        print(line)
        break
else:
    print("没有找到该单词")

f.close()










