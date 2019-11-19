"""
获取输入内容，能够获取信息中星期几的第一个字母来判断一下是星期几，
如果地一个字母一样，则继续判断第二个字母
星期一：Monday
星期二：Tuesday
星期三：Wednesday
星期四：Thursday
星期五：Friday
星期六：Saturday
星期日：Sunday
"""
while True:
    weeknum = input("请输入英文星期：")
    if weeknum[0] == "M":
        print("星期一")
    elif weeknum[0] == "W":
        print("星期三")
    elif weeknum[0] == "F":
        print("星期五")
    elif weeknum[0] == "T":
        if weeknum[1] == "h":
            print("星期四")
        elif weeknum[1] == "u":
            print("星期二")
    elif weeknum[0] == "S":
        if weeknum[1] == "a":
            print("星期六")
        elif weeknum[1] == "u":
            print("星期日")




