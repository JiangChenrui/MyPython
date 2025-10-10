import logging
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def timeit(f):

    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        logging.info(f"共耗时 {round(time.time()-start, 4)}s")
        return ret
    return wrapper

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    # 单线程
    start = time.time()
    for _ in range(4):
        fib(35)
    print("单线程耗时:", time.time() - start)  # 约 12 秒

    # 多线程（4 线程）
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        numbers = [35] * 4
        executor.map(fib, numbers)
    print("多线程耗时:", time.time() - start)  # 约 12 秒（GIL 限制）

    # 多进程（4 进程）
    start = time.time()
    # ProcessPoolExecutor中max_workers参数默认值是os.cpu_count()函数返回的cpu数量
    with ProcessPoolExecutor() as executor:
        numbers = [35] * 4
        executor.map(fib, numbers)
    print("多进程耗时:", time.time() - start)