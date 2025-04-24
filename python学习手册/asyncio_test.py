import asyncio

# 10个异步任务
async def task_coroutine(value):
    # 输出任务运行信息
    print(f'任务 {value} 开始运行')
    # 模拟异步等待，使每个任务休眠1秒
    await asyncio.sleep(1)
    
    # 输出任务运行信息
    print(f'任务 {value} 结束运行')

# 主协程定义
async def main():
    # 输出主协程启动信息
    print('主协程已启动')
    # 创建10个任务
    # 注意。任务的执行依赖于事件循环的调度，它会在其他所有协程执行完成后才会开始
    # 例如当前协程创建了任务，但是任务只有在当前协程挂起后才有可能开始执行
    started_tasks = [asyncio.create_task(task_coroutine(i), name=f'任务{i}') for i in range(10)]
    # 使得当前的协程（即 main 协程）挂起0.1秒，从而使得子任务运行
    # 如果没有这句代码，也没有之后的gather函数，子任务会在main函数将要结束时运行，此时事件循环还存在
    await asyncio.sleep(0.1)
    # 获取所有任务的集合
    all_tasks = asyncio.all_tasks()
    # 输出所有任务的详细信息
    for task in all_tasks:
        print(f'> {task.get_name()}, {task.get_coro()}')
    print("等待任务完成")
    # gather会收集传入的所有任务，并阻塞当前协程，直到所有任务都执行完毕
    # 没有gather函数，这样当前协程会直接结束，导致部分任务未能执行或未完成
    await asyncio.gather(*started_tasks)
    # gather函数类似于以下代码
    # 逐个等待每个任务完成
    for task in started_tasks:
        await task  # 等待单个任务完成

# 运行异步程序
asyncio.run(main())
