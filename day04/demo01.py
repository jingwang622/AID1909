import time
list01 = []
def get_time(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        time_continue = time_end - time_start
        print(time_continue)
    return wrapper
@get_time
def get_sum_zhishu():
    for r in range(2,10001):
        for c in range(r+1,10000):
            if r % c == 0:
                break
            if c == r+1:
                list01.append(r)
    print(sum(list01))
def main():
    get_sum_zhishu()
if __name__ == "__main__":
    main()




