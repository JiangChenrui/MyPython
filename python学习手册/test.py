from collections import UserDict, UserList, deque
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(os.cpu_count())

# if __name__ == "__main__":
#     # 单线程
#     start = time.time()
#     for _ in range(4):
#         fib(35)
#     print("单线程耗时:", time.time() - start)  # 约 12 秒

#     # 多线程（4 线程）
#     start = time.time()
#     with ThreadPoolExecutor(max_workers=4) as executor:
#         numbers = [35] * 4
#         executor.map(fib, numbers)
#     print("多线程耗时:", time.time() - start)  # 约 12 秒（GIL 限制）

#     # 多进程（4 进程）
#     start = time.time()
#     with ProcessPoolExecutor() as executor:
#         numbers = [35] * 4
#         executor.map(fib, numbers)
#     print("多进程耗时:", time.time() - start)  # 约 3 秒（4 核 CPU）

def display(*args):
    print(time.strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    time.sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10

def main():
    display('Script starting.')
    executor = ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display('results:', results)
    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display('result {}: {}'.format(i, result))

if __name__ == "__main__":
    main()

