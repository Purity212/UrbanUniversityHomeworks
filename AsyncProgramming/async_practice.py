import time
import asyncio
async def get_temp():
    await asyncio.sleep(2)
    print('Первое показание')
    print("25 C")

async def get_pres():
    await asyncio.sleep(4)
    print('Второе показание')
    print('101 kPa')

async def main():
    print("Старт")
    task_temp = asyncio.create_task(get_temp())
    task_pres = asyncio.create_task(get_pres())
    await task_temp
    await task_pres
    print("Финиш")

start = time.time()
asyncio.run(main())
finish = time.time()

print(f'Working time = {round(finish-start, 2)} seconds')