import asyncio

# 定义一个简单的异步任务，模拟处理逻辑
async def simple_task(number):
    await asyncio.sleep(1)
    return number

# 定义一个异步任务，稍后取消指定任务
async def cancel_task(task):
    await asyncio.sleep(0.2)
    was_cancelled = task.cancel()
    print(f'已取消: {was_cancelled}')

# 主协程，调度其他任务
async def main():
    coro = simple_task(1)
    task = asyncio.create_task(coro)
    shielded = asyncio.shield(task)

    # 创建取消任务的协程
    asyncio.create_task(cancel_task(shielded))
    
    try:
        result = await shielded
        print(f'>获得: {result}')
    except asyncio.CancelledError:
        print('任务已被取消')

    await asyncio.sleep(1)
    
    print(f'保护任务: {shielded}')
    print(f'任务: {task}')

# 启动主协程
asyncio.run(main())
