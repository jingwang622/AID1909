from multiprocessing import Process
class prime(Process):
    # 从begin到end所有指数之和
    def __init__(self,pr,begin,end):
        super().__init__()
        self.pr = pr
        self.begin = begin
        self.end = end

    def timeit(f):
        def wrapper(*args, **kwargs):
            start_time = time()
            res = f(*args, **kwargs)
            end_time = time()
            print("%s函数执行时间:%.8f" % (f.__name__, end_time - start_time))
            return res

        return wrapper

    def isPrime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n)):
            if n % i == 0:
                return False
        return True
    @timeit
    def run(self):
        for i in range(self.begin, self.end):
            if self.isPrime(i):
                self.pr.append(i)
        print("Sum:", sum(self.pr))

