import logging
import time


def timeit(f):

    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        logging.info(f"共耗时 {round(time.time()-start, 4)}s")
        return ret

    return wrapper