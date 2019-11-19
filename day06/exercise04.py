"""
区间素数
"""

def is_prime(lower,upper):
    for i in range(lower,upper):
        if i == 1:
            pass


if __name__ == '__main__':
    lower = int(input("请您输入区间最小值："))
    upper = int(input("请您输入区间最大值："))
    is_prime(lower,upper)

