# -*- coding: utf-8 -*-
"""
> **重点**：**多线程和多进程的比较**。
>
> 以下情况需要使用多线程：
>
> 1. 程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，
     所以使用线程而不是进程维护共享状态的代价相对较小。
> 2. 程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。
>
> 以下情况需要使用多进程：
>
> 1. 程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
> 2. 程序的输入可以并行的分成块，并且可以将运算结果合并。
> 3. 程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。
- 异步处理：从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，我们并不能保证任务将以某种顺序去执行，
因为执行顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给另一项任务。异步任务通常通过多任务协作处理的方式来实现，
由于执行时间和顺序的不确定，因此需要通过回调式编程或者`future`对象来获取任务执行的结果。
Python 3通过`asyncio`模块和`await`和`async`关键字（在Python 3.7中正式被列为关键字）来支持异步处理。
异步I/O - async / await
"""

import asyncio
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]  # 输出到终端
)


def timeit(f):

    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        logging.info(f"共耗时 {round(time.time()-start, 4)}s")
        return ret
    return wrapper


def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)

async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            logging.info(f'Prime =>{i}')
            primes.append(i)
        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        logging.info(f'Square =>{i*i}')
        squares.append(i * i)
        await asyncio.sleep(0.001)
    return squares


@timeit
def main():
    """主函数"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: logging.info(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
    main()