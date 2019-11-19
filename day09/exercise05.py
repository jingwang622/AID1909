"""
输出指定范围的素数
"""
def is_prime(lower,upper):
    for num in range(lower,upper+1):
        if num > 1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                print(num)

if __name__ == '__main__':
    lower = int(input("请您输出区间最小值:"))
    upper = int(input("请您输出区间最大值:"))
    is_prime(lower,upper)
