from concurrent.futures import ThreadPoolExecutor, as_completed

from flags import get_flag, show, main

MAX_WORKERS = 20

def download_one(cc):
    get_flag(cc)
    show(cc)
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))

def download_many_ac(cc_list):
    # cc_list = cc_list[:5]
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)

if __name__ == '__main__':
    main(download_many)
    main(download_many_ac)

