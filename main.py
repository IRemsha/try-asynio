import threading
import asyncio
from asyncio.tasks import sleep


# threading - за управление переключением отвечает OS и живет с GIL (конкурентная многозадачность)
# asyncio - за управление переключением отвечает разработчик через await (декларативная многозадачность)
 
def generator(a):
    while True:
        yield a
        a += 2 

async def async_func (b):
    while True:
        await b
        b += 3 
    
async def aiocount(counter):
    while True:
        await asyncio.sleep(1/10)
        counter.append(1)

async def print_every_1_sec(counter):
     while True:
        await asyncio.sleep(1)
        print(f"Число элементов: {len(counter)}!\n-- 1 cек прошла.")

async def print_every_5_sec():
     while True:
        await asyncio.sleep(5)
        print('---- 5 cек прошло.')         

async def print_every_10_sec():
     while True:
        await asyncio.sleep(10)
        print('-------- 10 cек прошло.')   

async def main():
    counter = list()
    
    task = [
        aiocount(counter),
        print_every_1_sec(counter),
        print_every_5_sec(),
        print_every_10_sec()
    ]

    await asyncio.gather(*task)

asyncio.run(main()) 