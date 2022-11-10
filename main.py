
from msilib.schema import MsiPatchHeaders
import time
import threading
from concurrent.futures import ThreadPoolExecutor
class Account(object):
    """银行账户"""
    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()
    def deposit(self, money):
        # 通过锁保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance


def main():
    """主函数"""
    account = Account()
    # 创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(10000):
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    # 关闭线程池
    pool.shutdown()
    for future in futures:
        future.result()
    print(account.balance)


if __name__ == '__main__':
    main()